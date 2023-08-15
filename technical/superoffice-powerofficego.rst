=====================================
SuperOffice to PowerOfficeGo Dataflow
=====================================

Generated: 2023-08-15 10:04:57

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to PowerOfficeGo. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Quoteline to PowerOfficeGo Outgoinginvoices
-------------------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Outgoinginvoices.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Outgoinginvoices:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Outgoinginvoices Property
     - PowerOfficeGo Data Type
   * - QuoteAlternativeId
     - OrderNo
     - "string"
   * - TotalPrice
     - NetAmount
     - "string"


SuperOffice Ownercontactlink to PowerOfficeGo Departments
---------------------------------------------------------
Every SuperOffice Ownercontactlink will be synchronized with a PowerOfficeGo Departments.

Once a link between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ownercontactlink and a PowerOfficeGo Departments:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ownercontactlink Property
     - PowerOfficeGo Departments Property
     - PowerOfficeGo Data Type
   * - name
     - Name
     - "string"


SuperOffice Product to PowerOfficeGo Vatcodes
---------------------------------------------
Every SuperOffice Product will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Product and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Product and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Product Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice Quotealternative to PowerOfficeGo Vatcodes
------------------------------------------------------
Every SuperOffice Quotealternative will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quotealternative and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quotealternative Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice Quoteline to PowerOfficeGo Vatcodes
-----------------------------------------------
Every SuperOffice Quoteline will be synchronized with a PowerOfficeGo Vatcodes.

Once a link between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Quoteline and a PowerOfficeGo Vatcodes:

.. list-table::
   :header-rows: 1

   * - SuperOffice Quoteline Property
     - PowerOfficeGo Vatcodes Property
     - PowerOfficeGo Data Type
   * - VAT
     - rate
     - "string"
   * - VATInfo
     - name
     - "string"


SuperOffice User to PowerOfficeGo Employees
-------------------------------------------
Every SuperOffice User will be synchronized with a PowerOfficeGo Employees.

Once a link between a SuperOffice User and a PowerOfficeGo Employees is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a PowerOfficeGo Employees:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - PowerOfficeGo Employees Property
     - PowerOfficeGo Data Type
   * - firstName
     - FirstName
     - "string"
   * - lastName
     - LastName
     - "string"

