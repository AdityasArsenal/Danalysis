-- Create Companies table
CREATE TABLE Companies (
    company_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    company_name NVARCHAR(255) NOT NULL,
    file_name NVARCHAR(255),
    url NVARCHAR(MAX),
    CONSTRAINT UK_Companies_company_name UNIQUE (company_name)
);

-- Create KPI_Definitions table
CREATE TABLE KPI_Definitions (
    kpi_definition_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    kpi_name NVARCHAR(255) NOT NULL,
    category NVARCHAR(50),
    description NVARCHAR(MAX),
    CONSTRAINT UK_KPI_Definitions_kpi_name UNIQUE (kpi_name),
    CONSTRAINT CHK_category CHECK (category IN ('Environmental', 'Social', 'Governance'))
);

-- Create Context_References table
CREATE TABLE Context_References (
    context_ref_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    context_ref NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX),
    CONSTRAINT UK_Context_References_context_ref UNIQUE (context_ref)
);

-- Create Units table
CREATE TABLE Units (
    unit_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    unit_ref NVARCHAR(255) NOT NULL,
    description NVARCHAR(MAX),
    CONSTRAINT UK_Units_unit_ref UNIQUE (unit_ref)
);

-- Create Company_KPI_Data table
CREATE TABLE Company_KPI_Data (
    company_kpi_data_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    company_id UNIQUEIDENTIFIER NOT NULL,
    kpi_definition_id UNIQUEIDENTIFIER NOT NULL,
    context_ref_id UNIQUEIDENTIFIER NULL,
    unit_id UNIQUEIDENTIFIER NULL,
    value NVARCHAR(MAX) NOT NULL, -- Stores various formats (numbers, percentages, text)
    period_start DATE,
    period_end DATE,
    decimals NVARCHAR(50),
    created_at DATETIME2 DEFAULT GETDATE(),
    CONSTRAINT FK_Company_KPI_Data_Companies FOREIGN KEY (company_id) REFERENCES Companies(company_id),
    CONSTRAINT FK_Company_KPI_Data_KPI_Definitions FOREIGN KEY (kpi_definition_id) REFERENCES KPI_Definitions(kpi_definition_id),
    CONSTRAINT FK_Company_KPI_Data_Context_References FOREIGN KEY (context_ref_id) REFERENCES Context_References(context_ref_id),
    CONSTRAINT FK_Company_KPI_Data_Units FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);

-- Create Aggregated_KPI_Data table
CREATE TABLE Aggregated_KPI_Data (
    aggregated_kpi_data_id UNIQUEIDENTIFIER PRIMARY KEY DEFAULT NEWID(),
    company_id UNIQUEIDENTIFIER NOT NULL,
    kpi_definition_id UNIQUEIDENTIFIER NOT NULL,
    value NVARCHAR(MAX) NOT NULL,
    period_start DATE,
    period_end DATE,
    created_at DATETIME2 DEFAULT GETDATE(),
    CONSTRAINT FK_Aggregated_KPI_Data_Companies FOREIGN KEY (company_id) REFERENCES Companies(company_id),
    CONSTRAINT FK_Aggregated_KPI_Data_KPI_Definitions FOREIGN KEY (kpi_definition_id) REFERENCES KPI_Definitions(kpi_definition_id)
);

-- Create indexes for performance
CREATE NONCLUSTERED INDEX IDX_Company_KPI_Data_company_id ON Company_KPI_Data(company_id);
CREATE NONCLUSTERED INDEX IDX_Company_KPI_Data_kpi_definition_id ON Company_KPI_Data(kpi_definition_id);
CREATE NONCLUSTERED INDEX IDX_Aggregated_KPI_Data_company_id ON Aggregated_KPI_Data(company_id);
CREATE NONCLUSTERED INDEX IDX_Aggregated_KPI_Data_kpi_definition_id ON Aggregated_KPI_Data(kpi_definition_id);