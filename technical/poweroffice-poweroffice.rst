===================================
Poweroffice to PowerOffice Dataflow
===================================

Generated: 2023-06-27 05:12:36

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Customer to PowerOffice Contactperson
-------------------------------------------------
Every Poweroffice Customer will be synchronized with a PowerOffice Contactperson.

Once a link between a Poweroffice Customer and a PowerOffice Contactperson is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Customer and a PowerOffice Contactperson:

.. list-table::
   :header-rows: 1

   * - Poweroffice Customer Property
     - PowerOffice Contactperson Property
     - PowerOffice Data Type
   * - LastName
     - lastName
     - "string"
   * - dateOfBirth
     - dateOfBirth
     - "string"
   * - emailAddress
     - emailAddress
     - "string"
   * - firstName
     - firstName
     - "string"
   * - id
     - id
     - "integer"
   * - lastChanged
     - lastChanged
     - "string"
   * - mailAddress.city
     - city
     - "string"
   * - mailAddress.countryCode
     - residenceCountryCode
     - "string"
   * - mailAddress.zipCode
     - zipCode
     - "string"
   * - streetAddresses.city
     - city
     - "string"
   * - streetAddresses.countryCode
     - residenceCountryCode
     - "string"
   * - streetAddresses.zipCode
     - zipCode
     - "string"

