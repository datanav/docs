===================================
PowerOffice GO to Youtrack Dataflow
===================================

Generated: 2024-09-15 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice GO Contactperson to Youtrack Users
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Contactperson and a Youtrack Users must be established.

A PowerOffice GO Contactperson will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Youtrack Users Property
   * - emailAddress
     - profile.email.email

Once a link between a PowerOffice GO Contactperson and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Contactperson and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Contactperson Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - emailAddress
     - profile.email
     - "string"
   * - emailAddress
     - profile.email.email
     - "string"
   * - residenceCountryCode
     - userType.id
     - "string"


PowerOffice GO Customers person to Youtrack Users
-------------------------------------------------
Before any synchronization can take place, a link between a PowerOffice GO Customers person and a Youtrack Users must be established.

A PowerOffice GO Customers person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Youtrack Users Property
   * - EmailAddress
     - profile.email.email

Once a link between a PowerOffice GO Customers person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - EmailAddress
     - profile.email
     - "string"
   * - MailAddress.CountryCode
     - userType.id
     - "string"


PowerOffice GO Customers to Youtrack Groups
-------------------------------------------
Every PowerOffice GO Customers will be synchronized with a Youtrack Groups.

Once a link between a PowerOffice GO Customers and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Customers and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Customers Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Departments to Youtrack Groups
---------------------------------------------
Every PowerOffice GO Departments will be synchronized with a Youtrack Groups.

Once a link between a PowerOffice GO Departments and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Departments and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Departments Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


PowerOffice GO Projectactivity to Youtrack Hubprojects
------------------------------------------------------
Every PowerOffice GO Projectactivity will be synchronized with a Youtrack Hubprojects.

Once a link between a PowerOffice GO Projectactivity and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projectactivity and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projectactivity Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type


PowerOffice GO Projects to Youtrack Hubprojects
-----------------------------------------------
Every PowerOffice GO Projects will be synchronized with a Youtrack Hubprojects.

Once a link between a PowerOffice GO Projects and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Projects and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Projects Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type


PowerOffice GO Timetrackingactivity to Youtrack Hubprojects
-----------------------------------------------------------
Every PowerOffice GO Timetrackingactivity will be synchronized with a Youtrack Hubprojects.

Once a link between a PowerOffice GO Timetrackingactivity and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice GO Timetrackingactivity and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - PowerOffice GO Timetrackingactivity Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type

