====================================
Powerofficego to UniEconomy Dataflow
====================================

Generated: 2023-08-18 13:02:10

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to UniEconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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
   * - OrganizationNumber (Dependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCode)
     - OrgNumber
     - "string"
   * - WebsiteUrl
     - WebUrl
     - "string"
   * - internationalIdNumber (Dependant on having wd:Q11994066 in poweroffice-customer:InternationalIdTypeDependant on having wd:Q11994066 in poweroffice-customer:InternationalIdType)
     - OrgNumber
     - "string"
   * - vatNumber (Dependant on having wd:Q11994066 in mailAddress.countryCodeDependant on having wd:Q11994066 in mailAddress.countryCode)
     - OrgNumber
     - "string"
   * - websiteUrl
     - WebUrl
     - "string"


Powerofficego Departments to UniEconomy Departments
---------------------------------------------------
Every Powerofficego Departments will be synchronized with a UniEconomy Departments.

Once a link between a Powerofficego Departments and a UniEconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a UniEconomy Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - UniEconomy Departments Property
     - UniEconomy Data Type
   * - Name
     - Name
     - "string"

