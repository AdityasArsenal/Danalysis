import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Azure SQL Database configuration
DB_CONFIG = {
    'server': os.environ.get("AZURE_SQL_SERVER", 'esgdatadb.database.windows.net,1433'),
    'database': os.environ.get("AZURE_SQL_DATABASE", 'ESGDataDB'),
    'username': os.environ.get("AZURE_SQL_USERNAME", 'CloudSAfbce9c74'),
    'password': os.environ.get("AZURE_SQL_PASSWORD", 'InsideOut@123'),
    'driver': '{ODBC Driver 18 for SQL Server}'
}

def get_connection():
    """Create a connection to the Azure SQL database."""
    try:
        conn_str = (
            f'DRIVER={DB_CONFIG["driver"]};'
            f'SERVER={DB_CONFIG["server"]};'
            f'DATABASE={DB_CONFIG["database"]};'
            f'UID={DB_CONFIG["username"]};'
            f'PWD={DB_CONFIG["password"]};'
            f'Encrypt=yes;'
            f'TrustServerCertificate=no;'
            f'Connection Timeout=60;'
        )
        return pyodbc.connect(conn_str)
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def insertion_company(company_name, file_name, url):
    """Insert a company into the Companies table and return its ID."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Check if company exists to avoid duplicates
        cursor.execute(
            'SELECT company_id FROM Companies WHERE company_name = ?',
            (company_name,)
        )
        row = cursor.fetchone()
        if row:
            return row[0]

        # Insert new company
        cursor.execute(
            '''
            INSERT INTO Companies (company_name, file_name, url)
            OUTPUT INSERTED.company_id
            VALUES (?, ?, ?)
            ''',
            (company_name, file_name, url)
        )
        company_id = cursor.fetchone()[0]
        conn.commit()
        return company_id
    except pyodbc.Error as e:
        print(f"Error inserting company {company_name}: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def batch_insert_context_references(context_refs):
    """Batch insert unique context references and return a map of context_ref to context_ref_id."""
    conn = get_connection()
    cursor = conn.cursor()
    context_id_map = {}

    try:
        # Get existing context references
        cursor.execute('SELECT context_ref, context_ref_id FROM Context_References')
        for row in cursor.fetchall():
            context_id_map[row[0]] = row[1]

        # Filter out already existing context refs and 'None'
        new_context_refs = [cr for cr in set(context_refs) if cr not in context_id_map and cr != 'None']

        # Prepare batch
        if new_context_refs:
            cursor.executemany(
                '''
                INSERT INTO Context_References (context_ref, description)
                VALUES (?, ?)
                ''',
                [(cr, f"Context for {cr}") for cr in new_context_refs]
            )
            conn.commit()

            # Update context_id_map
            cursor.execute('SELECT context_ref, context_ref_id FROM Context_References')
            for row in cursor.fetchall():
                context_id_map[row[0]] = row[1]

        return context_id_map
    except pyodbc.Error as e:
        print(f"Error inserting context references: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def batch_insert_units(unit_refs):
    """Batch insert unique unit references and return a map of unit_ref to unit_id."""
    conn = get_connection()
    cursor = conn.cursor()
    unit_id_map = {}

    try:
        # Get existing units
        cursor.execute('SELECT unit_ref, unit_id FROM Units')
        for row in cursor.fetchall():
            unit_id_map[row[0]] = row[1]

        # Filter out already existing unit refs and 'None'
        new_unit_refs = [ur for ur in set(unit_refs) if ur not in unit_id_map and ur != 'None']

        # Prepare batch
        if new_unit_refs:
            cursor.executemany(
                '''
                INSERT INTO Units (unit_ref, description)
                VALUES (?, ?)
                ''',
                [(ur, f"Unit for {ur}") for ur in new_unit_refs]
            )
            conn.commit()

            # Update unit_id_map
            cursor.execute('SELECT unit_ref, unit_id FROM Units')
            for row in cursor.fetchall():
                unit_id_map[row[0]] = row[1]

        return unit_id_map
    except pyodbc.Error as e:
        print(f"Error inserting units: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def insertion_kpi_definition(category, kpi_names, units, decimals, reference_units):
    """Insert KPI definitions and return a map of kpi_name to kpi_definition_id."""
    conn = get_connection()
    cursor = conn.cursor()
    kpi_id_map = {}

    try:
        # Get existing KPI definitions
        cursor.execute('SELECT kpi_name, kpi_definition_id FROM KPI_Definitions')
        for row in cursor.fetchall():
            kpi_id_map[row[0]] = row[1]

        # Insert new KPIs one by one to avoid duplicate key issues
        for kpi_name in kpi_names:
            if kpi_name not in kpi_id_map:
                try:
                    cursor.execute(
                        '''
                        INSERT INTO KPI_Definitions (kpi_name, category, description)
                        VALUES (?, ?, ?)
                        ''',
                        (kpi_name, category, f"Auto-generated for {kpi_name}")
                    )
                    # Get the ID of the newly inserted KPI
                    cursor.execute('SELECT kpi_definition_id FROM KPI_Definitions WHERE kpi_name = ?', (kpi_name,))
                    row = cursor.fetchone()
                    if row:
                        kpi_id_map[kpi_name] = row[0]
                    conn.commit()
                except pyodbc.IntegrityError as e:
                    # If duplicate key, just retrieve the existing ID
                    if "UK_KPI_Definitions_kpi_name" in str(e):
                        conn.rollback()
                        cursor.execute('SELECT kpi_definition_id FROM KPI_Definitions WHERE kpi_name = ?', (kpi_name,))
                        row = cursor.fetchone()
                        if row:
                            kpi_id_map[kpi_name] = row[0]
                    else:
                        conn.rollback()
                        raise

        return kpi_id_map
    except pyodbc.Error as e:
        print(f"Error inserting KPI definitions: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def batch_insert_company_kpi_data(company_id, kpi_names, values, periods, context_refs, unit_refs, decimals, kpi_id_map, context_id_map, unit_id_map):
    """Batch insert company KPI data."""
    conn = get_connection()
    cursor = conn.cursor()
    inserted_ids = []

    try:
        batch = []
        for kpi_name, value, period, context_ref, unit_ref, decimal in zip(kpi_names, values, periods, context_refs, unit_refs, decimals):
            if kpi_name in kpi_id_map:
                kpi_definition_id = kpi_id_map[kpi_name]
                context_ref_id = context_id_map.get(context_ref) if context_ref != 'None' else None
                unit_id = unit_id_map.get(unit_ref) if unit_ref != 'None' else None

                # Parse period
                period_start = period_end = None
                if period != 'None' and period != 'NA':
                    try:
                        start_str, end_str = period.split('--')
                        period_start = datetime.strptime(start_str, '%Y-%m-%d').date()
                        period_end = datetime.strptime(end_str, '%Y-%m-%d').date()
                    except ValueError as e:
                        print(f"Invalid period format for {kpi_name}: {period}, error: {e}")

                batch.append((
                    company_id, kpi_definition_id, context_ref_id, unit_id,
                    str(value), period_start, period_end, decimal
                ))

        if batch:
            cursor.executemany(
                '''
                INSERT INTO Company_KPI_Data (company_id, kpi_definition_id, 
                                             context_ref_id, unit_id, value, 
                                             period_start, period_end, decimals)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                batch
            )
            conn.commit()
            inserted_ids = [row[0] for row in batch]  # Note: company_kpi_data_id is auto-generated by NEWID()

        return inserted_ids
    except pyodbc.Error as e:
        print(f"Error inserting company KPI data: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

def insert_aggregated_kpi_data(company_id, kpi_name, value, kpi_id_map):
    """Insert aggregated KPI data."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if kpi_name in kpi_id_map:
            kpi_definition_id = kpi_id_map[kpi_name]
            cursor.execute(
                '''
                INSERT INTO Aggregated_KPI_Data (company_id, kpi_definition_id, value)
                VALUES (?, ?, ?)
                ''',
                (company_id, kpi_definition_id, str(value))
            )
            conn.commit()
            return kpi_definition_id  # Return kpi_definition_id as a proxy for success
        return None
    except pyodbc.Error as e:
        print(f"Error inserting aggregated KPI data for {kpi_name}: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()