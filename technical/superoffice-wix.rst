===========================
SuperOffice to Wix Dataflow
===========================

Generated: 2023-09-05 08:36:29

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Wix Contacts
----------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Wix Contacts must be established.

A SuperOffice Person will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
   * - Emails.Value
     - info.emails

Once a link between a SuperOffice Person and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Wix Contacts Property
     - Wix Data Type


SuperOffice User to Wix Contacts
--------------------------------
Before any synchronization can take place, a link between a SuperOffice User and a Wix Contacts must be established.

A SuperOffice User will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
   * - personEmail
     - info.emails

Once a link between a SuperOffice User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Wix Contacts Property
     - Wix Data Type

