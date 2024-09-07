===============================
Crmoffice to Crmoffice Dataflow
===============================

Generated: 2024-09-07 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Crmoffice to Crmoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Crmoffice Companies to Crmoffice Companies
------------------------------------------
Before any synchronization can take place, a link between a Crmoffice Companies and a Crmoffice Companies must be established.

A Crmoffice Companies will merge with a Crmoffice Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Crmoffice Companies Property
     - Crmoffice Companies Property
   * - orgNr
     - orgNr

Once a link between a Crmoffice Companies and a Crmoffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Crmoffice Companies and a Crmoffice Companies:

.. list-table::
   :header-rows: 1

   * - Crmoffice Companies Property
     - Crmoffice Companies Property
     - Crmoffice Data Type
   * - id
     - id
     - "string"
   * - postAddress.country
     - visitAddress.country
     - "string"
   * - postAddress.postCode
     - visitAddress.postCode
     - "string"
   * - postAddress.postalArea
     - visitAddress.postalArea
     - "string"
   * - postAddress.streetAddress
     - visitAddress.streetAddress
     - "string"
   * - visitAddress.country
     - postAddress.country
     - "string"
   * - visitAddress.postCode
     - postAddress.postCode
     - "string"
   * - visitAddress.postalArea
     - postAddress.postalArea
     - "string"
   * - visitAddress.streetAddress
     - postAddress.streetAddress
     - "string"

