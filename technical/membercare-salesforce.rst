=================================
MemberCare to Salesforce Dataflow
=================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Salesforce. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to Salesforce Division
-------------------------------------------
Every MemberCare Companies will be synchronized with a Salesforce Division.

Once a link between a MemberCare Companies and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - companyName
     - Name
     - "string"


MemberCare Companycategories to Salesforce Currencytype
-------------------------------------------------------
Every MemberCare Companycategories will be synchronized with a Salesforce Currencytype.

Once a link between a MemberCare Companycategories and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companycategories and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - MemberCare Companycategories Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


MemberCare Countries to Salesforce Currencytype
-----------------------------------------------
Every MemberCare Countries will be synchronized with a Salesforce Currencytype.

Once a link between a MemberCare Countries and a Salesforce Currencytype is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Countries and a Salesforce Currencytype:

.. list-table::
   :header-rows: 1

   * - MemberCare Countries Property
     - Salesforce Currencytype Property
     - Salesforce Data Type


MemberCare Organizations to Salesforce Division
-----------------------------------------------
Every MemberCare Organizations will be synchronized with a Salesforce Division.

Once a link between a MemberCare Organizations and a Salesforce Division is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Organizations and a Salesforce Division:

.. list-table::
   :header-rows: 1

   * - MemberCare Organizations Property
     - Salesforce Division Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"


MemberCare Products to Salesforce Product2
------------------------------------------
Every MemberCare Products will be synchronized with a Salesforce Product2.

Once a link between a MemberCare Products and a Salesforce Product2 is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Products and a Salesforce Product2:

.. list-table::
   :header-rows: 1

   * - MemberCare Products Property
     - Salesforce Product2 Property
     - Salesforce Data Type
   * - name
     - Name
     - "string"
   * - name
     - Name	
     - "string"


MemberCare Companies to Salesforce Organization
-----------------------------------------------
Every MemberCare Companies will be synchronized with a Salesforce Organization.

Once a link between a MemberCare Companies and a Salesforce Organization is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Salesforce Organization:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Salesforce Organization Property
     - Salesforce Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.id
     - ID
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"
   * - addresses.postalCode.zipCode
     - PostalCode
     - "string"
   * - addresses.postalCode.zipCode
     - PostalCode	
     - "string"
   * - addresses.street
     - Street
     - "string"
   * - companyName
     - Name
     - "string"
   * - companyName
     - Name	
     - "string"


MemberCare Invoices to Salesforce Invoice
-----------------------------------------
Every MemberCare Invoices will be synchronized with a Salesforce Invoice.

Once a link between a MemberCare Invoices and a Salesforce Invoice is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Salesforce Invoice:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Salesforce Invoice Property
     - Salesforce Data Type
   * - payDueDate
     - DueDate
     - "string"


MemberCare Invoices to Salesforce Invoiceline
---------------------------------------------
Every MemberCare Invoices will be synchronized with a Salesforce Invoiceline.

Once a link between a MemberCare Invoices and a Salesforce Invoiceline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Salesforce Invoiceline:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
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


MemberCare Invoices to Salesforce Orderitem
-------------------------------------------
Every MemberCare Invoices will be synchronized with a Salesforce Orderitem.

Once a link between a MemberCare Invoices and a Salesforce Orderitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Salesforce Orderitem:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
     - Salesforce Orderitem Property
     - Salesforce Data Type
   * - invoiceItems.quantity
     - Quantity
     - "string"
   * - invoiceItems.unitPrice
     - TotalPrice
     - "string"


MemberCare Invoices to Salesforce Quotelineitem
-----------------------------------------------
Every MemberCare Invoices will be synchronized with a Salesforce Quotelineitem.

Once a link between a MemberCare Invoices and a Salesforce Quotelineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Invoices and a Salesforce Quotelineitem:

.. list-table::
   :header-rows: 1

   * - MemberCare Invoices Property
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

