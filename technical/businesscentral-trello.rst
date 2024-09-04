============================
Businesscentral to  Dataflow
============================

Generated: 2024-09-04 14:01:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Members
-------------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Members.

Once a link between a Businesscentral Contacts person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Members:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Members Property
     -  Data Type


Businesscentral Customers company to  Organizations
---------------------------------------------------
Every Businesscentral Customers company will be synchronized with a  Organizations.

Once a link between a Businesscentral Customers company and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Customers company and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Businesscentral Customers company Property
     -  Organizations Property
     -  Data Type
   * - displayName
     - name
     - "string"
   * - website
     - website
     - "string"


Businesscentral Employees to  Members
-------------------------------------
Every Businesscentral Employees will be synchronized with a  Members.

Once a link between a Businesscentral Employees and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Members:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Members Property
     -  Data Type
   * - displayName
     - fullName
     - "string"

