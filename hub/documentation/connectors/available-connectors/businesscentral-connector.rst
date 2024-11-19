.. _businesscentral_connector:

================
Business Central
================

Business Central is an enterprise resource planning (ERP) solution aimed at small to medium-sized businesses (SMBs) developed by Microsoft.
  
The Business Central connector configuration can be found in the  `businesscentral-connector github repository <https://github.com/sesam-io/businesscentral-connector>`_. The `playground branch <https://github.com/sesam-io/businesscentral-connector/tree/playground>`_ is typically the most complete branch.
  
  
Frequently Asked Questions
==========================

Is the data synchronization real-time?
---------------------------------------
The synchronization latency depends on the APIs of the connected systems, the availability of webhooks, and the specific data type. While changes often propagate within seconds or minutes, Sesam does not guarantee real-time updates. The focus is on ensuring data consistency across systems.

How does Sesam handle data merging to avoid duplicates?
-------------------------------------------------------
Sesam uses merge criteria to connect data across systems before synchronization. For organizations, the merge criteria are often the company email address and/or Norwegian organizational number. For contacts, the merge criteria is often the email address. This helps minimize the risk of duplicate data creation.