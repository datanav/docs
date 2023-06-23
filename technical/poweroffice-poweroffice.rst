===================================
Poweroffice to PowerOffice Dataflow
===================================

Generated: 2023-06-23 07:30:52

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Poweroffice to PowerOffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Poweroffice Supplier to PowerOffice Address
-------------------------------------------
Before any synchronization can take place, a link between a Poweroffice Supplier and a PowerOffice Address must be established.

A Poweroffice Supplier will merge with a PowerOffice Address if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - PowerOffice Address Property
   * - MailAddress.Id
     - id

Once a link between a Poweroffice Supplier and a PowerOffice Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Poweroffice Supplier and a PowerOffice Address:

.. list-table::
   :header-rows: 1

   * - Poweroffice Supplier Property
     - PowerOffice Address Property
     - PowerOffice Data Type

