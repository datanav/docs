===================================
SuperOffice to PowerOffice Dataflow
===================================

Generated: 2023-06-23 07:30:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Listproductcategoryitems to PowerOffice Productgroup
----------------------------------------------------------------
Before any synchronization can take place, a link between a SuperOffice Listproductcategoryitems and a PowerOffice Productgroup must be established.

A new PowerOffice Productgroup will be created from a SuperOffice Listproductcategoryitems if it is connected to a SuperOffice Product that is synchronized into PowerOffice.

Once a link between a SuperOffice Listproductcategoryitems and a PowerOffice Productgroup is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Listproductcategoryitems and a PowerOffice Productgroup:

.. list-table::
   :header-rows: 1

   * - SuperOffice Listproductcategoryitems Property
     - PowerOffice Productgroup Property
     - PowerOffice Data Type

