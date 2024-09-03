======================
Keap to Exact Dataflow
======================

Generated: 2024-09-03 08:57:55

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to Exact. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Product to Exact Items
---------------------------
Every Keap Product will be synchronized with a Exact Items.

Once a link between a Keap Product and a Exact Items is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Product and a Exact Items:

.. list-table::
   :header-rows: 1

   * - Keap Product Property
     - Exact Items Property
     - Exact Data Type


Keap Users to Exact Addresses
-----------------------------
Every Keap Users will be synchronized with a Exact Addresses.

Once a link between a Keap Users and a Exact Addresses is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Users and a Exact Addresses:

.. list-table::
   :header-rows: 1

   * - Keap Users Property
     - Exact Addresses Property
     - Exact Data Type
   * - address.locality
     - City
     - "string"

