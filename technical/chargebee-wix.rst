=========================
Chargebee to Wix Dataflow
=========================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a Chargebee Customer and a Wix Contacts must be established.

A new Wix Contacts will be created from a Chargebee Customer if it is connected to a Chargebee Order that is synchronized into Wix.

Once a link between a Chargebee Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - primaryInfo.email
     - "string"
   * - first_name
     - info.name.first
     - "string"
   * - last_name
     - info.name.last
     - "string"


Chargebee Item to Wix Products
------------------------------
Every Chargebee Item will be synchronized with a Wix Products.

Once a link between a Chargebee Item and a Wix Products is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Wix Products:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Wix Products Property
     - Wix Data Type

