=============================
CRMOffice to HubSpot Dataflow
=============================

Generated: 2024-09-11 08:07:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Contacts to Hubspot Contact
-------------------------------------
Every CRMOffice Contacts will be synchronized with a Hubspot Contact.

Once a link between a CRMOffice Contacts and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Contacts and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - CRMOffice Contacts Property
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

