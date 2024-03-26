====================
HubSpot to  Dataflow
====================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Contact to  Ansatt
--------------------------
Before any synchronization can take place, a link between a HubSpot Contact and a  Ansatt must be established.

A HubSpot Contact will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Ansatt Property
   * - properties.email
     - Epost

Once a link between a HubSpot Contact and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Contact and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - HubSpot Contact Property
     -  Ansatt Property
     -  Data Type
   * - id
     - Id
     - "integer"
   * - properties.address
     - Adresse
     - "string"
   * - properties.city
     - Poststed
     - "string"
   * - properties.date_of_birth
     - Fodt
     - "string"
   * - properties.firstname
     - Fornavn
     - "string"
   * - properties.lastname
     - Etternavn
     - "string"
   * - properties.mobilephone
     - Mobil
     - "string"
   * - properties.zip
     - Postnummer
     - "string"

