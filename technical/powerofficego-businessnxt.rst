==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-26 15:45:37

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Company
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Company.

Once a link between a Powerofficego Customers and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Company Property
     -  Data Type
   * - Name
     - name
     - "string"
   * - Number
     - companyBusinessNo (Dependant on having wd:Q852835 in countryIsoCode)
     - "string"
   * - OrganizationNumber
     - companyBusinessNo (Dependant on having  in countryIsoCode)
     - "string"


Powerofficego Departments to  Company
-------------------------------------
Every Powerofficego Departments will be synchronized with a  Company.

Once a link between a Powerofficego Departments and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Company Property
     -  Data Type
   * - Code
     - companyBusinessNo (Dependant on having wd:Q2366457 in countryIsoCode)
     - "string"
   * - Name
     - name
     - "string"


Powerofficego Contactperson to  Country
---------------------------------------
Every Powerofficego Contactperson will be synchronized with a  Country.

Once a link between a Powerofficego Contactperson and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Country Property
     -  Data Type
   * - residenceCountryCode
     - isoCode
     - "string"


Powerofficego Currency to  Currency
-----------------------------------
Every Powerofficego Currency will be synchronized with a  Currency.

Once a link between a Powerofficego Currency and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a  Currency:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     -  Currency Property
     -  Data Type


Powerofficego Customers to  Country
-----------------------------------
Every Powerofficego Customers will be synchronized with a  Country.

Once a link between a Powerofficego Customers and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Country Property
     -  Data Type
   * - MailAddress.CountryCode
     - isoCode
     - "string"


Powerofficego Location to  Country
----------------------------------
Every Powerofficego Location will be synchronized with a  Country.

Once a link between a Powerofficego Location and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Location and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Location Property
     -  Country Property
     -  Data Type


Powerofficego Outgoinginvoices to  Country
------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a  Country.

Once a link between a Powerofficego Outgoinginvoices and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     -  Country Property
     -  Data Type


Powerofficego Suppliers to  Country
-----------------------------------
Every Powerofficego Suppliers will be synchronized with a  Country.

Once a link between a Powerofficego Suppliers and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers Property
     -  Country Property
     -  Data Type


Powerofficego Suppliers person to  Country
------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a  Country.

Once a link between a Powerofficego Suppliers person and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a  Country:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     -  Country Property
     -  Data Type

