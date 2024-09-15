=====================================
PowerOffice GO to Unieconomy Dataflow
=====================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Customers to Unieconomy Customers
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Unieconomy Customers.

Once a link between a PowerOffice GO Customers and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
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


PowerOffice GO Departments to Unieconomy Departments
----------------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Unieconomy Departments.

Once a link between a PowerOffice GO Departments and a Unieconomy Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Unieconomy Departments:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Unieconomy Departments Property
     - Unieconomy Data Type
   * - Name
     - Name
     - "string"

