==================================
PowerOfficeGO to Youtrack Dataflow
==================================

Generated: 2024-09-11 09:30:21

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOfficeGO to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOfficeGO Contactperson to Youtrack Users
---------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Contactperson and a Youtrack Users must be established.

A PowerOfficeGO Contactperson will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
     - Youtrack Users Property
   * - emailAddress
     - profile.email.email

Once a link between a PowerOfficeGO Contactperson and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Contactperson and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Contactperson Property
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


PowerOfficeGO Customers person to Youtrack Users
------------------------------------------------
Before any synchronization can take place, a link between a PowerOfficeGO Customers person and a Youtrack Users must be established.

A PowerOfficeGO Customers person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Youtrack Users Property
   * - EmailAddress
     - profile.email.email

Once a link between a PowerOfficeGO Customers person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - EmailAddress
     - profile.email
     - "string"
   * - MailAddress.CountryCode
     - userType.id
     - "string"


PowerOfficeGO Customers to Youtrack Groups
------------------------------------------
Every PowerOfficeGO Customers will be synchronized with a Youtrack Groups.

Once a link between a PowerOfficeGO Customers and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Customers and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Customers Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


PowerOfficeGO Departments to Youtrack Groups
--------------------------------------------
Every PowerOfficeGO Departments will be synchronized with a Youtrack Groups.

Once a link between a PowerOfficeGO Departments and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Departments and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Departments Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


PowerOfficeGO Projects to Youtrack Hubprojects
----------------------------------------------
Every PowerOfficeGO Projects will be synchronized with a Youtrack Hubprojects.

Once a link between a PowerOfficeGO Projects and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOfficeGO Projects and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - PowerOfficeGO Projects Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type

