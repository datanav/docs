==================================
Business Nxt to CRMOffice Dataflow
==================================

Generated: 2024-09-24 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to CRMOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Product to CRMOffice Companies
-------------------------------------------
Every Business Nxt Product will be synchronized with a CRMOffice Companies.

Once a link between a Business Nxt Product and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Product and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Product Property
     - CRMOffice Companies Property
     - CRMOffice Data Type


Business Nxt Address to CRMOffice Companies
-------------------------------------------
Every Business Nxt Address will be synchronized with a CRMOffice Companies.

Once a link between a Business Nxt Address and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
     - CRMOffice Companies Property
     - CRMOffice Data Type
   * - addressNo
     - id
     - "string"
   * - countryNo
     - postAddress.country
     - "string"
   * - countryNo
     - visitAddress.country
     - "string"
   * - postCode
     - postAddress.postCode
     - "string"
   * - postCode
     - visitAddress.postCode
     - "string"
   * - postalArea
     - postAddress.postalArea
     - "string"
   * - postalArea
     - visitAddress.postalArea
     - "string"


Business Nxt Company to CRMOffice Companies
-------------------------------------------
Every Business Nxt Company will be synchronized with a CRMOffice Companies.

Once a link between a Business Nxt Company and a CRMOffice Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a CRMOffice Companies:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - CRMOffice Companies Property
     - CRMOffice Data Type
   * - companyNo
     - id
     - "string"

