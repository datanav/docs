=================================
Tripletex to Businessnxt Dataflow
=================================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Tripletex Country to Businessnxt Country
----------------------------------------
Every Tripletex Country will be synchronized with a Businessnxt Country.

Once a link between a Tripletex Country and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to Businessnxt Currency
------------------------------------------
Every Tripletex Currency will be synchronized with a Businessnxt Currency.

Once a link between a Tripletex Currency and a Businessnxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Businessnxt Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Businessnxt Currency Property
     - Businessnxt Data Type
   * - displayName
     - name
     - "string"


Tripletex Order to Businessnxt Order
------------------------------------
Every Tripletex Order will be synchronized with a Businessnxt Order.

Once a link between a Tripletex Order and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - deliveryDate
     - dueDate
     - "string"
   * - orderDate
     - orderDate
     - "string"


Tripletex Orderline to Businessnxt Orderline
--------------------------------------------
Every Tripletex Orderline will be synchronized with a Businessnxt Orderline.

Once a link between a Tripletex Orderline and a Businessnxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Businessnxt Orderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Businessnxt Orderline Property
     - Businessnxt Data Type
   * - order.id
     - orderNo
     - "string"


Tripletex Product to Businessnxt Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Businessnxt Product.

Once a link between a Tripletex Product and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Businessnxt Product Property
     - Businessnxt Data Type
   * - description
     - description
     - "string"
   * - priceExcludingVatCurrency
     - priceQuantity
     - "string"
   * - stockOfGoods
     - quantityPerUnit
     - "string"


Tripletex Productgroup to Businessnxt Productcategory
-----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a Businessnxt Productcategory.

Once a link between a Tripletex Productgroup and a Businessnxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a Businessnxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - Businessnxt Productcategory Property
     - Businessnxt Data Type
   * - name
     - text
     - "string"

