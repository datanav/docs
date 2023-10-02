=================================
Wix.com to PowerOfficeGo Dataflow
=================================

Generated: 2023-10-02 12:32:51

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Wix.com Members to PowerOfficeGo Customers
------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOfficeGo Customers must be established.

A new PowerOfficeGo Customers will be created from a Wix.com Members if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGo.

Once a link between a Wix.com Members and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - loginEmail
     - EmailAddress
     - "string"


Wix.com Orders to PowerOfficeGo Outgoinginvoices
------------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a Wix.com Orders and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - buyerInfo.contactId
     - customerId
     - "string"
   * - buyerInfo.id
     - customerId
     - "string"
   * - currency
     - CurrencyCode
     - "string"
   * - id
     - OrderNo
     - "string"
   * - totals.total
     - NetAmount
     - "string"


Wix.com Contacts to PowerOfficeGo Contactperson
-----------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Wix.com Contacts and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - emailAddress
     - "string"


Wix.com Currencies to PowerOfficeGo Currency
--------------------------------------------
Every Wix.com Currencies will be synchronized with a PowerOfficeGo Currency.

If a matching PowerOfficeGo Currency already exists, the Wix.com Currencies will be merged with the existing one.
If no matching PowerOfficeGo Currency is found, a new PowerOfficeGo Currency will be created.

A Wix.com Currencies will merge with a PowerOfficeGo Currency if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - PowerOfficeGo Currency Property
   * - code
     - Code

Once a link between a Wix.com Currencies and a PowerOfficeGo Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a PowerOfficeGo Currency:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - PowerOfficeGo Currency Property
     - PowerOfficeGo Data Type


Wix.com Inventory to PowerOfficeGo Product
------------------------------------------
Every Wix.com Inventory will be synchronized with a PowerOfficeGo Product.

Once a link between a Wix.com Inventory and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - lastUpdated
     - availableStock
     - "string"
   * - variants.quantity
     - availableStock
     - "string"


Wix.com Orders to PowerOfficeGo Salesorderlines
-----------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGo Salesorderlines.

Once a link between a Wix.com Orders and a PowerOfficeGo Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGo Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGo Salesorderlines Property
     - PowerOfficeGo Data Type
   * - id
     - sesam_SalesOrdersId
     - "string"
   * - lineItems.name
     - Description
     - "string"
   * - lineItems.price
     - SalesOrderLineUnitPrice
     - "string"
   * - lineItems.quantity
     - Quantity
     - "string"


Wix.com Orders to PowerOfficeGo Salesorders
-------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGo Salesorders.

Once a link between a Wix.com Orders and a PowerOfficeGo Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGo Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGo Salesorders Property
     - PowerOfficeGo Data Type
   * - currency
     - CurrencyCode
     - "string"
   * - totals.total
     - TotalAmount
     - "string"


Wix.com Products to PowerOfficeGo Product
-----------------------------------------
Every Wix.com Products will be synchronized with a PowerOfficeGo Product.

Once a link between a Wix.com Products and a PowerOfficeGo Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a PowerOfficeGo Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - PowerOfficeGo Product Property
     - PowerOfficeGo Data Type
   * - costRange.maxValue
     - costPrice
     - "string"
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
     - "string"

