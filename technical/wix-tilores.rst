===========================
Wix.com to Tilores Dataflow
===========================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Tilores Human
---------------------------------
Every Wix.com Contacts will be synchronized with a Tilores Human.

Once a link between a Wix.com Contacts and a Tilores Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tilores Human:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tilores Human Property
     - Tilores Data Type
   * - id
     - id
     - "string"
   * - info.addresses.items.address.addressLine
     - street
     - "string"
   * - info.addresses.items.address.city
     - city
     - "string"
   * - info.addresses.items.address.postalCode
     - postalCode
     - "string"
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - email
     - "string"

