
===============
Online Analytical Processing - OLAP
==============

If you are looking for tools to get insights in your data from visualizations and analysis, you soon run across the term "Online Analytical Processing - OLAP". The context is usually Business intelligence (BI) - the strategies and technologies used by enterprises for the data analysis of business information. BI technologies provide historical, current, and predictive views of business operations.

The tools often relay on specific data structures and storage systems to do their job. Usually in the form of a Data warehouse.

To use these tools to visualize and analysis data from a Sesam node, you need to make the data available to the tool. How to best do this depends on the tool. Saving the data to SQL server is usually a good strategy. Both Sesam and the reporting tools have good connectors for SQL Databases. It is relatively easy to migrate traditional SQL databases to systems that still support SQL, but handle more data. If you don't have HUGE data sets you need to analyse now, this is a safe and affordable path.

Sesam -> Data store (OLAP server) -> OLAP Client

Examples of Reporting tools
================

    * Microsoft Power BI
    * IBM Cognos
    * Apache Superset
    * Tablea
    * Microsoft Excel 
    * Python/Jupyter
    * R/R studio/Shiny

Examples of data stores with focus on Power BI/Power query
=================
For many the Microsoft tools will be the most accessible and familiar. The Power query editor is used in many of the products and give a uniform way to connect to data and build data models. Power Query m code can be copied and used across products. Examples of products that use Power query editor: Power BI, Excel, Power BI dataflow, Azure Data Factory.

SQL Database - sesam connector 
------------------
Use standard Sesam SQL connectors. The SQL database can be on a cloud service or on premises but must be reachable from Sesam and reporting tool. 
https://docs.sesam.io/configuration.html#the-sql-systems
    PRO: Relatively easy to set up. Works well with Power BI and other reporting tools. Affordable. Handles relatively large datasets. Works well with Microsoft Power query.
    CON: You need to set up a tabular schema for your data in Sesam. You can use a simple generic schema and insert json in the table, but than this must be handled in reporting tool [1]. The database has an upper limit on how much data it can store. 

Azure SQL - sesam connector
------------------
For Power BI, a "Azure SQL" database is a good choice. You can have relativ large data bases. Max size depends on wich service tier you have. You can provision more than one Azure SQL database and connect them as a data model in Power BI. From Sesam you use the Sesam "microsoft azure sql data warehouse" connector to connect.
https://docs.sesam.io/configuration.html#the-microsoft-azure-sql-data-warehouse-system
    PRO: As for general SQL database but support more data
    CON: As for general SQL database,

Azure SQL Data warehouse (now Azure Synapsis Analytics) - sesam connector 
------------------
This is a specialized service for high performance data warehouse and analysis.
    PRO: Can handle more data and supports fast analysis
    CON: Have stricter restrictions on data types. Particular max length of nvarcar (text string). This can be a problem with large json blobs in table cells. Relative expensive.

Azure Power Power BI/Power query - sesam http endpoint
--------------------
You can use a sesam http endpoint as a data source in a Power query. In practice this is only a good choice if the endpoint only have relatively little data since it will be read in its entirety or you will have to implement "since" (sesam) logic in Power query. 
    PRO: Very direct and simple import. Can be combined with other data sources in a Power query data model. Can be done with only Sesam and Excel. 
    CON: Only a full read in practice. Keys in files, danger off sharing keys by mistake if you share eg. Power BI file or Excel file. 

Power BI API - micro service in sesam-community
------------------
This micro service use the Power BI API to make a Sesam sink that write data directly to a Power BI push dataset.
    PRO: You only need a Power BI Pro licence and office 365 in addition to Sesam. 
    CON: A bit tricky to set up and many limitations. You can only build reports with data from the Power BI dataset, you can not use Power query to build a data model and drill through different data sets.

Druid
----------------

    PRO:
    CON:

JSON in SQL table
==================
Power query supports turning JSON in a table cell into columns and values. This works well for a JSON schema where all key values are used and set to some value. The process is simple, but requires many mouse clicks for a highly nested model. For sparse and dynamic JSON data, this does not work that well and will need frequent manual tuning. With some clever Power query m code, you can probably make this more dynamic. 

IBM Cognos also support similar JSON parsing of cells.