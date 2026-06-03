 Mutual Fund Analytics

 Overview

This project was completed as part of the Bluestock Data Analytics Internship.

The project focuses on mutual fund data ingestion, cleaning, validation, SQLite database design, and analytical querying.

Day 1 Deliverables

* Project setup
* Python environment configuration
* NAV data extraction
* Data ingestion scripts
* Data quality validation
* GitHub repository setup

Day 2 Deliverables

Data Cleaning

* Cleaned NAV history data
* Cleaned investor transactions data
* Cleaned scheme performance data
* Generated 10 cleaned datasets

Database Design

* Designed SQLite star schema
* Created dimension and fact tables:

  * dim_fund
  * dim_date
  * fact_nav
  * fact_transactions
  * fact_performance
  * fact_aum

Data Loading

* Loaded cleaned datasets into SQLite using SQLAlchemy
* Verified row counts between source CSVs and database tables

SQL Analytics

* Created 10 analytical SQL queries
* Fund performance analysis
* AUM analysis
* Transaction analysis
* NAV trend analysis

Deliverables

* data/processed/
* bluestock_mf.db
* schema.sql
* queries.sql
* data_dictionary.md

Technologies Used

* Python
* Pandas
* SQLite
* SQLAlchemy
* SQL
* Git
* GitHub
