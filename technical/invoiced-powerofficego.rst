==================================
Invoiced to PowerOfficeGO Dataflow
==================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Contacts to PowerOfficeGO Contactperson
------------------------------------------------
Every Invoiced Contacts will be synchronized with a PowerOfficeGO Contactperson.

Once a link between a Invoiced Contacts and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Contacts and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Invoiced Contacts Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


Invoiced Customers company to PowerOfficeGO Customers
-----------------------------------------------------
Every Invoiced Customers company will be synchronized with a PowerOfficeGO Customers.

Once a link between a Invoiced Customers company and a PowerOfficeGO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a PowerOfficeGO Customers:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - PowerOfficeGO Customers Property
     - PowerOfficeGO Data Type
   * - name
     - Name
     - "string"


Invoiced Customers person to PowerOfficeGO Customers person
-----------------------------------------------------------
Every Invoiced Customers person will be synchronized with a PowerOfficeGO Customers person.

Once a link between a Invoiced Customers person and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Invoiced Invoices to PowerOfficeGO Salesorders
----------------------------------------------
Every Invoiced Invoices will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a Invoiced Invoices and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Invoices and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - Invoiced Invoices Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - customer
     - CustomerId
     - "integer"
   * - customer
     - CustomerReferenceContactPersonId
     - "integer"


Invoiced Items to PowerOfficeGO Product
---------------------------------------
Every Invoiced Items will be synchronized with a PowerOfficeGO Product.

Once a link between a Invoiced Items and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - unit_cost
     - costPrice
     - N/A


Invoiced Lineitem to PowerOfficeGO Salesorderlines
--------------------------------------------------
Every Invoiced Lineitem will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Invoiced Lineitem and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
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

