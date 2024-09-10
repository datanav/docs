=================================
Chargebee to Businessnxt Dataflow
=================================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Currency to Businessnxt Country
-----------------------------------------
Every Chargebee Currency will be synchronized with a Businessnxt Country.

Once a link between a Chargebee Currency and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Currency and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Currency Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Chargebee Item_family to Businessnxt Country
--------------------------------------------
Every Chargebee Item_family will be synchronized with a Businessnxt Country.

Once a link between a Chargebee Item_family and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item_family and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Item_family Property
     - Businessnxt Country Property
     - Businessnxt Data Type


Chargebee Address to Businessnxt Country
----------------------------------------
Every Chargebee Address will be synchronized with a Businessnxt Country.

Once a link between a Chargebee Address and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to Businessnxt Address
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Businessnxt Address.

Once a link between a Chargebee Business_entity and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"


Chargebee Business_entity to Businessnxt Company
------------------------------------------------
Every Chargebee Business_entity will be synchronized with a Businessnxt Company.

Once a link between a Chargebee Business_entity and a Businessnxt Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Businessnxt Company:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Businessnxt Company Property
     - Businessnxt Data Type
   * - name
     - name
     - "string"


Chargebee Customer to Businessnxt Country
-----------------------------------------
Every Chargebee Customer will be synchronized with a Businessnxt Country.

Once a link between a Chargebee Customer and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - billing_address.country
     - name
     - "string"


Chargebee Item to Businessnxt Product
-------------------------------------
Every Chargebee Item will be synchronized with a Businessnxt Product.

Once a link between a Chargebee Item and a Businessnxt Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Businessnxt Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Businessnxt Product Property
     - Businessnxt Data Type


Chargebee Order to Businessnxt Order
------------------------------------
Every Chargebee Order will be synchronized with a Businessnxt Order.

Once a link between a Chargebee Order and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Businessnxt Order Property
     - Businessnxt Data Type

