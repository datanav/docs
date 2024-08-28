============================
Businesscentral to  Dataflow
============================

Generated: 2024-08-28 09:26:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Customers company to  Business_entity
-----------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Business_entity.

Once a link between a Businesscentral Customers company and a  Business_entity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Business_entity:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Business_entity Property
     -  Data Type
   * - displayName
     - name
     - "string"


Businesscentral Customers company to  Customer
----------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Customer.

Once a link between a Businesscentral Customers company and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Customer Property
     -  Data Type


Businesscentral Customers person to  Customer
---------------------------------------------
Every Businesscentral Customers person will be synchronized with a  Customer.

Once a link between a Businesscentral Customers person and a  Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers person and a  Customer:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers person Property
     -  Customer Property
     -  Data Type
   * - email
     - email
     - "string"

