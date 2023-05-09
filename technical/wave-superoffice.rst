======================================
Wave Financial to SuperOffice Dataflow
======================================

Generated: 2023-05-08 07:30:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to SuperOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to SuperOffice Contact
------------------------------------
Every Wave Customer will be synchronized with a SuperOffice Contact.

Once a link between a Wave Customer and a SuperOffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a SuperOffice Contact:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - SuperOffice Contact Property
     - SuperOffice Data Type
   * - address.addressLine1
     - Address.Postal.Address1
     - "string"
   * - address.addressLine2
     - Address.Postal.Address2
     - "string"
   * - address.city
     - Address.Postal.City
     - "string"
   * - address.country.code
     - Country.CountryId
     - "integer"
   * - address.postalCode
     - Address.Postal.Zipcode
     - "string"
   * - id
     - ContactId
     - "integer"
   * - name
     - Name
     - "string"
   * - phone
     - Phones.Value
     - "string"
   * - website
     - Domains
     - "list"
   * - website
     - Urls.Value
     - "string"

