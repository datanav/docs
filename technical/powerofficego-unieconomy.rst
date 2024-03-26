====================================
Powerofficego to Unieconomy Dataflow
====================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Customers
-------------------------------------
Every Powerofficego Customers will be synchronized with a  Customers.

Once a link between a Powerofficego Customers and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customers:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customers Property
     -  Data Type
   * - OrganizationNumber (Dependant on having wd:Q11994066 in MailAddress.CountryCodeDependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCodeDependant on having wd:Q11994066 in MailAddress.countryCode)
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


Powerofficego Departments to  Departments
-----------------------------------------
Every Powerofficego Departments will be synchronized with a  Departments.

Once a link between a Powerofficego Departments and a  Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Departments:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Departments Property
     -  Data Type
   * - Name
     - Name
     - "string"

