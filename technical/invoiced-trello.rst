===========================
Invoiced to Trello Dataflow
===========================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to  Organizations
--------------------------------------------
Every Invoiced Customers company will be synchronized with a  Organizations.

Once a link between a Invoiced Customers company and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"


Invoiced Customers person to  Members
-------------------------------------
Every Invoiced Customers person will be synchronized with a  Members.

Once a link between a Invoiced Customers person and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a  Members:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     -  Members Property
     -  Data Type
   * - name
     - fullName
     - "string"

