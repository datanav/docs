===========================
SuperOffice to Ssb Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listcountryitems to Ssb Country
-------------------------------------------
Every SuperOffice Listcountryitems will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the SuperOffice Listcountryitems will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A SuperOffice Listcountryitems will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Ssb Country Property
   * - Name
     - name
   * - ThreeLetterISOCountry
     - code

Once a link between a SuperOffice Listcountryitems and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listcountryitems and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listcountryitems Property
     - Ssb Country Property
     - Ssb Data Type

