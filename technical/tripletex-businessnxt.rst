========================================
Tripletex to Visma Business Nxt Dataflow
========================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Businessnxt Address
-----------------------------------------
Every Tripletex Customer will be synchronized with a Businessnxt Address.

Once a link between a Tripletex Customer and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Department to Businessnxt Address
-------------------------------------------
Every Tripletex Department will be synchronized with a Businessnxt Address.

Once a link between a Tripletex Department and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"


Tripletex Orderline to Businessnxt Order
----------------------------------------
Every Tripletex Orderline will be synchronized with a Businessnxt Order.

Once a link between a Tripletex Orderline and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Businessnxt Order Property
     - Businessnxt Data Type


Tripletex Country to Visma Country
----------------------------------
Every Tripletex Country will be synchronized with a Visma Country.

Once a link between a Tripletex Country and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Visma Country Property
     - Visma Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to Visma Currency
------------------------------------
Every Tripletex Currency will be synchronized with a Visma Currency.

Once a link between a Tripletex Currency and a Visma Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Visma Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Visma Currency Property
     - Visma Data Type
   * - displayName
     - name
     - "string"


Tripletex Order to Visma Order
------------------------------
Every Tripletex Order will be synchronized with a Visma Order.

Once a link between a Tripletex Order and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Visma Order Property
     - Visma Data Type
   * - deliveryDate
     - dueDate
     - "string"
   * - orderDate
     - orderDate
     - "string"


Tripletex Orderline to Visma Orderline
--------------------------------------
Every Tripletex Orderline will be synchronized with a Visma Orderline.

Once a link between a Tripletex Orderline and a Visma Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Visma Orderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Visma Orderline Property
     - Visma Data Type
   * - order.id
     - orderNo
     - "string"


Tripletex Product to Visma Product
----------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Visma Product.

Once a link between a Tripletex Product and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Visma Product Property
     - Visma Data Type
   * - description
     - description
     - "string"
   * - priceExcludingVatCurrency
     - priceQuantity
     - "string"
   * - stockOfGoods
     - quantityPerUnit
     - "string"


Tripletex Productgroup to Visma Productcategory
-----------------------------------------------
Every Tripletex Productgroup will be synchronized with a Visma Productcategory.

Once a link between a Tripletex Productgroup and a Visma Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a Visma Productcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - Visma Productcategory Property
     - Visma Data Type
   * - name
     - text
     - "string"

