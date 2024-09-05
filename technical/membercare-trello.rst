=============================
Membercare to Trello Dataflow
=============================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Organizations to  Organizations
------------------------------------------
Every Membercare Organizations will be synchronized with a  Organizations.

Once a link between a Membercare Organizations and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Organizations and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Membercare Organizations Property
     -  Organizations Property
     -  Data Type
   * - name
     - name
     - "string"


Membercare Persons to  Members
------------------------------
Every Membercare Persons will be synchronized with a  Members.

Once a link between a Membercare Persons and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Persons and a  Members:

.. list-table::
   :header-rows: 1

   * - Membercare Persons Property
     -  Members Property
     -  Data Type
   * - name
     - fullName
     - "string"


Membercare Companies to  Organizations
--------------------------------------
Every Membercare Companies will be synchronized with a  Organizations.

Once a link between a Membercare Companies and a  Organizations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a  Organizations:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     -  Organizations Property
     -  Data Type
   * - companyName
     - name
     - "string"
   * - url
     - website
     - "string"

