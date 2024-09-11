==========================
Wave to CRMOffice Dataflow
==========================

Generated: 2024-09-11 07:53:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to Crmoffice Contacts
------------------------------------------
Every Wave Customer person will be synchronized with a Crmoffice Contacts.

Once a link between a Wave Customer person and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - mobile
     - mobilePhone
     - "string"
   * - phone
     - directPhone
     - "string"
   * - shippingDetails.phone
     - directPhone
     - "string"


Wave Product to Crmoffice Companies
-----------------------------------
Every Wave Product will be synchronized with a Crmoffice Companies.

Once a link between a Wave Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Wave Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Wave Customer to CRMOffice Contacts
-----------------------------------
Every Wave Customer will be synchronized with a CRMOffice Contacts.

Once a link between a Wave Customer and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - mobile
     - mobilePhone
     - "string"


Wave Vendor to CRMOffice Contacts
---------------------------------
Every Wave Vendor will be synchronized with a CRMOffice Contacts.

Once a link between a Wave Vendor and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - firstName
     - givenName
     - "string"
   * - lastName
     - familyName
     - "string"
   * - mobile
     - mobilePhone
     - "string"
   * - phone
     - directPhone
     - "string"

