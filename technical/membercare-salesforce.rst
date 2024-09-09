=================================
Membercare to Salesforce Dataflow
=================================

Generated: 2024-09-09 10:37:50

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Salesforce Division
-------------------------------------------
Every Membercare Companies will be synchronized with a Salesforce Division.

Once a link between a Membercare Companies and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - companyName
     - Name
     - "string"


Membercare Companycategories to Salesforce Currencytype
-------------------------------------------------------
Every Membercare Companycategories will be synchronized with a Salesforce Currencytype.

Once a link between a Membercare Companycategories and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companycategories and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Membercare Companycategories Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Membercare Countries to Salesforce Currencytype
-----------------------------------------------
Every Membercare Countries will be synchronized with a Salesforce Currencytype.

Once a link between a Membercare Countries and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Countries and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - Membercare Countries Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


Membercare Organizations to Salesforce Division
-----------------------------------------------
Every Membercare Organizations will be synchronized with a Salesforce Division.

Once a link between a Membercare Organizations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


Membercare Products to Salesforce Product2
------------------------------------------
Every Membercare Products will be synchronized with a Salesforce Product2.

Once a link between a Membercare Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - Membercare Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name	
     - "string"


Membercare Companies to Salesforce Organization
-----------------------------------------------
Every Membercare Companies will be synchronized with a Salesforce Organization.

Once a link between a Membercare Companies and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - PostalCode	
     - "string"
   * - companyName
     - Name	
     - "string"


Membercare Invoices to Salesforce Invoice
-----------------------------------------
Every Membercare Invoices will be synchronized with a Salesforce Invoice.

Once a link between a Membercare Invoices and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - payDueDate
     - DueDate
     - "string"


Membercare Invoices to Salesforce Invoiceline
---------------------------------------------
Every Membercare Invoices will be synchronized with a Salesforce Invoiceline.

Once a link between a Membercare Invoices and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Salesforce Invoiceline Property
     - Salesforce Data Type
   * - id
     - InvoiceId
     - "string"
   * - invoiceItems.description
     - Description
     - "string"
   * - invoiceItems.quantity
     - Quantity
     - "string"
   * - invoiceItems.unitPrice
     - UnitPrice
     - "string"


Membercare Invoices to Salesforce Orderitem
-------------------------------------------
Every Membercare Invoices will be synchronized with a Salesforce Orderitem.

Once a link between a Membercare Invoices and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - invoiceItems.quantity
     - Quantity
     - "string"
   * - invoiceItems.unitPrice
     - TotalPrice
     - "string"


Membercare Invoices to Salesforce Quotelineitem
-----------------------------------------------
Every Membercare Invoices will be synchronized with a Salesforce Quotelineitem.

Once a link between a Membercare Invoices and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Invoices and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - Membercare Invoices Property
     - Salesforce Quotelineitem Property
     - Salesforce Data Type
   * - invoiceItems.description
     - Description
     - "string"
   * - invoiceItems.quantity
     - Quantity
     - "string"
   * - invoiceItems.unitPrice
     - TotalPriceWithTax
     - "string"

