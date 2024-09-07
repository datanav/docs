===============================
Chargebee to Crmoffice Dataflow
===============================

Generated: 2024-09-07 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Chargebee to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Chargebee Customer to Crmoffice Contacts
----------------------------------------
Every Chargebee Customer will be synchronized with a Crmoffice Contacts.

Once a link between a Chargebee Customer and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Customer and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Chargebee Customer Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - first_name
     - givenName
     - "string"
   * - last_name
     - familyName
     - "string"


Chargebee Item to Crmoffice Companies
-------------------------------------
Every Chargebee Item will be synchronized with a Crmoffice Companies.

Once a link between a Chargebee Item and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Chargebee Item and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Chargebee Item Property
     - Crmoffice Companies Property
     - Crmoffice Data Type

