==============================
Wave Financial to Wix Dataflow
==============================

Generated: 2023-09-05 09:17:31

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to Wix Contacts
-----------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wix Contacts must be established.

A Wave Customer will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Contacts Property
   * - email
     - info.emails
   * - email
     - primaryInfo.email

Once a link between a Wave Customer and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - mobile
     - info.phones
     - "string"


Wave Customer to Wix Members
----------------------------
Before any synchronization can take place, a link between a Wave Customer and a Wix Members must be established.

A Wave Customer will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Wave Customer and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"


Wave Vendor to Wix Contacts
---------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wix Contacts must be established.

A Wave Vendor will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Contacts Property
   * - email
     - info.emails
   * - email
     - primaryInfo.email

Once a link between a Wave Vendor and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Contacts Property
     - Wix Data Type
   * - email
     - info.emails
     - "string"
   * - firstName
     - info.name.first
     - "string"
   * - lastName
     - info.name.last
     - "string"
   * - mobile
     - info.phones
     - "string"


Wave Vendor to Wix Members
--------------------------
Before any synchronization can take place, a link between a Wave Vendor and a Wix Members must be established.

A Wave Vendor will merge with a Wix Members if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Members Property
   * - email
     - loginEmail

Once a link between a Wave Vendor and a Wix Members is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a Wix Members:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     - Wix Members Property
     - Wix Data Type
   * - email
     - loginEmail
     - "string"

