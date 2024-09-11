========================================
Chargebee to Visma Business Nxt Dataflow
========================================

Generated: 2024-09-11 07:48:17

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Visma Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Chargebee Address to Visma Country
----------------------------------
Every Chargebee Address will be synchronized with a Visma Country.

Once a link between a Chargebee Address and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Address and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Address Property
     - Visma Country Property
     - Visma Data Type
   * - country
     - name
     - "string"


Chargebee Business_entity to Visma Address
------------------------------------------
Every Chargebee Business_entity will be synchronized with a Visma Address.

Once a link between a Chargebee Business_entity and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Visma Address:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Visma Address Property
     - Visma Data Type
   * - name
     - name
     - "string"


Chargebee Business_entity to Visma Company
------------------------------------------
Every Chargebee Business_entity will be synchronized with a Visma Company.

Once a link between a Chargebee Business_entity and a Visma Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Business_entity and a Visma Company:

.. list-table::
   :header-rows: 1

   * - Chargebee Business_entity Property
     - Visma Company Property
     - Visma Data Type
   * - name
     - name
     - "string"


Chargebee Customer to Visma Country
-----------------------------------
Every Chargebee Customer will be synchronized with a Visma Country.

Once a link between a Chargebee Customer and a Visma Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Visma Country:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Visma Country Property
     - Visma Data Type
   * - billing_address.country
     - name
     - "string"


Chargebee Item to Visma Product
-------------------------------
Every Chargebee Item will be synchronized with a Visma Product.

Once a link between a Chargebee Item and a Visma Product is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Visma Product:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Visma Product Property
     - Visma Data Type


Chargebee Order to Visma Order
------------------------------
Every Chargebee Order will be synchronized with a Visma Order.

Once a link between a Chargebee Order and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Order and a Visma Order:

.. list-table::
   :header-rows: 1

   * - Chargebee Order Property
     - Visma Order Property
     - Visma Data Type

