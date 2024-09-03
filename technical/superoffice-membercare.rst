==================================
SuperOffice to Membercare Dataflow
==================================

Generated: 2024-09-03 09:02:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Contact to  Companies
---------------------------------
Every SuperOffice Contact will be synchronized with a  Companies.

Once a link between a SuperOffice Contact and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Companies:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Companies Property
     -  Data Type
   * - Name
     - companyName
     - "string"
   * - Urls.Value
     - url
     - "string"


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

