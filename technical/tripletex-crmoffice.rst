======================
Tripletex to  Dataflow
======================

Generated: 2024-08-23 12:00:56

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Product to  Companies
-------------------------------
Every Tripletex Product will be synchronized with a  Companies.

Once a link between a Tripletex Product and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Product and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Product Property
     -  Companies Property
     -  Data Type


Tripletex Contact to  Contacts
------------------------------
Every Tripletex Contact will be synchronized with a  Contacts.

Once a link between a Tripletex Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Tripletex Contact Property
     -  Contacts Property
     -  Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"

