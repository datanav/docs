=============================
Crmoffice to Hubspot Dataflow
=============================

Generated: 2024-09-10 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Contacts to Hubspot Contact
-------------------------------------
Every Crmoffice Contacts will be synchronized with a Hubspot Contact.

Once a link between a Crmoffice Contacts and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Contacts and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Crmoffice Contacts Property
     - Hubspot Contact Property
     - Hubspot Data Type
   * - directPhone
     - properties.phone
     - "string"
   * - familyName
     - properties.lastname
     - "string"
   * - givenName
     - properties.firstname
     - "string"
   * - mobilePhone
     - properties.mobilephone
     - "string"

