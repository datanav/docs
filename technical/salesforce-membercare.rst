=================================
Salesforce to MemberCare Dataflow
=================================

Generated: 2024-09-13 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Salesforce to MemberCare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Salesforce Contact to MemberCare Persons
----------------------------------------
Every Salesforce Contact will be synchronized with a MemberCare Persons.

Once a link between a Salesforce Contact and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - MemberCare Persons Property
     - MemberCare Data Type
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


Salesforce Currencytype to MemberCare Companycategories
-------------------------------------------------------
Every Salesforce Currencytype will be synchronized with a MemberCare Companycategories.

Once a link between a Salesforce Currencytype and a MemberCare Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Currencytype and a MemberCare Companycategories:

.. list-table::
   :header-rows: 1

   * - Salesforce Currencytype Property
     - MemberCare Companycategories Property
     - MemberCare Data Type


Salesforce Customer to MemberCare Persons
-----------------------------------------
Every Salesforce Customer will be synchronized with a MemberCare Persons.

Once a link between a Salesforce Customer and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Customer and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Customer Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"


Salesforce Division to MemberCare Companies
-------------------------------------------
Every Salesforce Division will be synchronized with a MemberCare Companies.

Once a link between a Salesforce Division and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Division and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Division Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - Name
     - companyName
     - "string"


Salesforce Invoiceline to MemberCare Invoices
---------------------------------------------
Every Salesforce Invoiceline will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Invoiceline and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoiceline and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoiceline Property
     - MemberCare Invoices Property
     - MemberCare Data Type
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


Salesforce Order to MemberCare Invoices
---------------------------------------
Every Salesforce Order will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Order and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Salesforce Orderitem to MemberCare Invoices
-------------------------------------------
Every Salesforce Orderitem will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Orderitem and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Orderitem and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Orderitem Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - TotalPrice
     - invoiceItems.unitPrice
     - "string"


Salesforce Product2 to MemberCare Products
------------------------------------------
Every Salesforce Product2 will be synchronized with a MemberCare Products.

Once a link between a Salesforce Product2 and a MemberCare Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Product2 and a MemberCare Products:

.. list-table::
   :header-rows: 1

   * - Salesforce Product2 Property
     - MemberCare Products Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"
   * - Name	
     - name
     - "string"


Salesforce Quote to MemberCare Invoices
---------------------------------------
Every Salesforce Quote will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Quote and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - MemberCare Invoices Property
     - MemberCare Data Type


Salesforce Quotelineitem to MemberCare Invoices
-----------------------------------------------
Every Salesforce Quotelineitem will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Quotelineitem and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quotelineitem and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Quotelineitem Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - Description
     - invoiceItems.description
     - "string"
   * - Quantity
     - invoiceItems.quantity
     - "string"
   * - TotalPriceWithTax
     - invoiceItems.unitPrice
     - "string"


Salesforce Seller to MemberCare Persons
---------------------------------------
Every Salesforce Seller will be synchronized with a MemberCare Persons.

Once a link between a Salesforce Seller and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Seller and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce Seller Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - Name
     - name
     - "string"


Salesforce User to MemberCare Persons
-------------------------------------
Every Salesforce User will be synchronized with a MemberCare Persons.

Once a link between a Salesforce User and a MemberCare Persons is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a MemberCare Persons:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - MemberCare Persons Property
     - MemberCare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - FirstName
     - firstname
     - "string"
   * - ID
     - addresses.id
     - "string"
   * - LastName
     - lastname
     - "string"
   * - Name
     - name
     - "string"
   * - PostalCode
     - addresses.postalCode.zipCode
     - "string"


Salesforce Contact to MemberCare Countries
------------------------------------------
Every Salesforce Contact will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Contact and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Contact and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Contact Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - MailingCountry
     - name
     - "string"


Salesforce Invoice to MemberCare Invoices
-----------------------------------------
Every Salesforce Invoice will be synchronized with a MemberCare Invoices.

Once a link between a Salesforce Invoice and a MemberCare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Invoice and a MemberCare Invoices:

.. list-table::
   :header-rows: 1

   * - Salesforce Invoice Property
     - MemberCare Invoices Property
     - MemberCare Data Type
   * - DueDate
     - payDueDate
     - "string"


Salesforce Order to MemberCare Countries
----------------------------------------
Every Salesforce Order will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Order and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Order and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Order Property
     - MemberCare Countries Property
     - MemberCare Data Type
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


Salesforce Organization to MemberCare Companies
-----------------------------------------------
Every Salesforce Organization will be synchronized with a MemberCare Companies.

Once a link between a Salesforce Organization and a MemberCare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Organization and a MemberCare Companies:

.. list-table::
   :header-rows: 1

   * - Salesforce Organization Property
     - MemberCare Companies Property
     - MemberCare Data Type
   * - City
     - addresses.postalCode.city
     - "string"
   * - Country
     - addresses.country.id
     - "string"
   * - ID
     - addresses.id
     - "string"
   * - Name
     - companyName
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
   * - PostalCode	
     - addresses.postalCode.zipCode
     - "string"
   * - Street
     - addresses.street
     - "string"
   * - Street	
     - addresses.street
     - "string"


Salesforce Quote to MemberCare Countries
----------------------------------------
Every Salesforce Quote will be synchronized with a MemberCare Countries.

Once a link between a Salesforce Quote and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce Quote and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce Quote Property
     - MemberCare Countries Property
     - MemberCare Data Type
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


Salesforce User to MemberCare Countries
---------------------------------------
Every Salesforce User will be synchronized with a MemberCare Countries.

Once a link between a Salesforce User and a MemberCare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Salesforce User and a MemberCare Countries:

.. list-table::
   :header-rows: 1

   * - Salesforce User Property
     - MemberCare Countries Property
     - MemberCare Data Type
   * - Country
     - name
     - "string"
   * - CountryCode
     - iso2Letter
     - "string"

