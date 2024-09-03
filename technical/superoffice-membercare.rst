==================================
SuperOffice to Membercare Dataflow
==================================

Generated: 2024-09-03 10:41:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to Membercare Companies
-------------------------------------------
Every SuperOffice Contact will be synchronized with a Membercare Companies.

Once a link between a SuperOffice Contact and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Name
     - companyName
     - "string"
   * - Urls.Value
     - url
     - "string"


SuperOffice Quotealternative to Membercare Invoices
---------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Quotealternative and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - Membercare Invoices Property
     - Membercare Data Type


SuperOffice Quoteline to Membercare Invoices
--------------------------------------------
Every SuperOffice Quoteline will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Quoteline and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - Membercare Invoices Property
     - Membercare Data Type


SuperOffice Sale to Membercare Invoices
---------------------------------------
Every SuperOffice Sale will be synchronized with a Membercare Invoices.

Once a link between a SuperOffice Sale and a Membercare Invoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Sale and a Membercare Invoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Sale Property
     - Membercare Invoices Property
     - Membercare Data Type


SuperOffice Listcountryitems to Membercare Countries
----------------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Membercare Countries.

Once a link between a SuperOffice Listcountryitems and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Name
     - name
     - "string"
   * - ThreeLetterISOCountry
     - iso3Letter
     - "string"
   * - TwoLetterISOCountry
     - iso2Letter
     - "string"

