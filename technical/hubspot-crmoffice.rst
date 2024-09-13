=============================
HubSpot to CRMOffice Dataflow
=============================

Generated: 2024-09-13 00:00:03

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to CRMOffice Contacts
-------------------------------------
Every HubSpot Contact will be synchronized with a CRMOffice Contacts.

Once a link between a HubSpot Contact and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type
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


HubSpot Contactcompanyassociation to CRMOffice Contacts
-------------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a CRMOffice Contacts.

Once a link between a HubSpot Contactcompanyassociation and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type


HubSpot Product to CRMOffice Companies
--------------------------------------
Every HubSpot Product will be synchronized with a CRMOffice Companies.

Once a link between a HubSpot Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - HubSpot Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


HubSpot User to CRMOffice Contacts
----------------------------------
Every HubSpot User will be synchronized with a CRMOffice Contacts.

Once a link between a HubSpot User and a CRMOffice Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a CRMOffice Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - CRMOffice Contacts Property
     - CRMOffice Data Type

