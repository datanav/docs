==================================
Wix.com to PowerOffice GO Dataflow
==================================

Generated: 2024-09-11 07:53:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to PowerOffice Customers person
------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOffice Customers person must be established.

A new PowerOffice Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOffice.

A Wix.com Contacts will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice Customers person Property
   * - primaryInfo.email
     - EmailAddress

Once a link between a Wix.com Contacts and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
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


Wix.com Members to PowerOffice Contactperson
--------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOffice Contactperson must be established.

A Wix.com Members will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice Contactperson Property
   * - loginEmail
     - emailAddress

Once a link between a Wix.com Members and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - loginEmail
     - emailAddress
     - "string"


Wix.com Members to PowerOffice Customers person
-----------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOffice Customers person must be established.

A Wix.com Members will merge with a PowerOffice Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice Customers person Property
   * - loginEmail
     - EmailAddress

Once a link between a Wix.com Members and a PowerOffice Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOffice Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice Customers person Property
     - PowerOffice Data Type
   * - loginEmail
     - EmailAddress
     - "string"


Wix.com Contacts to Powerofficego Customers
-------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Powerofficego Customers must be established.

A new Powerofficego Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into Powerofficego.

Once a link between a Wix.com Contacts and a Powerofficego Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Powerofficego Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Powerofficego Customers Property
     - Powerofficego Data Type
   * - info.addresses.items.address.country
     - MailAddress.CountryCode
     - "string"


Wix.com Contacts to PowerOffice Contactperson
---------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOffice Contactperson.

If a matching PowerOffice Contactperson already exists, the Wix.com Contacts will be merged with the existing one.
If no matching PowerOffice Contactperson is found, a new PowerOffice Contactperson will be created.

A Wix.com Contacts will merge with a PowerOffice Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice Contactperson Property
   * - primaryInfo.email
     - emailAddress

Once a link between a Wix.com Contacts and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
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


Wix.com Orders to PowerOffice Salesorderlines
---------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOffice Salesorderlines.

Once a link between a Wix.com Orders and a PowerOffice Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOffice Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOffice Salesorderlines Property
     - PowerOffice Data Type
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
     - N/A
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
     - N/A
   * - totals.total
     - TotalAmount
     - "string"


Wix.com Orders to PowerOffice Salesorders
-----------------------------------------
Every Wix.com Orders will be synchronized with a PowerOffice Salesorders.

Once a link between a Wix.com Orders and a PowerOffice Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOffice Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOffice Salesorders Property
     - PowerOffice Data Type
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


Wix.com Products to PowerOffice Product
---------------------------------------
Every Wix.com Products will be synchronized with a PowerOffice Product.

Once a link between a Wix.com Products and a PowerOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a PowerOffice Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - PowerOffice Product Property
     - PowerOffice Data Type
   * - costAndProfitData.itemCost
     - costPrice
     - N/A
   * - costRange.maxValue
     - costPrice
     - N/A
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
     - N/A

