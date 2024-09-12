==========================
Freshteam to Wave Dataflow
==========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Wave. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Wave Country
----------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Wave Country must be established.

A Freshteam Employee will merge with a Wave Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Wave Country Property
   * - address.country
     - name
   * - communication_address.communication_country
     - name

Once a link between a Freshteam Employee and a Wave Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Wave Country:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Wave Country Property
     - Wave Data Type

