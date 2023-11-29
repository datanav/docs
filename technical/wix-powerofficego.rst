====================
Wix.com to  Dataflow
====================

Generated: 2023-11-29 23:38:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Members to  Contactperson
---------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Contactperson must be established.

A Wix.com Members will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contactperson Property
   * - loginEmail
     - emailAddress

Once a link between a Wix.com Members and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Contactperson Property
     -  Data Type
   * - loginEmail
     - emailAddress
     - "string"


Wix.com Contacts to PowerOfficeGo Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOfficeGo Customers person must be established.

A new PowerOfficeGo Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers person Property
     - PowerOfficeGo Data Type
   * - info.addresses.items.address.country
     - MailAddress.CountryCode
     - "string"
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - EmailAddress
     - "string"


Wix.com Contacts to PowerOfficeGo Customers
-------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - info.addresses.items.address.country
     - MailAddress.CountryCode
     - "string"


Wix.com Contacts to PowerOfficeGo Contactperson
-----------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGo Contactperson.

If a matching PowerOfficeGo Contactperson already exists, the Wix.com Contacts will be merged with the existing one.
If no matching PowerOfficeGo Contactperson is found, a new PowerOfficeGo Contactperson will be created.

A Wix.com Contacts will merge with a PowerOfficeGo Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Contactperson Property
   * - primaryInfo.email
     - emailAddress

Once a link between a Wix.com Contacts and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - info.addresses.items.address.country
     - residenceCountryCode
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - emailAddress
     - "string"


Wix.com Currencies to  Currency
-------------------------------
Every Wix.com Currencies will be synchronized with a  Currency.

If a matching  Currency already exists, the Wix.com Currencies will be merged with the existing one.
If no matching  Currency is found, a new  Currency will be created.

A Wix.com Currencies will merge with a  Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     -  Currency Property
   * - code
     - code

Once a link between a Wix.com Currencies and a  Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a  Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     -  Currency Property
     -  Data Type


Wix.com Inventory to  Product
-----------------------------
Every Wix.com Inventory will be synchronized with a  Product.

Once a link between a Wix.com Inventory and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     -  Product Property
     -  Data Type
   * - lastUpdated
     - availableStock
     - "string"
   * - variants.quantity
     - availableStock
     - "integer"


Wix.com Orders to  Salesorderlines
----------------------------------
Every Wix.com Orders will be synchronized with a  Salesorderlines.

Once a link between a Wix.com Orders and a  Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorderlines Property
     -  Data Type
   * - id
     - sesam_SalesOrderId
     - "string"
   * - id
     - sesam_SalesOrdersId
     - "string"
   * - lineItems.name
     - Description
     - "string"
   * - lineItems.price
     - ProductUnitPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - lineItems.price
     - SalesOrderLineUnitPrice
     - "string"
   * - lineItems.productId
     - ProductCode
     - "string"
   * - lineItems.productId
     - ProductId
     - "integer"
   * - lineItems.quantity
     - Quantity
     - "integer"
   * - totals.total
     - TotalAmount
     - "string"


Wix.com Orders to  Salesorders
------------------------------
Every Wix.com Orders will be synchronized with a  Salesorders.

Once a link between a Wix.com Orders and a  Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a  Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     -  Salesorders Property
     -  Data Type
   * - buyerInfo.id
     - CustomerReferenceContactPersonId
     - "string"
   * - currency
     - CurrencyCode
     - "string"
   * - totals.total
     - TotalAmount
     - "string"


Wix.com Products to  Product
----------------------------
Every Wix.com Products will be synchronized with a  Product.

Once a link between a Wix.com Products and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Product Property
     -  Data Type
   * - costRange.maxValue
     - costPrice
     - "if", "is-decimal", "decimal", "integer"]
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - price.price
     - salesPrice
     - "string"
   * - priceData.price
     - salesPrice
     - "if", "is-decimal", "decimal", "integer"]

