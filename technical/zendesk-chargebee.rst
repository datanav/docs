====================
Zendesk to  Dataflow
====================

Generated: 2024-09-02 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Zendesk to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Zendesk Organizations to  Business_entity
-----------------------------------------
Every Zendesk Organizations will be synchronized with a  Business_entity.

Once a link between a Zendesk Organizations and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Organizations and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Zendesk Organizations Property
     -  Business_entity Property
     -  Data Type
   * - name
     - name
     - "string"


Zendesk Users to  Customer
--------------------------
Every Zendesk Users will be synchronized with a  Customer.

Once a link between a Zendesk Users and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Zendesk Users and a  Customer:

.. list-table::
   :header-rows: 1

   * - Zendesk Users Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"

