===========================
Membercare to Keap Dataflow
===========================

Generated: 2024-09-03 09:11:47

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Keap Companies
--------------------------------------
Every Membercare Companies will be synchronized with a Keap Companies.

Once a link between a Membercare Companies and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Keap Companies Property
     - Keap Data Type
   * - companyName
     - company_name
     - "string"

