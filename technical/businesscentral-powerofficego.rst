============================
Businesscentral to  Dataflow
============================

Generated: 2023-12-02 00:00:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contact person to  Contactperson
------------------------------------------------
Every Businesscentral Contact person will be synchronized with a  Contactperson.

Once a link between a Businesscentral Contact person and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact person and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact person Property
     -  Contactperson Property
     -  Data Type
   * - addressLine1
     - address1
     - "string"
   * - addressLine2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - residenceCountryCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - zipCode
     - "string"


Businesscentral Currencies to  Currency
---------------------------------------
Every Businesscentral Currencies will be synchronized with a  Currency.

If a matching  Currency already exists, the Businesscentral Currencies will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A Businesscentral Currencies will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
   * - code
     - code

Once a link between a Businesscentral Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Businesscentral Currencies Property
     -  Currency Property
     -  Data Type


Businesscentral Items to  Product
---------------------------------
Every Businesscentral Items will be synchronized with a  Product.

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - displayName.string
     - name
     - "string"
   * - gtin
     - gtin
     - "string"
   * - inventory
     - availableStock
     - "integer"
   * - taxGroupCode
     - vatCode
     - "string"
   * - unitCost
     - costPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - unitPrice
     - salesPrice
     - "if", "is-decimal", "decimal", "integer"]


Businesscentral Salesorderlines to  Salesorderlines
---------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Salesorderlines.

Once a link between a Businesscentral Salesorderlines and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Salesorderlines Property
     -  Data Type
   * - amountExcludingTax
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - discountPercent
     - Allowance
     - "float"
   * - invoiceQuantity
     - Quantity
     - "integer"
   * - itemId
     - ProductId
     - "integer"
   * - quantity
     - Quantity
     - "integer"
   * - unitPrice
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]


Businesscentral Salesorders to  Salesorders
-------------------------------------------
Every Businesscentral Salesorders will be synchronized with a  Salesorders.

Once a link between a Businesscentral Salesorders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorders Property
     -  Salesorders Property
     -  Data Type
   * - currencyId
     - CurrencyCode
     - "string"
   * - customerId
     - CustomerReferenceContactPersonId
     - "string"
   * - orderDate
     - SalesOrderDate
     - "string"

