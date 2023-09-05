=================================
Wix.com to PowerOfficeGo Dataflow
=================================

Generated: 2023-09-05 14:12:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to PowerOfficeGo Currency
--------------------------------------------
Before any synchronization can take place, a link between a Wix.com Currencies and a PowerOfficeGo Currency must be established.

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


Wix.com Contacts to PowerOfficeGo Customers
-------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGo Customers.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers Property
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

