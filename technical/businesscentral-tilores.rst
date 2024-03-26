===================================
Businesscentral to Tilores Dataflow
===================================

Generated: 2024-03-26 14:24:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Businesscentral to Tilores. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Businesscentral Contacts person to  Human
-----------------------------------------
Every Businesscentral Contacts person will be synchronized with a  Human.

Once a link between a Businesscentral Contacts person and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Contacts person and a  Human:

.. list-table::
   :header-rows: 1

   * - Businesscentral Contacts person Property
     -  Human Property
     -  Data Type
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - id
     - id
     - "string"
   * - mobilePhoneNumber
     - phoneNumber
     - "string"
   * - phoneNumber
     - phoneNumber
     - "string"
   * - postalCode
     - postalCode
     - "string"


Businesscentral Employees to  Human
-----------------------------------
Every Businesscentral Employees will be synchronized with a  Human.

Once a link between a Businesscentral Employees and a  Human is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Businesscentral Employees and a  Human:

.. list-table::
   :header-rows: 1

   * - Businesscentral Employees Property
     -  Human Property
     -  Data Type
   * - birthDate
     - dateOfBirth
     - "string"
   * - city
     - city
     - "string"
   * - email
     - email
     - "string"
   * - givenName
     - firstName
     - "string"
   * - id
     - id
     - "string"
   * - personalEmail
     - email
     - "string"
   * - postalCode
     - postalCode
     - "string"
   * - surname
     - lastName
     - "string"

