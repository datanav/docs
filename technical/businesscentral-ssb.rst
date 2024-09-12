================================
Business Central to Ssb Dataflow
================================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Central to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Central Salesorders to Ssb Country
-------------------------------------------
Every Business Central Salesorders will be synchronized with a Ssb Country.

Once a link between a Business Central Salesorders and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesorders and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesorders Property
     - Ssb Country Property
     - Ssb Data Type


Business Central Salesquotes to Ssb Country
-------------------------------------------
Every Business Central Salesquotes will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the Business Central Salesquotes will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A Business Central Salesquotes will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Ssb Country Property
   * - billToCountry
     - name
   * - shipToCountry
     - name

Once a link between a Business Central Salesquotes and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Central Salesquotes and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - Business Central Salesquotes Property
     - Ssb Country Property
     - Ssb Data Type

