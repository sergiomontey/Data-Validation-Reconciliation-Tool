# 📊 Data Validation & Reconciliation Tool

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Pandas](https://img.shields.io/badge/Powered%20by-Pandas-150458.svg)
![SQLAlchemy](https://img.shields.io/badge/Database-SQLAlchemy-red.svg)
![License](https://img.shields.io/badge/License-Proprietary-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **Enterprise-grade desktop application for ETL validation and data reconciliation** - Compare source and target systems to find data mismatches after ETL operations with comprehensive validation, automated scheduling, and intelligent alerting.

## 🎯 Overview

Data Validation & Reconciliation Tool is a powerful desktop application designed for data engineers, ETL developers, and quality assurance teams who need to ensure data accuracy across systems. Built with Python and Tkinter, it provides comprehensive data validation capabilities including row count comparison, checksum verification, value-level reconciliation, custom validation rules, and automated monitoring with email and Slack alerts.

### 🌟 Key Features

- **📋 Row Count Comparison**: Instant verification of record counts between systems
- **📋 Checksum Validation**: MD5 hash-based data integrity verification
- **📋 Value-Level Reconciliation**: Field-by-field comparison with configurable tolerance
- **📋 Tolerance Configuration**: Precise decimal comparison for financial data
- **📋 Custom Validation Rules**: Build complex business logic validations
- **📋 Scheduled Reconciliation**: Automated hourly, daily, weekly, monthly runs
- **📋 Email/Slack Alerts**: Real-time notifications on discrepancies
- **📋 Discrepancy Reports**: Professional Excel exports with detailed findings
- **🔌 Multi-Database Support**: PostgreSQL, MySQL, SQLite, Oracle, MS SQL
- **⚡ Performance Optimized**: Efficient processing of large datasets

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** with pip
- **pandas** library
- **sqlalchemy** for database connections
- **openpyxl** for Excel export
- **schedule** for automation
- **tkinter** (included with Python)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/data-reconciliation-tool.git
cd data-reconciliation-tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python data_reconciliation_tool.py
```

### 4. Run Your First Validation

1. **Tab 1 - Connections**: Add source and target database connections
2. **Tab 2 - Validation**: Configure source/target queries and validation options
3. **Tab 3 - Review Results**: View comprehensive validation report
4. **Tab 4 - Schedule**: Set up automated reconciliation runs
5. **Export**: Download Excel reports with detailed discrepancies

## 📋 Features In Detail

### 1. Comprehensive Validation Types

**Row Count Validation:**
- Instant count comparison between source and target
- Difference calculation and reporting
- Pass/Fail status with detailed metrics
- Identifies missing or extra records

**Checksum Validation:**
- MD5 hash calculation for entire datasets
- Detects any data modifications
- Ensures complete data integrity
- Fast verification for large tables

**Value-Level Reconciliation:**
- Field-by-field comparison on key columns
- Configurable decimal tolerance (e.g., 0.01 for currency)
- Identifies missing records in source or target
- Highlights value mismatches with before/after
- Shows sample discrepancies (up to 10 records)
- Calculates differences for numeric fields

### 2. Multi-Database Connection Management

**Supported Databases:**
- **SQLite**: Embedded, no server required
- **PostgreSQL**: Enterprise-grade open source
- **MySQL**: Popular web application database
- **Oracle**: Enterprise database system
- **Microsoft SQL Server**: Windows-native database

**Connection Features:**
- Secure credential storage in JSON config
- Connection testing before saving
- Reusable connections across validations
- Easy connection selection via dropdown
- Connection browsing and management

**Connection Configuration:**
- Connection name (friendly identifier)
- Database type selection
- Host and port specification
- Database name
- Username and password (encrypted storage)

### 3. Intelligent Custom Validation Rules

**Rule Types:**

**Column Comparison:**
- Compare two columns for consistency
- Example: `total_amount = quantity × unit_price`
- Configurable tolerance for numeric comparisons

**Null Check:**
- Ensure critical fields are populated
- Example: `email_address NOT NULL`
- Business rule enforcement

**Range Check:**
- Validate numeric values within bounds
- Example: `age >= 0 AND age <= 120`
- Data quality validation

**Pattern Match:**
- Regex-based pattern validation
- Example: `phone_number matches ^\d{3}-\d{3}-\d{4}$`
- Format consistency checking

**Custom Function:**
- Complex multi-field validation logic
- Example: `if status='APPROVED' then approval_date IS NOT NULL`
- Business rule validation

**Rule Configuration:**
- Rule name and description
- Column selection (comma-separated)
- Expression or function definition
- Tolerance specification
- Enable/disable individual rules

### 4. Automated Scheduling System

**Schedule Types:**
- **Hourly**: Every hour at specified minute
- **Daily**: Once per day at specified time
- **Weekly**: Once per week (e.g., Monday 9:00 AM)
- **Monthly**: Once per month (e.g., 1st at 9:00 AM)

**Job Management:**
- Enable/disable jobs without deletion
- Run any job immediately for testing
- View next scheduled run time
- Job status tracking (Active/Inactive)
- Job history and execution logs

**Scheduler Features:**
- Background thread processing
- Non-blocking UI during scheduled runs
- Automatic retry on failures
- Configurable alert recipients
- Multiple concurrent jobs supported

### 5. Multi-Channel Alerting

**Email Alerts (SMTP):**
- Gmail, Outlook, Office 365 support
- Custom SMTP server configuration
- Multiple recipients (comma-separated)
- Rich text email format
- Detailed discrepancy summary
- Attached reports option

**Slack Integration:**
- Webhook-based messaging
- Rich formatted blocks
- Color-coded status indicators
- Direct links to detailed reports
- Channel or DM delivery
- Customizable message templates

**Alert Triggers:**
- Row count mismatches
- Checksum validation failures
- Value-level discrepancies found
- Custom rule violations
- Scheduled validation failures

### 6. Professional Reporting

**Excel Export (.xlsx):**
- Multi-worksheet structure:
  - Summary sheet (overview and metadata)
  - Validation Results (all validation types)
  - Discrepancies Detail (missing records, mismatches)
- Professional formatting:
  - Color-coded headers
  - Bold fonts for emphasis
  - Cell borders and alignment
  - Number formatting
- Sample discrepancy records (up to 10 per type)
- Ready for stakeholder distribution

**Report Contents:**
- Validation timestamp
- Source and target connections
- Validation configuration
- Pass/Fail status for each validation type
- Row count comparison
- Checksum results
- Detailed discrepancies:
  - Missing in target
  - Missing in source
  - Value mismatches with differences
- Quality metrics and statistics

**Report Management:**
- In-memory history during session
- View past validation results
- Export historical reports
- Delete old reports
- Configurable retention period

### 7. Configuration Management

**Validation Configuration:**
- Save current validation setup to JSON
- Load saved configurations
- Reusable validation templates
- Quick setup for recurring validations

**Saved Configuration Includes:**
- Source connection and query
- Target connection and query
- Key columns for reconciliation
- Tolerance settings
- Enabled validation types
- Custom rules to apply

**Application Settings:**
- Email SMTP configuration
- Slack webhook URL
- Default tolerance values
- History retention period
- Performance optimization options

## 📊 Use Cases

### Data Engineers

- **Post-ETL Validation**: Verify data accuracy after pipeline execution
- **Production Monitoring**: Continuous monitoring of critical data flows
- **Migration Verification**: Ensure 100% accuracy during system migrations
- **Pipeline Quality Gates**: Automated validation before promoting data
- **Error Detection**: Early identification of data quality issues
- **Performance Tuning**: Monitor data load consistency over time

### ETL Developers

- **Development Testing**: Validate transformations during development
- **Regression Testing**: Ensure changes don't break existing pipelines
- **Data Transformation Verification**: Confirm business logic correctness
- **Load Balancing**: Verify parallel load processes produce identical results
- **Incremental Load Validation**: Check delta loads match expectations
- **Deployment Verification**: Post-deployment data accuracy checks

### Quality Assurance Teams

- **Compliance Auditing**: Regular audits for SOX, GDPR, HIPAA compliance
- **Data Quality Scorecards**: Track quality metrics over time
- **Production Validation**: Daily checks on critical business data
- **Issue Tracking**: Document and track data discrepancies
- **Quality Reporting**: Generate executive-level quality reports
- **SLA Monitoring**: Ensure data accuracy meets SLAs

### Business Analysts

- **Report Validation**: Verify report data matches source systems
- **Data Warehouse Quality**: Check dimensional model accuracy
- **Dashboard Verification**: Ensure BI dashboards show correct data
- **Stakeholder Confidence**: Provide validation evidence to business
- **Data Lineage**: Trace data from source to target
- **Reconciliation Reports**: Monthly/quarterly reconciliation documentation

## 🔧 Configuration & Best Practices

### Setting Up Database Connections

**PostgreSQL Example:**
```
Connection Name: Production_PostgreSQL
Database Type: postgresql
Host: prod-db.company.com
Port: 5432
Database: data_warehouse
Username: readonly_user
Password: ••••••••••
```

**MySQL Example:**
```
Connection Name: Staging_MySQL
Database Type: mysql
Host: staging-mysql.internal
Port: 3306
Database: etl_staging
Username: etl_validator
Password: ••••••••••
```

**SQLite Example:**
```
Connection Name: Local_Test
Database Type: sqlite
Database: /path/to/local_test.db
(Leave host, port, username, password empty)
```

### Writing Effective Queries

**Best Practice - Use Date Filters:**
```sql
-- Validate today's data only
SELECT * FROM orders 
WHERE order_date = CURRENT_DATE

-- Validate yesterday's data
SELECT * FROM sales 
WHERE sale_date = CURRENT_DATE - INTERVAL '1 day'
```

**Best Practice - Select Specific Columns:**
```sql
-- Instead of SELECT *
SELECT order_id, customer_id, total_amount, status 
FROM orders 
WHERE order_date >= '2024-01-01'
```

**Best Practice - Use Appropriate Indexes:**
```sql
-- Ensure key columns are indexed
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_order_id ON orders(order_id);
```

### Configuring Key Columns

**Single Key Column:**
```
Key Columns: order_id
```

**Composite Key:**
```
Key Columns: customer_id, order_date, product_id
```

**Natural Key:**
```
Key Columns: email_address
```

**Surrogate Key:**
```
Key Columns: record_id
```

### Setting Appropriate Tolerances

**Financial Data (Currency):**
```
Tolerance: 0.01  (penny precision)
Example: $199.99 matches $200.00 within tolerance
```

**Scientific Data:**
```
Tolerance: 0.001  (3 decimal places)
Example: 1.2345 matches 1.2351 within tolerance
```

**Percentage Values:**
```
Tolerance: 0.0001  (2 decimal places)
Example: 12.34% matches 12.35% within tolerance
```

**Integer Values (Exact Match):**
```
Tolerance: 0  (no tolerance)
Example: Only exact matches pass
```

### Scheduling Best Practices

**Daily ETL Validation:**
- Schedule: Daily at 7:00 AM (after 6:00 AM ETL completes)
- Enable email alerts to ETL team
- Validate previous day's data only
- Set up retry on failure

**Hourly Incremental Loads:**
- Schedule: Hourly at :15 (15 minutes after load)
- Enable Slack alerts to #data-ops channel
- Validate last hour's data
- Quick checks: row count + checksum only

**Weekly Comprehensive Check:**
- Schedule: Weekly Monday 6:00 AM
- Enable email alerts to management
- Full value-level reconciliation
- Export detailed Excel report

**Monthly Compliance Audit:**
- Schedule: Monthly 1st at 9:00 AM
- Enable email to compliance team
- Full month's data validation
- Archive reports for 7 years

## 📦 Installation Guide

### Windows Installation

**Step 1: Install Python**
1. Download Python 3.8+ from [python.org](https://python.org)
2. Run installer with "Add Python to PATH" checked
3. Verify: Open Command Prompt, type `python --version`

**Step 2: Install Dependencies**
```bash
pip install pandas sqlalchemy openpyxl schedule requests
```

**Step 3: Install Database Drivers (as needed)**
```bash
# PostgreSQL
pip install psycopg2-binary

# MySQL
pip install pymysql

# MS SQL Server
pip install pyodbc
```

**Step 4: Get Application**
```bash
git clone https://github.com/yourusername/data-reconciliation-tool.git
cd data-reconciliation-tool
```

**Step 5: Run**
```bash
python data_reconciliation_tool.py
```

### macOS Installation

**Step 1: Install Python with tkinter**
```bash
brew install python@3.11
brew install python-tk@3.11
```

**Step 2: Install Dependencies**
```bash
pip3 install pandas sqlalchemy openpyxl schedule requests
```

**Step 3: Install Database Drivers**
```bash
# PostgreSQL
pip3 install psycopg2-binary

# MySQL
pip3 install pymysql
```

**Step 4: Clone and Run**
```bash
git clone https://github.com/yourusername/data-reconciliation-tool.git
cd data-reconciliation-tool
python3 data_reconciliation_tool.py
```

### Linux Installation (Ubuntu/Debian)

**Step 1: Install System Packages**
```bash
sudo apt update
sudo apt install python3 python3-tk python3-pip
```

**Step 2: Install Python Packages**
```bash
pip3 install pandas sqlalchemy openpyxl schedule requests
```

**Step 3: Install Database Drivers**
```bash
# PostgreSQL
pip3 install psycopg2-binary

# MySQL
pip3 install pymysql
```

**Step 4: Clone and Run**
```bash
git clone https://github.com/yourusername/data-reconciliation-tool.git
cd data-reconciliation-tool
python3 data_reconciliation_tool.py
```

### Docker Installation (Optional)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "data_reconciliation_tool.py"]
```

## 🚨 Troubleshooting

### Common Issues & Solutions

**Issue: "Connection failed: No such host is known"**

**Solutions:**
- Verify hostname/IP address is correct
- Check network connectivity with `ping hostname`
- Ensure database server is running
- Verify firewall rules allow connection
- Check if VPN is required and connected

**Issue: "Connection failed: password authentication failed"**

**Solutions:**
- Verify username and password are correct
- Check user has appropriate permissions
- Ensure user has SELECT privileges on tables
- Verify user account is not locked
- Check if IP address is whitelisted

**Issue: "Query execution timeout"**

**Solutions:**
- Add WHERE clause to filter data
- Create indexes on filter columns
- Run during off-peak hours
- Increase query timeout in database settings
- Consider using sampling for large tables

**Issue: "Out of memory error"**

**Solutions:**
- Validate smaller date ranges
- Use sampling: `TABLESAMPLE SYSTEM (10)`
- Select fewer columns in query
- Increase available RAM
- Process data in chunks

**Issue: "Email send failed: Authentication failed"**

**Solutions:**
- Use App Password for Gmail (not regular password)
- Enable "Less secure app access" (not recommended)
- Verify SMTP server and port are correct
- Check email account is not locked
- Test with telnet: `telnet smtp.gmail.com 587`

**Issue: "Slack webhook not working"**

**Solutions:**
- Verify webhook URL is complete and correct
- Test webhook with curl:
  ```bash
  curl -X POST -H 'Content-type: application/json' \
    --data '{"text":"Test message"}' \
    YOUR_WEBHOOK_URL
  ```
- Check workspace permissions
- Ensure webhook is not disabled

**Issue: "Scheduler not running jobs"**

**Solutions:**
- Verify job status is "Active"
- Check system time is correct
- Ensure application stays running
- Review console for error messages
- Verify schedule time format (HH:MM)

## 🔐 Security & Privacy

### Data Security

**Local Processing:**
- All reconciliation done locally
- No data sent to external servers
- Full control over data location and access
- Database credentials stored locally

**Credential Protection:**
- Passwords stored in JSON config file
- File permissions should be restricted (chmod 600)
- Use read-only database accounts when possible
- Consider encrypting config file for sensitive environments

**Network Security:**
- Use SSL/TLS for database connections
- VPN recommended for remote connections
- Restrict database network access
- Use least-privilege database accounts

**Best Practices:**
- Don't commit `recon_config.json` to version control
- Add to `.gitignore`:
  ```
  recon_config.json
  *.db
  *.xlsx
  *.log
  ```
- Rotate database passwords regularly
- Use separate accounts per environment
- Enable database audit logging
- Restrict file permissions on exports

### Compliance Considerations

**SOX Compliance:**
- Maintain validation audit trail
- Archive reports for 7 years
- Document validation procedures
- Track who ran validations and when

**GDPR Compliance:**
- Ensure data accuracy (Article 5)
- Document data quality processes
- Implement data validation controls
- Maintain processing records

**HIPAA Compliance:**
- Validate healthcare data accuracy
- Encrypt exports containing PHI
- Restrict access to validation results
- Maintain audit logs

## 📊 Roadmap

### Current Version (v1.0)

- ✅ Row count comparison
- ✅ Checksum validation (MD5)
- ✅ Value-level reconciliation
- ✅ Configurable tolerance
- ✅ Custom validation rules
- ✅ Scheduled reconciliation
- ✅ Email alerts (SMTP)
- ✅ Slack alerts (webhook)
- ✅ Excel export
- ✅ Multi-database support

### Upcoming Features (v1.1)

- 🔄 Historical trend analysis
- 🔄 Data drift detection
- 🔄 Parallel execution for large datasets
- 🔄 Additional export formats (PDF, CSV)
- 🔄 Validation templates library
- 🔄 Rule execution order control
- 🔄 Batch validation (multiple source-target pairs)
- 🔄 Interactive data viewer for discrepancies

### Future Enhancements (v2.0)

- 📋 REST API for programmatic access
- 📋 Command-line interface (CLI)
- 📋 Web-based dashboard
- 📋 Machine learning anomaly detection
- 📋 Data quality KPI tracking
- 📋 Integration with data catalogs
- 📋 Visual query builder
- 📋 Column mapping recommendations

### Long-term Vision (v3.0)

- 🎯 Cloud database support (Snowflake, Redshift, BigQuery)
- 🎯 Big data integration (Spark, Hadoop)
- 🎯 Real-time streaming validation
- 🎯 Multi-tenancy support
- 🎯 Role-based access control
- 🎯 Integration with Airflow/Prefect
- 🎯 Mobile app for alerts
- 🎯 Advanced analytics and insights

## 📄 License

**Proprietary Demo License**

Copyright (c) 2025 MonteyAI LLC. All rights reserved.

This project is released under a **proprietary demonstration license**. This is a proof-of-concept application intended for educational and demonstration purposes only.

### Quick Summary

✅ **Allowed**: Viewing, learning, educational use, portfolio demonstrations

❌ **Not Allowed**: Commercial use, redistribution, production deployment

⚠️ **No Warranties**: Provided "AS IS" for demonstration purposes only

### 📋 Full License Terms

**Please read the complete license agreement**: [LICENSE](LICENSE)

The full license includes important information about:
- Permitted uses and restrictions
- Disclaimer of warranties
- Limitation of liability
- Demo/proof-of-concept status
- Commercial licensing options

### 💼 Commercial Licensing

Interested in using this for production or commercial purposes?

📧 **Contact**: smontecinos@monteyai.com

🌐 **Website**: https://monteyai.com

🏢 **Company**: MonteyAI LLC

---

**By using this software, you agree to the terms in the [LICENSE](LICENSE) file.**

---

<div align="center">

<img width="468" alt="MonteyAI ETL Tools" src="https://github.com/user-attachments/assets/6b8cb8a2-a4b9-4dfe-9287-14693c2a6380" />

</div>

## 🙏 Acknowledgments

- **Pandas Development Team**: For the powerful data analysis library
- **SQLAlchemy Team**: For the excellent database abstraction layer
- **Python Community**: For comprehensive data tools and libraries
- **Tkinter Developers**: For the cross-platform GUI framework
- **Schedule Library**: For elegant job scheduling
- **Data Engineering Community**: For feedback and inspiration

## 🔗 Related Projects

Part of the **MonteyAI ETL Tools Suite**:

- **[Source-to-Target Mapping Generator](https://github.com/sergiomontey/Source-to-Target-Mapping-Documentation-Generator)** - Document ETL mappings professionally
- **[CSV to Database Uploader](https://github.com/yourusername/csv-database-uploader)** - Load CSV data into databases
- **[Database Creator & Manager](https://github.com/yourusername/database-creator-manager)** - Visual database and table creation
- **[Data Profiler Application](https://github.com/yourusername/data-profiler-application)** - Comprehensive data quality analysis
- **Data Validation & Reconciliation Tool** - This tool

### Recommended Workflow

1. **Profile Source Data** → Use Data Profiler Application
2. **Design Target Schema** → Use Database Creator & Manager
3. **Load Data** → Use CSV to Database Uploader
4. **Validate ETL Results** → Use Data Validation & Reconciliation Tool (this tool)
5. **Document Mappings** → Use Source-to-Target Mapping Generator
6. **Monitor Production** → Schedule recurring validations with this tool

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with 💻 by MonteyAI for data professionals worldwide

[Report Bug](https://github.com/yourusername/data-reconciliation-tool/issues) · [Request Feature](https://github.com/yourusername/data-reconciliation-tool/issues) · [Documentation](https://github.com/yourusername/data-reconciliation-tool/wiki)

</div>
