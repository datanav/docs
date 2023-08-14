====================================
Powerofficego to UniEconomy Dataflow
====================================

Generated: 2023-08-14 09:02:09

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customer to UniEconomy Customers
----------------------------------------------
Every Powerofficego Customer will be synchronized with a UniEconomy Customers.

Once a link between a Powerofficego Customer and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customer and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customer Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - InternationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - WebsiteUrl
     - WebUrl
     - "string"
   * - internationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - vatNumber (Dependant on having wd:Q11994066 in mailAddress.countryCodeDependant on having wd:Q11994066 in streetAddresses.countryCode)
     - OrgNumber
     - "string"
   * - websiteUrl
     - WebUrl
     - "string"


Powerofficego Customers to UniEconomy Customers
-----------------------------------------------
Every Powerofficego Customers will be synchronized with a UniEconomy Customers.

Once a link between a Powerofficego Customers and a UniEconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a UniEconomy Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - UniEconomy Customers Property
     - UniEconomy Data Type
   * - internationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - vatNumber (Dependant on having wd:Q11994066 in mailAddress.countryCode)
     - OrgNumber
     - "string"
   * - websiteUrl
     - WebUrl
     - "string"

