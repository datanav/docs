===============================
Crmoffice to Chargebee Dataflow
===============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Companies to Chargebee Item
-------------------------------------
Every Crmoffice Companies will be synchronized with a Chargebee Item.

Once a link between a Crmoffice Companies and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Companies and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - Crmoffice Companies Property
     - Chargebee Item Property
     - Chargebee Data Type


Crmoffice Contacts to Chargebee Customer
----------------------------------------
Every Crmoffice Contacts will be synchronized with a Chargebee Customer.

Once a link between a Crmoffice Contacts and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - familyName
     - last_name
     - "string"
   * - givenName
     - first_name
     - "string"

