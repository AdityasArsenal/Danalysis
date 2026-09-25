# Danalysis

Danalysis is a Python-based data analysis and ingestion project for company ESG data. It downloads company XBRL/XML reports, extracts Environmental, Social, and Governance (ESG) key performance indicators (KPIs), stores the results in Azure SQL Database, and exports processed data to Excel workbooks.

## Features

- Download company XML/XBRL reports from URLs listed in an Excel workbook.
- Extract ESG data across three categories:
  - Environmental
  - Social
  - Governance
- Store company information, KPI definitions, context references, units, and KPI values in SQL Server/Azure SQL Database.
- Generate aggregated KPI records for selected metrics.
- Export extracted KPI data and missing KPI names to Excel files.
- Remove duplicate company records while preserving input order.

## Project Structure

```text
Danalysis/
├── requirements.txt
├── src/
│   ├── main.py                    # Main processing pipeline
│   ├── scraper.py                 # Downloads XML files from Excel-listed URLs
│   ├── add_data_to_DB.py          # Azure SQL database operations
│   ├── add_data_to_sheet.py       # Writes extracted data to Excel workbooks
│   ├── KEnvironmental_handeler.py  # Environmental KPI extraction
│   ├── KSocial_handeler.py        # Social KPI extraction
│   ├── KGovernance_handeler.py    # Governance KPI extraction
│   ├── cleanup_database.py        # Database cleanup utilities
│   ├── create_db_schema.sql       # SQL Server database schema
│   ├── extra_stuff/               # Supporting input files
│   ├── ex_sheets/                 # Example/input spreadsheets
│   ├── ex_xmls/                   # Example XML files
│   ├── new_exls/                  # Generated Excel output
│   └── new_xml/                   # Downloaded XML files
└── README.md
```

## Requirements

- Python 3.9 or newer
- Microsoft SQL Server or Azure SQL Database
- ODBC Driver 18 for SQL Server
- An Excel workbook containing company names and XML/XBRL URLs
- Python packages used by the project:
  - `requests`
  - `openpyxl`
  - `pyodbc`
  - `python-dotenv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AdityasArsenal/Danalysis.git
   cd Danalysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   pip install openpyxl pyodbc python-dotenv
   ```

   The additional packages are included here because they are imported by the source code. They should also be added to `requirements.txt` for reproducible setup.

## Database Setup

1. Create an Azure SQL Database or SQL Server database.
2. Execute [`src/create_db_schema.sql`](src/create_db_schema.sql) to create the required tables and indexes.
3. Create a `.env` file in the project root with your database connection settings:

   ```env
   AZURE_SQL_SERVER=your-server.database.windows.net,1433
   AZURE_SQL_DATABASE=your_database_name
   AZURE_SQL_USERNAME=your_username
   AZURE_SQL_PASSWORD=your_password
   ```

   Do not commit `.env` files, passwords, API keys, or other secrets to the repository.

## Input Data

The processing pipeline expects an Excel workbook containing at least:

- Company names in column `A`
- XML/XBRL report URLs in column `E`

Update the input path and processing limits in `src/main.py` if your workbook has a different location or structure.

## Usage

From the repository root, run:

```bash
python src/main.py
```

The pipeline will:

1. Read company names and report URLs from the configured Excel workbook.
2. Download the XML/XBRL reports into the generated `new_xml/` directory.
3. Parse Environmental, Social, and Governance KPI data.
4. Insert companies, KPI definitions, units, context references, and KPI values into the configured database.
5. Create Excel output files in `new_exls/`.
6. Print processing and insertion totals to the console.

## Database Schema

The SQL schema defines the following main tables:

- `Companies` — company names, source files, and report URLs.
- `KPI_Definitions` — KPI names, categories, and descriptions.
- `Context_References` — XBRL context references.
- `Units` — measurement unit references.
- `Company_KPI_Data` — raw KPI values associated with companies and reporting periods.
- `Aggregated_KPI_Data` — selected aggregated KPI values.

## Output

Generated files may include:

- Downloaded XML/XBRL reports in `new_xml/`.
- Company-specific Excel workbooks in `new_exls/`.
- Separate workbook sheets for Environmental, Social, and Governance results.
- A list of KPI names that were not found in the source reports.

Generated files and local database configuration should remain uncommitted unless they are intentionally being shared.

## Security Notes

- Use environment variables for database credentials.
- Never publish passwords or connection secrets in source files.
- Review and rotate any credentials that may have been exposed in development files.
- Use least-privilege database permissions where possible.

## Contributing

1. Create a feature branch.
2. Make your changes and add tests where appropriate.
3. Verify the pipeline against representative XML and Excel inputs.
4. Open a pull request with a clear description of the change.

## License

No license has been specified for this repository yet.
