============================
Businesscentral to  Dataflow
============================

Generated: 2023-11-30 12:43:05

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contact person to  Contactperson
------------------------------------------------
Every Businesscentral Contact person will be synchronized with a  Contactperson.

Once a link between a Businesscentral Contact person and a  Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contact person and a  Contactperson:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contact person Property
     -  Contactperson Property
     -  Data Type
   * - addressLine1
     - address1
     - "string"
   * - addressLine2
     - address2
     - "string"
   * - city
     - city
     - "string"
   * - country
     - residenceCountryCode
     - "string"
   * - email
     - emailAddress
     - "string"
   * - id
     - id
     - "integer"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - zipCode
     - "string"

