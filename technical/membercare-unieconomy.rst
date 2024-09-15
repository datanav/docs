=================================
MemberCare to Unieconomy Dataflow
=================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from MemberCare to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

MemberCare Companies to Unieconomy Companies
--------------------------------------------
Every MemberCare Companies will be synchronized with a Unieconomy Companies.

Once a link between a MemberCare Companies and a Unieconomy Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a MemberCare Companies and a Unieconomy Companies:

.. list-table::
   :header-rows: 1

   * - MemberCare Companies Property
     - Unieconomy Companies Property
     - Unieconomy Data Type
   * - companyName
     - Name
     - "string"

