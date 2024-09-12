===============================
CRMOffice to Chargebee Dataflow
===============================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Chargebee. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Companies to Chargebee Item
-------------------------------------
Every CRMOffice Companies will be synchronized with a Chargebee Item.

Once a link between a CRMOffice Companies and a Chargebee Item is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a Chargebee Item:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - Chargebee Item Property
     - Chargebee Data Type


CRMOffice Contacts to Chargebee Customer
----------------------------------------
Every CRMOffice Contacts will be synchronized with a Chargebee Customer.

Once a link between a CRMOffice Contacts and a Chargebee Customer is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Chargebee Customer:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
     - Chargebee Customer Property
     - Chargebee Data Type
   * - familyName
     - last_name
     - "string"
   * - givenName
     - first_name
     - "string"

