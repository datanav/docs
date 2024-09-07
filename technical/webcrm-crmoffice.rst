============================
Webcrm to Crmoffice Dataflow
============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Webcrm to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Webcrm Products to Crmoffice Companies
--------------------------------------
Every Webcrm Products will be synchronized with a Crmoffice Companies.

Once a link between a Webcrm Products and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Products and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Webcrm Products Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


Webcrm Users to Crmoffice Contacts
----------------------------------
Every Webcrm Users will be synchronized with a Crmoffice Contacts.

Once a link between a Webcrm Users and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Users and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Webcrm Users Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - UserMobilePhone
     - mobilePhone
     - "string"
   * - UserTelephone
     - directPhone
     - "string"


Webcrm Persons to Crmoffice Contacts
------------------------------------
Every Webcrm Persons will be synchronized with a Crmoffice Contacts.

Once a link between a Webcrm Persons and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Webcrm Persons and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - Webcrm Persons Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
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

