==========================
Powerofficego to  Dataflow
==========================

Generated: 2024-08-28 08:12:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to  Customers company
---------------------------------------------
Every Powerofficego Customers will be synchronized with a  Customers company.

Once a link between a Powerofficego Customers and a  Customers company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Customers company:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Customers company Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Customers person to  Customers person
---------------------------------------------------
Every Powerofficego Customers person will be synchronized with a  Customers person.

Once a link between a Powerofficego Customers person and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Customers person Property
     -  Data Type
   * - Id
     - id
     - "string"
   * - MailAddress.AddressLine1
     - address1
     - "string"
   * - MailAddress.AddressLine2
     - address2
     - "string"
   * - MailAddress.City
     - city
     - "string"
   * - MailAddress.CountryCode
     - country
     - "string"
   * - MailAddress.ZipCode
     - postal_code
     - "string"


Powerofficego Salesorders to  Invoices
--------------------------------------
Every Powerofficego Salesorders will be synchronized with a  Invoices.

Once a link between a Powerofficego Salesorders and a  Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a  Invoices:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     -  Invoices Property
     -  Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - CustomerId
     - customer
     - "string"
   * - CustomerReferenceContactPersonId
     - customer
     - "string"

