=================================
Wix.com to PowerOfficeGO Dataflow
=================================

Generated: 2024-09-11 08:38:15

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOfficeGO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to PowerOfficeGO Customers person
--------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOfficeGO Customers person must be established.

A new PowerOfficeGO Customers person will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOfficeGO.

A Wix.com Contacts will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGO Customers person Property
   * - primaryInfo.email
     - EmailAddress

Once a link between a Wix.com Contacts and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
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


Wix.com Members to PowerOfficeGO Contactperson
----------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOfficeGO Contactperson must be established.

A Wix.com Members will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGO Contactperson Property
   * - loginEmail
     - emailAddress

Once a link between a Wix.com Members and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
   * - loginEmail
     - emailAddress
     - "string"


Wix.com Members to PowerOfficeGO Customers person
-------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOfficeGO Customers person must be established.

A Wix.com Members will merge with a PowerOfficeGO Customers person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGO Customers person Property
   * - loginEmail
     - EmailAddress

Once a link between a Wix.com Members and a PowerOfficeGO Customers person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOfficeGO Customers person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOfficeGO Customers person Property
     - PowerOfficeGO Data Type
   * - loginEmail
     - EmailAddress
     - "string"


Wix.com Contacts to PowerOffice Customers
-----------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOffice Customers must be established.

A new PowerOffice Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOffice.

Once a link between a Wix.com Contacts and a PowerOffice Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice Customers Property
     - PowerOffice Data Type
   * - info.addresses.items.address.country
     - MailAddress.CountryCode
     - "string"


Wix.com Contacts to PowerOfficeGO Contactperson
-----------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGO Contactperson.

If a matching PowerOfficeGO Contactperson already exists, the Wix.com Contacts will be merged with the existing one.
If no matching PowerOfficeGO Contactperson is found, a new PowerOfficeGO Contactperson will be created.

A Wix.com Contacts will merge with a PowerOfficeGO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGO Contactperson Property
   * - primaryInfo.email
     - emailAddress

Once a link between a Wix.com Contacts and a PowerOfficeGO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGO Contactperson Property
     - PowerOfficeGO Data Type
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


Wix.com Orders to PowerOfficeGO Salesorderlines
-----------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGO Salesorderlines.

Once a link between a Wix.com Orders and a PowerOfficeGO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGO Salesorderlines Property
     - PowerOfficeGO Data Type
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


Wix.com Orders to PowerOfficeGO Salesorders
-------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOfficeGO Salesorders.

Once a link between a Wix.com Orders and a PowerOfficeGO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOfficeGO Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOfficeGO Salesorders Property
     - PowerOfficeGO Data Type
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


Wix.com Products to PowerOfficeGO Product
-----------------------------------------
Every Wix.com Products will be synchronized with a PowerOfficeGO Product.

Once a link between a Wix.com Products and a PowerOfficeGO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a PowerOfficeGO Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - PowerOfficeGO Product Property
     - PowerOfficeGO Data Type
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

