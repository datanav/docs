=============================
Wix.com to Freshteam Dataflow
=============================

Generated: 2023-11-09 12:53:12

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Freshteam. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Freshteam Employee
--------------------------------------
Every Wix.com Contacts will be synchronized with a Freshteam Employee.

Once a link between a Wix.com Contacts and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Freshteam Employee Property
     - Freshteam Data Type
   * - info.addresses.items.address.countryFullname
     - Billing_Country
     - "string"
   * - info.addresses.items.address.countryFullname
     - Shipping_Country
     - "string"
   * - info.addresses.items.address.countryFullname
     - communication_address.communication_country
     - "string"
   * - info.name.first
     - first_name
     - "string"
   * - info.name.last
     - last_name
     - "string"
   * - primaryInfo.phone
     - phone_numbers.number (Dependant on having wd:Q17517 in phone_numbers.name)
     - "string"


Wix.com Members to Freshteam Employee
-------------------------------------
Every Wix.com Members will be synchronized with a Freshteam Employee.

Once a link between a Wix.com Members and a Freshteam Employee is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Freshteam Employee:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Freshteam Employee Property
     - Freshteam Data Type

