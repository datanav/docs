==================================
Tripletex to Business Nxt Dataflow
==================================

Generated: 2024-09-12 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Business Nxt Address
------------------------------------------
Every Tripletex Customer will be synchronized with a Business Nxt Address.

Once a link between a Tripletex Customer and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Department to Business Nxt Address
--------------------------------------------
Every Tripletex Department will be synchronized with a Business Nxt Address.

Once a link between a Tripletex Department and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - name
     - name
     - "string"


Tripletex Orderline to Business Nxt Order
-----------------------------------------
Every Tripletex Orderline will be synchronized with a Business Nxt Order.

Once a link between a Tripletex Orderline and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Business Nxt Order Property
     - Business Nxt Data Type


Tripletex Country to Business Nxt Country
-----------------------------------------
Every Tripletex Country will be synchronized with a Business Nxt Country.

Once a link between a Tripletex Country and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to Business Nxt Currency
-------------------------------------------
Every Tripletex Currency will be synchronized with a Business Nxt Currency.

Once a link between a Tripletex Currency and a Business Nxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a Business Nxt Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - Business Nxt Currency Property
     - Business Nxt Data Type
   * - displayName
     - name
     - "string"


Tripletex Order to Business Nxt Order
-------------------------------------
Every Tripletex Order will be synchronized with a Business Nxt Order.

Once a link between a Tripletex Order and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - deliveryDate
     - dueDate
     - "string"
   * - orderDate
     - orderDate
     - "string"


Tripletex Orderline to Business Nxt Orderline
---------------------------------------------
Every Tripletex Orderline will be synchronized with a Business Nxt Orderline.

Once a link between a Tripletex Orderline and a Business Nxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Business Nxt Orderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Business Nxt Orderline Property
     - Business Nxt Data Type
   * - order.id
     - orderNo
     - "string"


Tripletex Product to Business Nxt Product
-----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a Business Nxt Product.

Once a link between a Tripletex Product and a Business Nxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a Business Nxt Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - Business Nxt Product Property
     - Business Nxt Data Type
   * - description
     - description
     - "string"
   * - priceExcludingVatCurrency
     - priceQuantity
     - "string"
   * - stockOfGoods
     - quantityPerUnit
     - "string"


Tripletex Productgroup to Business Nxt Productcategory
------------------------------------------------------
Every Tripletex Productgroup will be synchronized with a Business Nxt Productcategory.

Once a link between a Tripletex Productgroup and a Business Nxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a Business Nxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - Business Nxt Productcategory Property
     - Business Nxt Data Type
   * - name
     - text
     - "string"

