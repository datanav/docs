==================================
Invoiced to Powerofficego Dataflow
==================================

Generated: 2024-09-09 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Powerofficego. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to Powerofficego Contactperson
------------------------------------------------
Every Invoiced Contacts will be synchronized with a Powerofficego Contactperson.

Once a link between a Invoiced Contacts and a Powerofficego Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a Powerofficego Contactperson:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - Powerofficego Contactperson Property
     - Powerofficego Data Type
   * - address1
     - address1
     - "string"
   * - address2
     - address2
     - "string"
   * - city
     - city
     - "string"


Invoiced Customers company to Powerofficego Customers
-----------------------------------------------------
Every Invoiced Customers company will be synchronized with a Powerofficego Customers.

Once a link between a Invoiced Customers company and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - name
     - Name
     - "string"


Invoiced Customers person to Powerofficego Customers person
-----------------------------------------------------------
Every Invoiced Customers person will be synchronized with a Powerofficego Customers person.

Once a link between a Invoiced Customers person and a Powerofficego Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Powerofficego Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Powerofficego Customers person Property
     - Powerofficego Data Type
   * - address1
     - MailAddress.AddressLine1
     - "string"
   * - address2
     - MailAddress.AddressLine2
     - "string"
   * - city
     - MailAddress.City
     - "string"
   * - country
     - MailAddress.CountryCode
     - "string"
   * - id
     - Id
     - "integer"
   * - postal_code
     - MailAddress.ZipCode
     - "string"


Invoiced Invoices to Powerofficego Salesorders
----------------------------------------------
Every Invoiced Invoices will be synchronized with a Powerofficego Salesorders.

Once a link between a Invoiced Invoices and a Powerofficego Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a Powerofficego Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - Powerofficego Salesorders Property
     - Powerofficego Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer
     - CustomerId
     - "integer"
   * - customer
     - CustomerReferenceContactPersonId
     - "integer"


Invoiced Items to Powerofficego Product
---------------------------------------
Every Invoiced Items will be synchronized with a Powerofficego Product.

Once a link between a Invoiced Items and a Powerofficego Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Powerofficego Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Powerofficego Product Property
     - Powerofficego Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costPrice
     - N/A


Invoiced Lineitem to Powerofficego Salesorderlines
--------------------------------------------------
Every Invoiced Lineitem will be synchronized with a Powerofficego Salesorderlines.

Once a link between a Invoiced Lineitem and a Powerofficego Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Powerofficego Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Powerofficego Salesorderlines Property
     - Powerofficego Data Type
   * - $original_id
     - sesam_SalesOrderId
     - "string"
   * - items.amount
     - ProductUnitPrice
     - N/A
   * - items.discounts
     - Allowance
     - "float"
   * - items.name
     - Description
     - "string"
   * - items.quantity
     - Quantity
     - N/A

