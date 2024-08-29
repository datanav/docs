===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-08-29 10:36:33

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer person to  Contacts
---------------------------------
Every Wave Customer person will be synchronized with a  Contacts.

Once a link between a Wave Customer person and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer person and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer person Property
     -  Contacts Property
     -  Data Type


Wave Customer to  Contacts
--------------------------
Every Wave Customer will be synchronized with a  Contacts.

Once a link between a Wave Customer and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Contacts Property
     -  Data Type
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - Mobile
     - "string"
   * - shippingDetails.address.city
     - City
     - "string"
   * - shippingDetails.address.country.code
     - Country
     - "string"


Wave Vendor to  Contacts
------------------------
Every Wave Vendor will be synchronized with a  Contacts.

Once a link between a Wave Vendor and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Vendor and a  Contacts:

.. list-table::
   :header-rows: 1

   * - Wave Vendor Property
     -  Contacts Property
     -  Data Type
   * - address.city
     - City
     - "string"
   * - address.country.code
     - Country
     - "string"
   * - email
     - Email
     - "string"
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"
   * - mobile
     - Mobile
     - "string"
   * - phone
     - Phone
     - "string"

