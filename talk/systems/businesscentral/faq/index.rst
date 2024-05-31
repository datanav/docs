Business Central FAQ
====================


Is the data synchronization real-time?
---------------------------------------
The synchronization latency depends on the APIs of the connected systems, the availability of webhooks, and the specific data type. While changes often propagate within seconds or minutes, Talk does not guarantee real-time updates. The focus is on ensuring data consistency across systems.

Can Talk handle custom properties in Business Central?
-------------------------------------------------------
No, Talk only synchronizes the core standard metadata about each object. Custom properties are currently not supported by Talk.

How does Talk handle data merging to avoid duplicates?
-------------------------------------------------------
Talk uses merge criteria to connect data across systems before synchronization. For organizations, the merge criteria are the company email address and/or Norwegian organizational number. For contacts, the merge criteria is the email address. This helps minimize the risk of duplicate data creation.

Who is responsible for keeping the connectors up-to-date?
----------------------------------------------------------
Sesam, the provider of the Talk service, is responsible for maintaining and updating the connectors. As system APIs evolve, Sesam will increase the support of connectors accordingly.

In what way does Talk support synchronization of Contact Person data to/from Business Central?
-----------------------------------------------------------------------------------------------
The Talk Business Central connector supports the synchronization of Contact Persons data from Business Central to other systems. However, due to limitations in the Business Central API, it is not possible to sync Contact Person data originating in other systems into Business Central.
