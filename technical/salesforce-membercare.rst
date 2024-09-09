=================================
Salesforce to Membercare Dataflow
=================================

Generated: 2024-09-09 09:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to Membercare Persons
----------------------------------------
Every Salesforce Contact will be synchronized with a Membercare Persons.

Once a link between a Salesforce Contact and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Membercare Persons Property
     - Membercare Data Type
   * - Birthdate
     - birthDate
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - LastName
     - lastname
     - "string"
   * - Name
     - firstname
     - "string"
   * - Name
     - name
     - "string"


Salesforce Currencytype to Membercare Companycategories
-------------------------------------------------------
Every Salesforce Currencytype will be synchronized with a Membercare Companycategories.

Once a link between a Salesforce Currencytype and a Membercare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a Membercare Companycategories:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - Membercare Companycategories Property
     - Membercare Data Type


Salesforce Customer to Membercare Persons
-----------------------------------------
Every Salesforce Customer will be synchronized with a Membercare Persons.

Once a link between a Salesforce Customer and a Membercare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a Membercare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - Membercare Persons Property
     - Membercare Data Type
   * - Name
     - name
     - "string"


Salesforce Division to Membercare Companies
-------------------------------------------
Every Salesforce Division will be synchronized with a Membercare Companies.

Once a link between a Salesforce Division and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Name
     - companyName
     - "string"


Salesforce Invoiceline to Membercare Invoices
---------------------------------------------
Every Salesforce Invoiceline will be synchronized with a Membercare Invoices.

Once a link between a Salesforce Invoiceline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - Description
     - invoiceItems.description
     - "string"
   * - InvoiceId
     - id
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - UnitPrice
     - invoiceItems.unitPrice
     - "string"


Salesforce Order to Membercare Invoices
---------------------------------------
Every Salesforce Order will be synchronized with a Membercare Invoices.

Once a link between a Salesforce Order and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Membercare Invoices Property
     - Membercare Data Type


Salesforce Orderitem to Membercare Invoices
-------------------------------------------
Every Salesforce Orderitem will be synchronized with a Membercare Invoices.

Once a link between a Salesforce Orderitem and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - TotalPrice
     - invoiceItems.unitPrice
     - "string"


Salesforce Product2 to Membercare Products
------------------------------------------
Every Salesforce Product2 will be synchronized with a Membercare Products.

Once a link between a Salesforce Product2 and a Membercare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a Membercare Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - Membercare Products Property
     - Membercare Data Type
   * - Name	
     - name
     - "string"


Salesforce Contact to Membercare Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a Membercare Countries.

Once a link between a Salesforce Contact and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - Membercare Countries Property
     - Membercare Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Invoice to Membercare Invoices
-----------------------------------------
Every Salesforce Invoice will be synchronized with a Membercare Invoices.

Once a link between a Salesforce Invoice and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - Membercare Invoices Property
     - Membercare Data Type
   * - DueDate
     - payDueDate
     - "string"


Salesforce Order to Membercare Countries
----------------------------------------
Every Salesforce Order will be synchronized with a Membercare Countries.

Once a link between a Salesforce Order and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - Membercare Countries Property
     - Membercare Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - iso2Letter
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - iso2Letter
     - "string"


Salesforce Organization to Membercare Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a Membercare Companies.

Once a link between a Salesforce Organization and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - Membercare Companies Property
     - Membercare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - Name	
     - companyName
     - "string"
   * - Name	
     - name
     - "string"
   * - PostalCode	
     - addresses.postalCode.zipCode
     - "string"
   * - Street	
     - addresses.street
     - "string"


Salesforce Quote to Membercare Countries
----------------------------------------
Every Salesforce Quote will be synchronized with a Membercare Countries.

Once a link between a Salesforce Quote and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - Membercare Countries Property
     - Membercare Data Type
   * - BillingCountry
     - name
     - "string"
   * - BillingCountryCode
     - iso2Letter
     - "string"
   * - ShippingCountry
     - name
     - "string"
   * - ShippingCountryCode
     - iso2Letter
     - "string"

