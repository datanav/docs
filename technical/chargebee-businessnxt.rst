=================================
Chargebee to BusinessNxt Dataflow
=================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Currency to BusinessNxt Country
-----------------------------------------
Every Chargebee Currency will be synchronized with a BusinessNxt Country.

Once a link between a Chargebee Currency and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


Chargebee Item_family to BusinessNxt Country
--------------------------------------------
Every Chargebee Item_family will be synchronized with a BusinessNxt Country.

Once a link between a Chargebee Item_family and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type


Chargebee Address to BusinessNxt Country
----------------------------------------
Every Chargebee Address will be synchronized with a BusinessNxt Country.

Once a link between a Chargebee Address and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to BusinessNxt Address
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a BusinessNxt Address.

Once a link between a Chargebee Business_entity and a BusinessNxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a BusinessNxt Address:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - BusinessNxt Address Property
     - BusinessNxt Data Type
   * - name
     - name
     - "string"


Chargebee Business_entity to BusinessNxt Company
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a BusinessNxt Company.

Once a link between a Chargebee Business_entity and a BusinessNxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a BusinessNxt Company:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - BusinessNxt Company Property
     - BusinessNxt Data Type
   * - name
     - name
     - "string"


Chargebee Customer to BusinessNxt Country
-----------------------------------------
Every Chargebee Customer will be synchronized with a BusinessNxt Country.

Once a link between a Chargebee Customer and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - billing_address.country
     - name
     - "string"


Chargebee Item to BusinessNxt Product
-------------------------------------
Every Chargebee Item will be synchronized with a BusinessNxt Product.

Once a link between a Chargebee Item and a BusinessNxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a BusinessNxt Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - BusinessNxt Product Property
     - BusinessNxt Data Type


Chargebee Order to BusinessNxt Order
------------------------------------
Every Chargebee Order will be synchronized with a BusinessNxt Order.

Once a link between a Chargebee Order and a BusinessNxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a BusinessNxt Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - BusinessNxt Order Property
     - BusinessNxt Data Type

