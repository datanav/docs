=============================
Powerofficego to Wix Dataflow
=============================

Generated: 2023-10-01 14:13:48

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Customers to Wix Contacts
---------------------------------------
Every Powerofficego Customers will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Customers and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - info.emails
     - "string"


Powerofficego Customers to Wix Members
--------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers and a Wix Members must be established.

A new Wix Members will be created from a Powerofficego Customers if it is connected to a Powerofficego Salesorders, Salesorderline, or Outgoinginvoices that is synchronized into Wix.

Once a link between a Powerofficego Customers and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Wix Members Property
     - Wix Data Type
   * - EmailAddress
     - loginEmail
     - "string"


Powerofficego Employees to Wix Contacts
---------------------------------------
Every Powerofficego Employees will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Employees and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Employees and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Employees Property
     - Wix Contacts Property
     - Wix Data Type
   * - FirstName
     - info.name.first
     - "string"
   * - LastName
     - info.name.last
     - "string"
   * - PhoneNumber
     - info.phones
     - "string"
   * - PhoneNumber
     - primaryInfo.phone
     - "string"


Powerofficego Outgoinginvoices to Wix Orders
--------------------------------------------
Every Powerofficego Outgoinginvoices will be synchronized with a Wix Orders.

Once a link between a Powerofficego Outgoinginvoices and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Outgoinginvoices and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Outgoinginvoices Property
     - Wix Orders Property
     - Wix Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - NetAmount
     - totals.total
     - "string"
   * - customerId
     - buyerInfo.contactId
     - "string"
   * - customerId
     - buyerInfo.id
     - "string"


Powerofficego Salesorderline to Wix Orders
------------------------------------------
Every Powerofficego Salesorderline will be synchronized with a Wix Orders.

Once a link between a Powerofficego Salesorderline and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorderline and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorderline Property
     - Wix Orders Property
     - Wix Data Type
   * - Description
     - lineItems.name
     - "string"
   * - Description
     - lineItems.name.name
     - "string"
   * - Quantity
     - lineItems.quantity
     - "string"
   * - Quantity
     - lineItems.quantity.quantity
     - "string"
   * - SalesOrderLineUnitPrice
     - lineItems.price
     - "string"
   * - SalesOrderLineUnitPrice
     - lineItems.price.price
     - "string"


Powerofficego Contactperson to Wix Contacts
-------------------------------------------
Every Powerofficego Contactperson will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Contactperson and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Wix Contacts Property
     - Wix Data Type
   * - emailAddress
     - info.emails
     - "string"
   * - emailAddress
     - primaryInfo.email
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"


Powerofficego Currency to Wix Currencies
----------------------------------------
Every Powerofficego Currency will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the Powerofficego Currency will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A Powerofficego Currency will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Wix Currencies Property
   * - Code
     - code

Once a link between a Powerofficego Currency and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - Wix Currencies Property
     - Wix Data Type


Powerofficego Customers person to Wix Contacts
----------------------------------------------
Every Powerofficego Customers person will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Customers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Wix Contacts Property
     - Wix Data Type
   * - EmailAddress
     - primaryInfo.email
     - "string"
   * - FirstName
     - info.name.first
     - "string"
   * - LastName
     - info.name.last
     - "string"


Powerofficego Product to Wix Inventory
--------------------------------------
Every Powerofficego Product will be synchronized with a Wix Inventory.

Once a link between a Powerofficego Product and a Wix Inventory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wix Inventory:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Wix Inventory Property
     - Wix Data Type
   * - availableStock
     - lastUpdated
     - "string"
   * - availableStock
     - variants.quantity
     - "string"


Powerofficego Product to Wix Products
-------------------------------------
Every Powerofficego Product will be synchronized with a Wix Products.

Once a link between a Powerofficego Product and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Product and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Powerofficego Product Property
     - Wix Products Property
     - Wix Data Type
   * - costPrice
     - costRange.maxValue
     - "string"
   * - description
     - description
     - "string"
   * - name
     - name
     - "string"
   * - salesPrice
     - price.price
     - "string"
   * - salesPrice
     - priceData.price
     - "decimal"


Powerofficego Salesorders to Wix Orders
---------------------------------------
Every Powerofficego Salesorders will be synchronized with a Wix Orders.

Once a link between a Powerofficego Salesorders and a Wix Orders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Salesorders and a Wix Orders:

.. list-table::
   :header-rows: 1

   * - Powerofficego Salesorders Property
     - Wix Orders Property
     - Wix Data Type
   * - CurrencyCode
     - currency
     - "string"
   * - TotalAmount
     - totals.total
     - "string"


Powerofficego Suppliers person to Wix Contacts
----------------------------------------------
Every Powerofficego Suppliers person will be synchronized with a Wix Contacts.

Once a link between a Powerofficego Suppliers person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Suppliers person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Powerofficego Suppliers person Property
     - Wix Contacts Property
     - Wix Data Type
   * - FirstName
     - info.name.first
     - "string"

