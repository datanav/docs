============================
Membercare to Exact Dataflow
============================

Generated: 2024-09-03 09:02:43

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Membercare to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Membercare Companies to Exact Addresses
---------------------------------------
Every Membercare Companies will be synchronized with a Exact Addresses.

Once a link between a Membercare Companies and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Membercare Companies and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Membercare Companies Property
     - Exact Addresses Property
     - Exact Data Type
   * - addresses.country.id
     - Country
     - "string"
   * - addresses.postalCode.city
     - City
     - "string"

