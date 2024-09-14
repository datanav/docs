============================
WebCRM to CRMOffice Dataflow
============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Products to CRMOffice Companies
--------------------------------------
Every WebCRM Products will be synchronized with a CRMOffice Companies.

Once a link between a WebCRM Products and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Products and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - WebCRM Products Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


WebCRM Users to CRMOffice Contacts
----------------------------------
Every WebCRM Users will be synchronized with a CRMOffice Contacts.

Once a link between a WebCRM Users and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Users and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Users Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - UserMobilePhone
     - mobilePhone
     - "string"
   * - UserTelephone
     - directPhone
     - "string"


WebCRM Persons to CRMOffice Contacts
------------------------------------
Every WebCRM Persons will be synchronized with a CRMOffice Contacts.

Once a link between a WebCRM Persons and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Persons and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - WebCRM Persons Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
   * - PersonDirectPhone
     - directPhone
     - "string"
   * - PersonFirstName
     - givenName
     - "string"
   * - PersonLastName
     - familyName
     - "string"
   * - PersonMobilePhone
     - mobilePhone
     - "string"

