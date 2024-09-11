=================================
Tripletex to BusinessNxt Dataflow
=================================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to Visma Address
-----------------------------------
Every Tripletex Customer will be synchronized with a Visma Address.

Once a link between a Tripletex Customer and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     - Visma Address Property
     - Visma Data Type
   * - name
     - name
     - "string"
   * - phoneNumber
     - phone
     - "string"
   * - phoneNumberMobile
     - mobilePhone
     - "string"


Tripletex Department to Visma Address
-------------------------------------
Every Tripletex Department will be synchronized with a Visma Address.

Once a link between a Tripletex Department and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     - Visma Address Property
     - Visma Data Type
   * - name
     - name
     - "string"


Tripletex Orderline to Visma Order
----------------------------------
Every Tripletex Orderline will be synchronized with a Visma Order.

Once a link between a Tripletex Orderline and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - Visma Order Property
     - Visma Data Type


Tripletex Country to BusinessNxt Country
----------------------------------------
Every Tripletex Country will be synchronized with a BusinessNxt Country.

Once a link between a Tripletex Country and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"


Tripletex Currency to BusinessNxt Currency
------------------------------------------
Every Tripletex Currency will be synchronized with a BusinessNxt Currency.

Once a link between a Tripletex Currency and a BusinessNxt Currency is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Currency and a BusinessNxt Currency:

.. list-table::
   :header-rows: 1

   * - Tripletex Currency Property
     - BusinessNxt Currency Property
     - BusinessNxt Data Type
   * - displayName
     - name
     - "string"


Tripletex Order to BusinessNxt Order
------------------------------------
Every Tripletex Order will be synchronized with a BusinessNxt Order.

Once a link between a Tripletex Order and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Order and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Tripletex Order Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type
   * - deliveryDate
     - dueDate
     - "string"
   * - orderDate
     - orderDate
     - "string"


Tripletex Orderline to BusinessNxt Orderline
--------------------------------------------
Every Tripletex Orderline will be synchronized with a BusinessNxt Orderline.

Once a link between a Tripletex Orderline and a BusinessNxt Orderline is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Orderline and a BusinessNxt Orderline:

.. list-table::
   :header-rows: 1

   * - Tripletex Orderline Property
     - BusinessNxt Orderline Property
     - BusinessNxt Data Type
   * - order.id
     - orderNo
     - "string"


Tripletex Product to BusinessNxt Product
----------------------------------------
preliminary mapping until we can sort out suppliers. This removes all supplier products for now, it  will be synchronized with a BusinessNxt Product.

Once a link between a Tripletex Product and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type
   * - description
     - description
     - "string"
   * - priceExcludingVatCurrency
     - priceQuantity
     - "string"
   * - stockOfGoods
     - quantityPerUnit
     - "string"


Tripletex Productgroup to BusinessNxt Productcategory
-----------------------------------------------------
Every Tripletex Productgroup will be synchronized with a BusinessNxt Productcategory.

Once a link between a Tripletex Productgroup and a BusinessNxt Productcategory is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Productgroup and a BusinessNxt Productcategory:

.. list-table::
   :header-rows: 1

   * - Tripletex Productgroup Property
     - BusinessNxt Productcategory Property
     - BusinessNxt Data Type
   * - name
     - text
     - "string"

