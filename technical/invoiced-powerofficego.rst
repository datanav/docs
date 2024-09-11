===================================
Invoiced to PowerOffice GO Dataflow
===================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to PowerOffice Contactperson
----------------------------------------------
Every Invoiced Contacts will be synchronized with a PowerOffice Contactperson.

Once a link between a Invoiced Contacts and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - address1
     - address1
     - "string"
   * - address2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - email
     - emailAddress
     - "string"
   * - postal_code
     - zipCode
     - "string"


Invoiced Customers company to PowerOffice Customers
---------------------------------------------------
Every Invoiced Customers company will be synchronized with a PowerOffice Customers.

Once a link between a Invoiced Customers company and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
   * - name
     - Name
     - "string"


Invoiced Customers person to PowerOffice Customers person
---------------------------------------------------------
Every Invoiced Customers person will be synchronized with a PowerOffice Customers person.

Once a link between a Invoiced Customers person and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Invoiced Invoices to PowerOffice Salesorders
--------------------------------------------
Every Invoiced Invoices will be synchronized with a PowerOffice Salesorders.

Once a link between a Invoiced Invoices and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer
     - CustomerId
     - "integer"
   * - customer
     - CustomerReferenceContactPersonId
     - "integer"


Invoiced Items to PowerOffice Product
-------------------------------------
Every Invoiced Items will be synchronized with a PowerOffice Product.

Once a link between a Invoiced Items and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costPrice
     - N/A


Invoiced Lineitem to PowerOffice Salesorderlines
------------------------------------------------
Every Invoiced Lineitem will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Invoiced Lineitem and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
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

