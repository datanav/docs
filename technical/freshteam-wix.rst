=========================
Freshteam to Wix Dataflow
=========================

Generated: 2023-11-08 08:34:49

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
   * - address.city
     - info.addresses.items.address.city
     - "string"
   * - address.street
     - info.addresses.items.address.addressLine
     - "string"
   * - communication_address.communication_city
     - info.addresses.items.address.city
     - "string"
   * - communication_address.communication_street
     - info.addresses.items.address.addressLine
     - "string"
   * - first_name
     - info.name.first
     - "string"
   * - id
     - id
     - "string"
   * - last_name
     - info.name.last
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - info.phones
     - "string"
   * - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.nameDependant on having wd:Q17517 in phone_numbers.name)
     - primaryInfo.phone
     - "string"

