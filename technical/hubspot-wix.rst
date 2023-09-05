=======================
HubSpot to Wix Dataflow
=======================

Generated: 2023-09-05 09:13:38

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to Wix Contacts
-------------------------------
Every HubSpot Contact will be synchronized with a Wix Contacts.

If a matching Wix Contacts already exists, the HubSpot Contact will be merged with the existing one.
If no matching Wix Contacts is found, a new Wix Contacts will be created.

A HubSpot Contact will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
   * - properties.email
     - info.emails

Once a link between a HubSpot Contact and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Contacts Property
     - Wix Data Type
   * - properties.email
     - info.emails
     - "string"
   * - properties.firstname
     - info.name.first
     - "string"
   * - properties.lastname
     - info.name.last
     - "string"
   * - properties.mobilephone
     - info.phones
     - "string"


HubSpot Contact to Wix Members
------------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a Wix Members must be established.

A HubSpot Contact will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
   * - properties.email
     - loginEmail

Once a link between a HubSpot Contact and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a Wix Members:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     - Wix Members Property
     - Wix Data Type
   * - properties.email
     - loginEmail
     - "string"


HubSpot Contactcompanyassociation to Wix Contacts
-------------------------------------------------
Every HubSpot Contactcompanyassociation will be synchronized with a Wix Contacts.

Once a link between a HubSpot Contactcompanyassociation and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contactcompanyassociation and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot Contactcompanyassociation Property
     - Wix Contacts Property
     - Wix Data Type


HubSpot User to Wix Contacts
----------------------------
Every HubSpot User will be synchronized with a Wix Contacts.

Once a link between a HubSpot User and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot User and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - HubSpot User Property
     - Wix Contacts Property
     - Wix Data Type

