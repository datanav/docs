=========================
Freshteam to Ssb Dataflow
=========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Ssb Country
---------------------------------
Before any synchronization can take place, a link between a Freshteam Employee and a Ssb Country must be established.

A Freshteam Employee will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Ssb Country Property
   * - address.country
     - name
   * - communication_address.communication_country
     - name

Once a link between a Freshteam Employee and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Ssb Country Property
     - Ssb Data Type

