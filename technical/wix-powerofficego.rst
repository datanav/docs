==================================
Wix.com to PowerOffice GO Dataflow
==================================

Generated: 2024-10-14 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOffice GO. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to PowerOffice GO Contactperson
------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOffice GO Contactperson must be established.

A new PowerOffice GO Contactperson will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOffice GO.

A Wix.com Contacts will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice GO Contactperson Property
   * - primaryInfo.email
     - emailAddress

Once a link between a Wix.com Contacts and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
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


Wix.com Contacts to PowerOffice GO Customers
--------------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a PowerOffice GO Customers must be established.

A new PowerOffice GO Customers will be created from a Wix.com Contacts if it is connected to a Wix.com Wix-orders that is synchronized into PowerOffice GO.

A Wix.com Contacts will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice GO Customers Property
   * - primaryInfo.email
     - EmailAddress

Once a link between a Wix.com Contacts and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
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


Wix.com Members to PowerOffice GO Contactperson
-----------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOffice GO Contactperson must be established.

A Wix.com Members will merge with a PowerOffice GO Contactperson if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice GO Contactperson Property
   * - loginEmail
     - emailAddress

Once a link between a Wix.com Members and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type
   * - loginEmail
     - emailAddress
     - "string"


Wix.com Members to PowerOffice GO Customers
-------------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a PowerOffice GO Customers must be established.

A Wix.com Members will merge with a PowerOffice GO Customers if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice GO Customers Property
   * - loginEmail
     - EmailAddress

Once a link between a Wix.com Members and a PowerOffice GO Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a PowerOffice GO Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - PowerOffice GO Customers Property
     - PowerOffice GO Data Type
   * - loginEmail
     - EmailAddress
     - "string"


Wix.com Contacts to PowerOffice GO Contactperson
------------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOffice GO Contactperson.

Once a link between a Wix.com Contacts and a PowerOffice GO Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOffice GO Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOffice GO Contactperson Property
     - PowerOffice GO Data Type


Wix.com Orders to PowerOffice GO Salesorderlines
------------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOffice GO Salesorderlines.

Once a link between a Wix.com Orders and a PowerOffice GO Salesorderlines is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOffice GO Salesorderlines:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOffice GO Salesorderlines Property
     - PowerOffice GO Data Type
   * - id
     - sesam_SalesOrderId
     - "string"
   * - lineItems.name
     - Description
     - "string"
   * - lineItems.price
     - ProductUnitPrice
     - N/A
   * - lineItems.productId
     - ProductId
     - "integer"
   * - lineItems.quantity
     - Quantity
     - N/A


Wix.com Orders to PowerOffice GO Salesorders
--------------------------------------------
Every Wix.com Orders will be synchronized with a PowerOffice GO Salesorders.

Once a link between a Wix.com Orders and a PowerOffice GO Salesorders is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Orders and a PowerOffice GO Salesorders:

.. list-table::
   :header-rows: 1

   * - Wix.com Orders Property
     - PowerOffice GO Salesorders Property
     - PowerOffice GO Data Type
   * - buyerInfo.id
     - CustomerId
     - "integer"
   * - buyerInfo.id
     - CustomerReferenceContactPersonId
     - "integer"
   * - currency
     - CurrencyCode
     - "string"


Wix.com Products to PowerOffice GO Product
------------------------------------------
Every Wix.com Products will be synchronized with a PowerOffice GO Product.

Once a link between a Wix.com Products and a PowerOffice GO Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a PowerOffice GO Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - PowerOffice GO Product Property
     - PowerOffice GO Data Type
   * - costAndProfitData.itemCost
     - costPrice
     - N/A
   * - costRange.maxValue
     - costPrice
     - N/A
   * - name
     - name
     - "string"
   * - priceData.price
     - salesPrice
     - N/A

