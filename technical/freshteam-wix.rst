=========================
Freshteam to Wix Dataflow
=========================

Generated: 2023-09-05 08:40:40

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Freshteam to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Freshteam Employee to Wix Contacts
----------------------------------
Every Freshteam Employee will be synchronized with a Wix Contacts.

Once a link between a Freshteam Employee and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Freshteam Employee and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Freshteam Employee Property
     - Wix Contacts Property
     - Wix Data Type
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - info.phones
     - "string"

