=====================================
PowerOffice GO to Unieconomy Dataflow
=====================================

Generated: 2024-09-11 11:38:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Customers to Unieconomy Customers
-----------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a Unieconomy Customers.

Once a link between a PowerOfficeGO Customers and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
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


PowerOfficeGO Departments to Unieconomy Departments
---------------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a Unieconomy Departments.

Once a link between a PowerOfficeGO Departments and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - Name
     - Name
     - "string"

