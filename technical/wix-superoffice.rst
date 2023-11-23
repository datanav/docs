===============================
Wix.com to SuperOffice Dataflow
===============================

Generated: 2023-11-23 11:43:00

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to SuperOffice Person
--------------------------------------
Every Wix.com Contacts will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Wix.com Contacts will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Wix.com Contacts will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
   * - info.emails
     - Emails.Value
   * - primaryInfo.email
     - Emails.Value

Once a link between a Wix.com Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - info.emails
     - Emails.Value
     - "string"
   * - info.name.first
     - Firstname
     - "string"
   * - info.name.last
     - Lastname
     - "string"
   * - info.phones
     - MobilePhones.Value
     - "string"
   * - primaryInfo.email
     - Emails.Value
     - "string"
   * - primaryInfo.phone
     - MobilePhones.Value
     - "string"


Wix.com Members to SuperOffice Person
-------------------------------------
Every Wix.com Members will be synchronized with a SuperOffice Person.

If a matching SuperOffice Person already exists, the Wix.com Members will be merged with the existing one.
If no matching SuperOffice Person is found, a new SuperOffice Person will be created.

A Wix.com Members will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - SuperOffice Person Property
   * - loginEmail
     - Emails.Value

Once a link between a Wix.com Members and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - loginEmail
     - Emails.Value
     - "string"


Wix.com Products classification to SuperOffice Listproducttypeitems
-------------------------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Products classification and a SuperOffice Listproducttypeitems must be established.

A new SuperOffice Listproducttypeitems will be created from a Wix.com Products classification if it is connected to a Wix.com Wix-products, or Wix-inventory that is synchronized into SuperOffice.

Once a link between a Wix.com Products classification and a SuperOffice Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products classification and a SuperOffice Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Wix.com Products classification Property
     - SuperOffice Listproducttypeitems Property
     - SuperOffice Data Type


Wix.com Inventory to SuperOffice Product
----------------------------------------
Every Wix.com Inventory will be synchronized with a SuperOffice Product.

If a matching SuperOffice Product already exists, the Wix.com Inventory will be merged with the existing one.
If no matching SuperOffice Product is found, a new SuperOffice Product will be created.

A Wix.com Inventory will merge with a SuperOffice Product if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - SuperOffice Product Property
   * - id
     - ERPProductKey

Once a link between a Wix.com Inventory and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Inventory and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Inventory Property
     - SuperOffice Product Property
     - SuperOffice Data Type


Wix.com Products to SuperOffice Listproducttypeitems
----------------------------------------------------
Every Wix.com Products will be synchronized with a SuperOffice Listproducttypeitems.

Once a link between a Wix.com Products and a SuperOffice Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a SuperOffice Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - SuperOffice Listproducttypeitems Property
     - SuperOffice Data Type
   * - productType
     - Name
     - "string"


Wix.com Products to SuperOffice Product
---------------------------------------
Every Wix.com Products will be synchronized with a SuperOffice Product.

Once a link between a Wix.com Products and a SuperOffice Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a SuperOffice Product:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     - SuperOffice Product Property
     - SuperOffice Data Type
   * - costRange.maxValue
     - UnitCost
     - "string"
   * - description
     - Description
     - "string"
   * - name
     - Name
     - "string"
   * - price.currency
     - ERPPriceListKey
     - "string"
   * - price.price
     - UnitListPrice
     - "decimal"
   * - priceData.currency
     - ERPPriceListKey
     - "string"
   * - priceData.price
     - UnitListPrice
     - "decimal"

