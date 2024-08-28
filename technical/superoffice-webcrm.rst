========================
SuperOffice to  Dataflow
========================

Generated: 2024-08-28 10:47:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Organisations
-------------------------------------
Every SuperOffice Contact will be synchronized with a  Organisations.

Once a link between a SuperOffice Contact and a  Organisations is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Organisations:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Organisations Property
     -  Data Type
   * - Address.Postal.Address1
     - OrganisationAddress
     - "string"
   * - Address.Postal.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Postal.City
     - OrganisationCity
     - "string"
   * - Address.Postal.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Postal.Zipcode
     - OrganisationPostCode
     - "string"
   * - Address.Street.Address1
     - OrganisationAddress
     - "string"
   * - Address.Street.Address1
     - OrganisationDeliveryAddress
     - "string"
   * - Address.Street.City
     - OrganisationCity
     - "string"
   * - Address.Street.City
     - OrganisationDeliveryCity
     - "string"
   * - Address.Street.Zipcode
     - OrganisationDeliveryPostCode
     - "string"
   * - Address.Street.Zipcode
     - OrganisationPostCode
     - "string"
   * - ContactId
     - OrganisationId
     - "string"
   * - Name
     - OrganisationName
     - "string"
   * - Phones.Value
     - OrganisationTelephone
     - "string"

