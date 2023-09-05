===============================
Wix.com to SuperOffice Dataflow
===============================

Generated: 2023-09-05 08:36:35

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to SuperOffice Person
--------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a SuperOffice Person must be established.

A Wix.com Contacts will merge with a SuperOffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
   * - info.emails
     - Emails.Value

Once a link between a Wix.com Contacts and a SuperOffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a SuperOffice Person:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - SuperOffice Person Property
     - SuperOffice Data Type
   * - info.emails
     - Emails.Value
     - "string"
   * - info.phones
     - MobilePhones.Value
     - "string"

