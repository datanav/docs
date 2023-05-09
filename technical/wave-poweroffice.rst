======================================
Wave Financial to PowerOffice Dataflow
======================================

Generated: 2023-05-01 16:25:05

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Business to PowerOffice Address
------------------------------------
Every Wave Business will be synchronized with a PowerOffice Address.

Once a link between a Wave Business and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Business and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Wave Business Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - address.addressLine1
     - Address1
     - "string"
   * - address.addressLine2
     - Address2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country
     - CountryCode
     - "string"
   * - address.postalCode
     - ZipCode
     - "string"


Wave Customer to PowerOffice Address
------------------------------------
Every Wave Customer will be synchronized with a PowerOffice Address.

Once a link between a Wave Customer and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - PowerOffice Address Property
     - PowerOffice Data Type
   * - address.addressLine1
     - Address1
     - "string"
   * - address.addressLine2
     - Address2
     - "string"
   * - address.city
     - City
     - "string"
   * - address.country.code
     - CountryCode
     - "string"
   * - address.postalCode
     - ZipCode
     - "string"

