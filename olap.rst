.. _data-analysis:

==================
Data analysis and visualization of data from Sesam
==================


Online Analytical Processing - OLAP
==============

If you are looking for tools to get insights in your data from visualizations and analysis, you soon run across the term "Online Analytical Processing - OLAP". The context is usually Business intelligence (BI) - the strategies and technologies used by enterprises for the data analysis of business information. BI technologies provide historical, current, and predictive views of business operations.

The tools often rely on specific data structures and storage systems to do their job. Usually in the form of a Data warehouse/OLAP server.

To use these tools to visualize and analysis data from a Sesam node, you need to make the data available to the tool. How to best do this depends on the tool. Saving the data to SQL server is usually a good strategy. Both Sesam and the reporting tools have good connectors for SQL Databases. It is relatively easy to migrate traditional SQL databases to systems that still support SQL, but handle more data. If you don't have HUGE data sets you need to analyse now, this is a safe and affordable path. Flattening (un-nested and not hierarchical) the JSON in Sesam can make it easier to ingest and analyse the data.

Sesam -> Data store (OLAP server) -> OLAP Client

Examples of Reporting tools
================
This is not a complete list, but a little selection. Some are the reporting end of general BI systems and supporting IT architecture. Others are more general tools or visualization orientated.

* `Microsoft Power BI <https://powerbi.microsoft.com/en-us/>`_
* `IBM Cognos analytics <https://www.ibm.com/no-en/products/cognos-analytics>`_
* `Apache Superset <https://superset.apache.org/>`_
* `Tableau <https://www.tableau.com/>`_
* `Microsoft Excel <https://www.microsoft.com/en-us/download/details.aspx?id=39379&CorrelationId=173567af-a2fc-49c9-a413-1be96c50c4e0>`_/`Power query <https://docs.microsoft.com/en-us/power-query/>`_ 
* Python/`Jupyter <https://jupyter.org/>`_/Plotly/`Dash <https://dash.plotly.com/introduction>`_
* R/`R studio <https://rstudio.com/>`_ /`Shiny <https://rstudio.com/products/shiny/shiny-server/>`_

Examples of data stores with focus on Power BI/Power query
=================
For many the Microsoft tools will be the most accessible and familiar. The Power query is used in many of the products and give a uniform way to connect to data and build data models. Power Query m code can be copied and used across products. Examples of products that use Power query: Power BI, Excel, Power BI dataflow, Azure Data Factory.

SQL Database - sesam connector 
------------------
Use standard Sesam SQL connectors. The SQL database can be on a cloud service or on premises but must be reachable from Sesam and reporting tool. 
https://docs.sesam.io/configuration.html#the-sql-systems

PRO: Relatively easy to set up. Works well with Power BI and other reporting tools. Affordable. Handles relatively large datasets. Works well with Microsoft Power query.

CON: You need to set up a tabular schema for your data in Sesam. You can use a simple generic schema and insert json in the table, but than this must be handled in reporting tool [1]. The database has an upper limit on how much data it can store. 

Azure SQL - sesam connector
------------------
For Power BI, a "Azure SQL" database is a good choice. You can have relatively large data bases. Max size depends on which service tier you have. You can provision more than one Azure SQL database and connect them as a data model in Power BI. From Sesam you use the Sesam "microsoft azure sql data warehouse" connector to connect.
https://docs.sesam.io/configuration.html#the-microsoft-azure-sql-data-warehouse-system

PRO: As for general SQL database but support more data

CON: As for general SQL database,

Azure SQL Data warehouse (now Azure Synapsis Analytics) - sesam connector 
------------------
This is a specialized service for high performance data warehouse and analysis.

PRO Can handle more data and supports fast analysis

CON: Have stricter restrictions on data types. Particular max length of nvarcar (text string). This can be a problem with large json blobs in table cells. Relative expensive.

Azure Power Power BI/Power query - sesam http endpoint
--------------------
You can use a sesam http endpoint as a data source in a Power query. This is NOT a good practice for sensitive data! In practice this is only a good choice if the endpoint only have relatively little data since it will be read in its entirety or you will have to implement "since" (sesam) logic in Power query. Remember to filter "_deleted" entities in Sesam if you don't want them to be part of the data sent. You must use an anonymous Web connection in Power query (from Web in Data tab in Excel) and a shareable link from Sesam http endpoint output.

PRO: Very direct and simple import. Can be combined with other data sources in a Power query data model. Can be done with only Sesam and Excel. 

CON: Only a full read in practice. Keys in files, danger off sharing keys by mistake if you share eg. Power BI file or Excel file. 

Power BI API - micro service in sesam-community
------------------
This micro service use the Power BI API to make a Sesam sink that write data directly to a Power BI push dataset.

PRO You only need a Power BI Pro licence and office 365 in addition to Sesam. 

CON: A bit tricky to set up and many limitations. You can only build reports with data from the Power BI dataset, you can not use Power query to build a data model and drill through different data sets.

Druid
----------------
"Apache Druid is a real-time analytics database designed for fast slice-and-dice analytics ("OLAP" queries) on large data sets". 
https://druid.apache.org/docs/latest/design/index.html
You can load data into Druid from a Sesam http-endpoint. You can use a standard Druid HTTP(s) data loader. 
https://github.com/sesam-community/druid

PRO: Druid works good with event/time-oriented data.

CON: Druid HTTP(s) data loader will only ingest flat JSON data, so you need to flatten the data in Sesam. 

JSON in SQL table
==================
Power query supports turning JSON in a table cell into columns and values. This works well for a JSON schema where all key values are used and set to some value. The process is simple, but requires many mouse clicks for a highly nested model. For sparse and dynamic JSON data, this does not work that well and will need frequent manual tuning. With some clever Power query m code, you can probably make this more dynamic. If the JSON data is flattened in Sesam this process is much simpler.

IBM Cognos also support similar JSON parsing of cells.

Metadata from Sesam API
========================
