===================================
Invoiced to PowerOffice GO Dataflow
===================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to PowerOffice GO Contactperson
-------------------------------------------------
Every Invoiced Contacts will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Invoiced Contacts and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


Invoiced Customers company to PowerOffice GO Customers
------------------------------------------------------
Every Invoiced Customers company will be synchronized with a PowerOffice GO Customers.

Once a link between a Invoiced Customers company and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - name
     - Name
     - "string"


Invoiced Customers person to PowerOffice GO Customers person
------------------------------------------------------------
Every Invoiced Customers person will be synchronized with a PowerOffice GO Customers person.

Once a link between a Invoiced Customers person and a PowerOffice GO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a PowerOffice GO Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - PowerOffice GO Customers person Property
     - PowerOffice GO Data Type
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


Invoiced Invoices to PowerOffice GO Salesorders
-----------------------------------------------
Every Invoiced Invoices will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Invoiced Invoices and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer
     - CustomerId
     - "integer"
   * - customer
     - CustomerReferenceContactPersonId
     - "integer"


Invoiced Items to PowerOffice GO Product
----------------------------------------
Every Invoiced Items will be synchronized with a PowerOffice GO Product.

Once a link between a Invoiced Items and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costPrice
     - N/A


Invoiced Lineitem to PowerOffice GO Salesorderlines
---------------------------------------------------
Every Invoiced Lineitem will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Invoiced Lineitem and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
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

