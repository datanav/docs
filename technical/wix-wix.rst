=======================
Wix.com to Wix Dataflow
=======================

Generated: 2023-09-05 08:47:45

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Wix Members
-------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Wix Members must be established.

A Wix.com Contacts will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Members Property
   * - info.emails
     - loginEmail

Once a link between a Wix.com Contacts and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Wix Members Property
     - Wix Data Type
   * - info.emails
     - loginEmail
     - "string"


Wix.com Members to Wix Contacts
-------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Wix Contacts must be established.

A Wix.com Members will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Contacts Property
   * - loginEmail
     - info.emails

Once a link between a Wix.com Members and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Wix Contacts Property
     - Wix Data Type
   * - loginEmail
     - info.emails
     - "string"

