=====================================
Wave Financial to Membercare Dataflow
=====================================

Generated: 2024-09-03 09:11:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Membercare Companies
-------------------------------------
Every Wave Customer will be synchronized with a Membercare Companies.

Once a link between a Wave Customer and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Membercare Companies Property
     - Membercare Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Wave Country to Membercare Countries
------------------------------------
Every Wave Country will be synchronized with a Membercare Countries.

Once a link between a Wave Country and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Membercare Countries Property
     - Membercare Data Type
   * - name
     - name
     - "string"

