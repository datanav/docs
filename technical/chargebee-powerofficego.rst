====================================
Chargebee to PowerOffice GO Dataflow
====================================

Generated: 2024-10-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Address to PowerOffice GO Customers
---------------------------------------------
Every Chargebee Address will be synchronized with a PowerOffice GO Customers.

Once a link between a Chargebee Address and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - addr
     - MailAddress.AddressLine1
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - subscription_id
     - Id
     - "integer"
   * - zip
     - MailAddress.ZipCode
     - "string"


Chargebee Address to PowerOffice GO Customers (human data)
----------------------------------------------------------
Every Chargebee Address will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Chargebee Address and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type
   * - addr
     - MailAddress.AddressLine1
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - subscription_id
     - Id
     - "integer"
   * - zip
     - MailAddress.ZipCode
     - "string"


Chargebee Customer to PowerOffice GO Customers
----------------------------------------------
Every Chargebee Customer will be synchronized with a PowerOffice GO Customers.

Once a link between a Chargebee Customer and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type


Chargebee Customer to PowerOffice GO Customers (human data)
-----------------------------------------------------------
Every Chargebee Customer will be synchronized with a PowerOffice GO Customers (human data).

Once a link between a Chargebee Customer and a PowerOffice GO Customers (human data) is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a PowerOffice GO Customers (human data):

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - PowerOffice GO Customers (human data) Property
     - PowerOffice GO Data Type
   * - email
     - EmailAddress
     - "string"
   * - first_name
     - FirstName
     - "string"
   * - last_name
     - LastName
     - "string"


Chargebee Item to PowerOffice GO Product
----------------------------------------
Every Chargebee Item will be synchronized with a PowerOffice GO Product.

Once a link between a Chargebee Item and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type


Chargebee Order to PowerOffice GO Salesorders
---------------------------------------------
Every Chargebee Order will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Chargebee Order and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - currency_code
     - CurrencyCode
     - "string"
   * - customer_id
     - CustomerId
     - "integer"
   * - customer_id
     - CustomerReferenceContactPersonId
     - "integer"

