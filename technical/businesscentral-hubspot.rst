============================
Businesscentral to  Dataflow
============================

Generated: 2023-11-30 20:48:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Items to  Product
---------------------------------
Before any synchronization can take place, a link between a Businesscentral Items and a  Product must be established.

A new  Product will be created from a Businesscentral Items if it is connected to a Businesscentral Salesorderlines that is synchronized into .

Once a link between a Businesscentral Items and a  Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Items and a  Product:

.. list-table::
   :header-rows: 1

   * - Businesscentral Items Property
     -  Product Property
     -  Data Type


Businesscentral Company to  Company
-----------------------------------
Every Businesscentral Company will be synchronized with a  Company.

Once a link between a Businesscentral Company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Company and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Company Property
     -  Company Property
     -  Data Type


Businesscentral Contact company to  Company
-------------------------------------------
Every Businesscentral Contact company will be synchronized with a  Company.

Once a link between a Businesscentral Contact company and a  Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact company and a  Company:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact company Property
     -  Company Property
     -  Data Type
   * - addressLine1
     - properties.address
     - "string"
   * - addressLine2
     - properties.address2
     - "string"
   * - city
     - properties.city
     - "string"
   * - country
     - properties.country
     - "string"
   * - id
     - id
     - "string"
   * - phoneNumber
     - properties.phone
     - "string"
   * - postalCode
     - properties.zip
     - "string"


Businesscentral Salesorderlines to  Lineitem
--------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Lineitem.

Once a link between a Businesscentral Salesorderlines and a  Lineitem is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Lineitem:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Lineitem Property
     -  Data Type
   * - amountExcludingTax
     - properties.price
     - "string"
   * - description
     - properties.description
     - "string"
   * - invoiceQuantity
     - properties.quantity
     - "integer"
   * - itemId
     - properties.hs_product_id
     - "string"
   * - quantity
     - properties.quantity
     - "integer"


Businesscentral Salesorderlines to  Lineitemdealassociation
-----------------------------------------------------------
Every Businesscentral Salesorderlines will be synchronized with a  Lineitemdealassociation.

Once a link between a Businesscentral Salesorderlines and a  Lineitemdealassociation is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Salesorderlines and a  Lineitemdealassociation:

.. list-table::
   :header-rows: 1

   * - Businesscentral Salesorderlines Property
     -  Lineitemdealassociation Property
     -  Data Type

