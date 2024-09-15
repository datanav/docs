================================
Invoiced to SuperOffice Dataflow
================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to SuperOffice Contact
-------------------------------------------------
Every Invoiced Customers company will be synchronized with a SuperOffice Contact.

Once a link between a Invoiced Customers company and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
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


Invoiced Customers person to SuperOffice Person
-----------------------------------------------
Every Invoiced Customers person will be synchronized with a SuperOffice Person.

Once a link between a Invoiced Customers person and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - SuperOffice Person Property
     - SuperOffice Data Type
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


Invoiced Items to SuperOffice Product
-------------------------------------
Every Invoiced Items will be synchronized with a SuperOffice Product.

Once a link between a Invoiced Items and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Items and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Invoiced Items Property
     - SuperOffice Product Property
     - SuperOffice Data Type
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


Invoiced Lineitem to SuperOffice Quoteline
------------------------------------------
Every Invoiced Lineitem will be synchronized with a SuperOffice Quoteline.

Once a link between a Invoiced Lineitem and a SuperOffice Quoteline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Lineitem and a SuperOffice Quoteline:

.. list-table::
   :header-rows: 1

   * - Invoiced Lineitem Property
     - SuperOffice Quoteline Property
     - SuperOffice Data Type
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

