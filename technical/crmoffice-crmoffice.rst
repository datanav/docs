===============================
CRMOffice to CRMOffice Dataflow
===============================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from CRMOffice to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

CRMOffice Companies to CRMOffice Companies
------------------------------------------
Before any synchronization can take place, a link between a CRMOffice Companies and a CRMOffice Companies must be established.

A CRMOffice Companies will merge with a CRMOffice Companies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - CRMOffice Companies Property
   * - orgNr
     - orgNr

Once a link between a CRMOffice Companies and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a CRMOffice Companies and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - CRMOffice Companies Property
     - CRMOffice Companies Property
     - CRMOffice Data Type
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

