======================
Tripletex to  Dataflow
======================

Generated: 2023-11-30 00:00:01

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Project to  Projects
------------------------------
Every Tripletex Project will be synchronized with a  Projects.

Once a link between a Tripletex Project and a  Projects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Project and a  Projects:

.. list-table::
   :header-rows: 1

   * - Tripletex Project Property
     -  Projects Property
     -  Data Type
   * - endDate
     - due_date
     - "string"
   * - endDate
     - due_on
     - "string"
   * - name
     - name
     - "string"
   * - projectManager.id
     - owner.gid
     - "string"
   * - startDate
     - start_on
     - "string"

