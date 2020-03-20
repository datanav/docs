
===============
Online Analytical Processing - OLAP
==============

If you are looking for tools to get insights in your data from visualizations and analysis, you soon run across the term "Online Analytical Processing - OLAP". The context is usually Business intelligence (BI) - the strategies and technologies used by enterprises for the data analysis of business information. BI technologies provide historical, current, and predictive views of business operations.

The tools often relay on specific data structures and storage systems to do their job. Usually in the form of a Data warehouse.

To use these tools to visualize and analysis data from a Sesam node, you need to make the data available to the tool. How to best do this depends on the tool. Saving the data to SQL server is usually a good strategy. Both Sesam and the reporting tools have good connectors for SQL Databases. It is relatively easy to migrate traditional SQL databases to systems that still support SQL, but more data. If you don't have HUGE data sets you need to analyse now, this is a safe and affordable path.

Sesam -> Data store (OLAP server) -> OLAP Client

Example of Reporting tools
================

    * Microsoft Power BI
    * IBM Cognos
    * Apache Superset
    * Tablea 

Examples of data stores with focus on Power BI
=================

Power BI API - micro service in sesam-community
------------------
    PRO: You only need a Power BI Pro licence and office 365 in addition to Sesam. 
    CON: A bit tricky to set up and many limitations.

SQL Database - sesam connector 
------------------
    PRO: Relatively easy to set up. Works well with Power BI and other reporting tools. Affordable. Handles relatively large datasets.
    CON: You need to set up a tabular schema for your data in Sesam. You can use a simple generic schema and insert json in the table, but than this must be handled in reporting tool. The database has an upper limit on how much data it can store. 

Azure SQL - sesam connector
------------------
    PRO: 
    CON:

Azure SQL Data warehouse (now Azure Synapsis Analytics) - sesam connector 
------------------
    PRO:
    CON:

Azure Power BI Dataflow and Power BI desktop - sesam http endpoint
--------------------
    PRO:
    CON:

Druid
----------------
    PRO:
    CON:
