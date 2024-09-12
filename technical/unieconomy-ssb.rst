==========================
Unieconomy to Ssb Dataflow
==========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Countries to Ssb Country
-----------------------------------
Every Unieconomy Countries will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the Unieconomy Countries will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A Unieconomy Countries will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Ssb Country Property
   * - Name
     - name

Once a link between a Unieconomy Countries and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Countries and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - Unieconomy Countries Property
     - Ssb Country Property
     - Ssb Data Type

