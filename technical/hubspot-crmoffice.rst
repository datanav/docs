=============================
HubSpot to Crmoffice Dataflow
=============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Crmoffice Contacts
-------------------------------------
Every HubSpot Contact will be synchronized with a Crmoffice Contacts.

Once a link between a HubSpot Contact and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type
   * - properties.firstname
     - givenName
     - "string"
   * - properties.lastname
     - familyName
     - "string"
   * - properties.mobilephone
     - mobilePhone
     - "string"
   * - properties.phone
     - directPhone
     - "string"


HubSpot Contactcompanyassociation to Crmoffice Contacts
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Crmoffice Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type


HubSpot Product to Crmoffice Companies
--------------------------------------
Every HubSpot Product will be synchronized with a Crmoffice Companies.

Once a link between a HubSpot Product and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - Crmoffice Companies Property
     - Crmoffice Data Type


HubSpot User to Crmoffice Contacts
----------------------------------
Every HubSpot User will be synchronized with a Crmoffice Contacts.

Once a link between a HubSpot User and a Crmoffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Crmoffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Crmoffice Contacts Property
     - Crmoffice Data Type

