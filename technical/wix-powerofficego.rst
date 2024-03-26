====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 13:42:34

Introduction
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


Wix.com Contacts to  Customers person
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Customers person must be established.

A new  Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Contacts and a  Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customers person Property
     -  Data Type
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
   * - primaryInfo.phone
     - PhoneNumber
     - "string"


Wix.com Contacts to  Customers
------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Customers must be established.

A new  Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into .

Once a link between a Wix.com Contacts and a  Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Customers Property
     -  Data Type
   * - info.addresses.items.address.country
     - MailAddress.CountryCode
     - "string"


Wix.com Contacts to  Contactperson
----------------------------------
Every Wix.com Contacts will be synchronized with a  Contactperson.

If a matching  Contactperson already exists, the Wix.com Contacts will be merged with the existing one.
If no matching  Contactperson is found, a new  Contactperson will be created.

A Wix.com Contacts will merge with a  Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contactperson Property
   * - primaryInfo.email
     - emailAddress

Once a link between a Wix.com Contacts and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Contactperson Property
     -  Data Type
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
   * - primaryInfo.phone
     - phoneNumber
     - "string"


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
     - "if", "is-decimal", "decimal", "float", "decimal"]]
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
     - "integer", "decimal"]
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
     - CustomerId
     - "integer"
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
   * - costAndProfitData.itemCost
     - costPrice
     - "if", "is-decimal", "decimal", "integer"]
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

