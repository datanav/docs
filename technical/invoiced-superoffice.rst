================================
Invoiced to Superoffice Dataflow
================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to Superoffice Contact
-------------------------------------------------
Every Invoiced Customers company will be synchronized with a Superoffice Contact.

Once a link between a Invoiced Customers company and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - Superoffice Contact Property
     - Superoffice Data Type
   * - address1
     - Address.Postal.Address1
     - "string"
   * - address1
     - Address.Street.Address1
     - "string"
   * - address2
     - Address.Postal.Address2
     - "string"
   * - address2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Postal.City
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - postal_code
     - Address.Postal.Zipcode
     - "string"
   * - postal_code
     - Address.Street.Zipcode
     - "string"


Invoiced Customers person to Superoffice Person
-----------------------------------------------
Every Invoiced Customers person will be synchronized with a Superoffice Person.

Once a link between a Invoiced Customers person and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - Superoffice Person Property
     - Superoffice Data Type
   * - address1
     - Address.Street.Address1
     - "string"
   * - address2
     - Address.Street.Address2
     - "string"
   * - city
     - Address.Street.City
     - "string"
   * - country
     - Country.CountryId
     - "integer"
   * - id
     - PersonId
     - "integer"
   * - postal_code
     - Address.Street.Zipcode
     - "string"


Invoiced Items to Superoffice Product
-------------------------------------
Every Invoiced Items will be synchronized with a Superoffice Product.

Once a link between a Invoiced Items and a Superoffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a Superoffice Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - Superoffice Product Property
     - Superoffice Data Type
   * - currency
     - ERPPriceListKey
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - unit_cost
     - UnitCost
     - "string"


Invoiced Lineitem to Superoffice Quoteline
------------------------------------------
Every Invoiced Lineitem will be synchronized with a Superoffice Quoteline.

Once a link between a Invoiced Lineitem and a Superoffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a Superoffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - Superoffice Quoteline Property
     - Superoffice Data Type
   * - $original_id
     - QuoteAlternativeId
     - "integer"
   * - items.amount
     - UnitListPrice
     - N/A
   * - items.description
     - Description
     - "string"
   * - items.discounts
     - ERPDiscountPercent
     - "integer"
   * - items.name
     - Name
     - "string"
   * - items.quantity
     - Quantity
     - N/A

