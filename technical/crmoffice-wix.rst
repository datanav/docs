=========================
CRMOffice to Wix Dataflow
=========================

Generated: 2024-09-11 07:45:31

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Wix Contacts
----------------------------------
Every Crmoffice Contacts will be synchronized with a Wix Contacts.

Once a link between a Crmoffice Contacts and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Wix Contacts Property
     - Wix Data Type
   * - directPhone
     - primaryInfo.phone
     - "string"
   * - familyName
     - info.name.last
     - "string"
   * - givenName
     - info.name.first
     - "string"

