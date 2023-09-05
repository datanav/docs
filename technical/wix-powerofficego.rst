=================================
Wix.com to PowerOfficeGo Dataflow
=================================

Generated: 2023-09-05 13:37:59

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to PowerOfficeGo Contactperson
-----------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGo Contactperson.

Once a link between a Wix.com Contacts and a PowerOfficeGo Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Contactperson:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Contactperson Property
     - PowerOfficeGo Data Type
   * - info.name.first
     - firstName
     - "string"
   * - info.name.last
     - lastName
     - "string"
   * - primaryInfo.email
     - emailAddress
     - "string"


Wix.com Contacts to PowerOfficeGo Customers
-------------------------------------------
Every Wix.com Contacts will be synchronized with a PowerOfficeGo Customers.

Once a link between a Wix.com Contacts and a PowerOfficeGo Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a PowerOfficeGo Customers:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - PowerOfficeGo Customers Property
     - PowerOfficeGo Data Type
   * - info.name.first
     - FirstName
     - "string"
   * - info.name.last
     - LastName
     - "string"
   * - primaryInfo.email
     - EmailAddress
     - "string"

