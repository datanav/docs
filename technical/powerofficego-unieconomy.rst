=====================================
PowerOffice GO to Unieconomy Dataflow
=====================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Employees to Unieconomy Countries
------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Employees and a Unieconomy Countries must be established.

A PowerOffice GO Employees will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Unieconomy Countries Property
   * - MailAddress.CountryCode
     - CountryCode

Once a link between a PowerOffice GO Employees and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Employees and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Employees Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


PowerOffice GO Contactperson to Unieconomy Countries
----------------------------------------------------
Every PowerOffice GO Contactperson will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Contactperson will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Contactperson will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Unieconomy Countries Property
   * - residenceCountryCode
     - CountryCode

Once a link between a PowerOffice GO Contactperson and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


PowerOffice GO Currency to Unieconomy Currencycodes
---------------------------------------------------
Every PowerOffice GO Currency will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the PowerOffice GO Currency will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A PowerOffice GO Currency will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Unieconomy Currencycodes Property
   * - code
     - Code

Once a link between a PowerOffice GO Currency and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Currency and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Currency Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


PowerOffice GO Customers to Unieconomy Countries
------------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Customers will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Customers will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Unieconomy Countries Property
   * - MailAddress.CountryCode
     - CountryCode

Once a link between a PowerOffice GO Customers and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


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


PowerOffice GO Location to Unieconomy Countries
-----------------------------------------------
Every PowerOffice GO Location will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Location will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Location will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Location Property
     - Unieconomy Countries Property
   * - countryCode
     - CountryCode

Once a link between a PowerOffice GO Location and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Location and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Location Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


PowerOffice GO Outgoinginvoices to Unieconomy Countries
-------------------------------------------------------
Every PowerOffice GO Outgoinginvoices will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Outgoinginvoices will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Outgoinginvoices will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Outgoinginvoices Property
     - Unieconomy Countries Property
   * - DeliveryAddressCountryCode
     - CountryCode

Once a link between a PowerOffice GO Outgoinginvoices and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Outgoinginvoices and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Outgoinginvoices Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


PowerOffice GO Suppliers person to Unieconomy Countries
-------------------------------------------------------
Every PowerOffice GO Suppliers person will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Suppliers person will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Suppliers person will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Unieconomy Countries Property
   * - MailAddress.CountryCode
     - CountryCode

Once a link between a PowerOffice GO Suppliers person and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers person and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers person Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


PowerOffice GO Suppliers to Unieconomy Countries
------------------------------------------------
Every PowerOffice GO Suppliers will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the PowerOffice GO Suppliers will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A PowerOffice GO Suppliers will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
     - Unieconomy Countries Property
   * - MailAddress.CountryCode
     - CountryCode

Once a link between a PowerOffice GO Suppliers and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Suppliers and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Suppliers Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

