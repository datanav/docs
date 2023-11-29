====================
Wix.com to  Dataflow
====================

Generated: 2023-11-29 23:45:21

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Person
---------------------------
Every Wix.com Contacts will be synchronized with a  Person.

If a matching  Person already exists, the Wix.com Contacts will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A Wix.com Contacts will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Person Property
   * - primaryInfo.email
     - Emails.Value

Once a link between a Wix.com Contacts and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Person Property
     -  Data Type
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


Wix.com Members to  Person
--------------------------
Every Wix.com Members will be synchronized with a  Person.

If a matching  Person already exists, the Wix.com Members will be merged with the existing one.
If no matching  Person is found, a new  Person will be created.

A Wix.com Members will merge with a  Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Person Property
   * - loginEmail
     - Emails.Value

Once a link between a Wix.com Members and a  Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Person Property
     -  Data Type
   * - loginEmail
     - Emails.Value
     - "string"


Wix.com Products classification to  Listproducttypeitems
--------------------------------------------------------
Before any synchronization can take place, a link between a Wix.com Products classification and a  Listproducttypeitems must be established.

A new  Listproducttypeitems will be created from a Wix.com Products classification if it is connected to a Wix.com Wix-products, or Wix-inventory that is synchronized into .

Once a link between a Wix.com Products classification and a  Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products classification and a  Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Wix.com Products classification Property
     -  Listproducttypeitems Property
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


Wix.com Products to  Listproducttypeitems
-----------------------------------------
Every Wix.com Products will be synchronized with a  Listproducttypeitems.

Once a link between a Wix.com Products and a  Listproducttypeitems is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Products and a  Listproducttypeitems:

.. list-table::
   :header-rows: 1

   * - Wix.com Products Property
     -  Listproducttypeitems Property
     -  Data Type
   * - productType
     - Name
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

