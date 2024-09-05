==========================
Wix.com to Trello Dataflow
==========================

Generated: 2024-09-05 12:09:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Trello. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Members
----------------------------
Every Wix.com Contacts will be synchronized with a  Members.

Once a link between a Wix.com Contacts and a  Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Members:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Members Property
     -  Data Type
   * - primaryInfo.email
     - email
     - "string"

