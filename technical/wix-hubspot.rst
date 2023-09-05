===========================
Wix.com to HubSpot Dataflow
===========================

Generated: 2023-09-05 08:43:09

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to HubSpot Contact
-----------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a HubSpot Contact must be established.

A Wix.com Contacts will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
   * - info.emails
     - properties.email

Once a link between a Wix.com Contacts and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - info.emails
     - properties.email
     - "string"
   * - info.phones
     - properties.mobilephone
     - "string"


Wix.com Members to HubSpot Contact
----------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a HubSpot Contact must be established.

A Wix.com Members will merge with a HubSpot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
   * - loginEmail
     - properties.email

Once a link between a Wix.com Members and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - loginEmail
     - properties.email
     - "string"

