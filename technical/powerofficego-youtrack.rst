===================================
PowerOffice GO to Youtrack Dataflow
===================================

Generated: 2024-09-11 07:51:19

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from PowerOffice GO to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

PowerOffice Contactperson to Youtrack Users
-------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Contactperson and a Youtrack Users must be established.

A PowerOffice Contactperson will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
     - Youtrack Users Property
   * - emailAddress
     - profile.email.email

Once a link between a PowerOffice Contactperson and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Contactperson and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice Contactperson Property
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


PowerOffice Customers person to Youtrack Users
----------------------------------------------
Before any synchronization can take place, a link between a PowerOffice Customers person and a Youtrack Users must be established.

A PowerOffice Customers person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Youtrack Users Property
   * - EmailAddress
     - profile.email.email

Once a link between a PowerOffice Customers person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a PowerOffice Customers person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - PowerOffice Customers person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - EmailAddress
     - profile.email
     - "string"
   * - MailAddress.CountryCode
     - userType.id
     - "string"


Powerofficego Customers to Youtrack Groups
------------------------------------------
Every Powerofficego Customers will be synchronized with a Youtrack Groups.

Once a link between a Powerofficego Customers and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to Youtrack Groups
--------------------------------------------
Every Powerofficego Departments will be synchronized with a Youtrack Groups.

Once a link between a Powerofficego Departments and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Projects to Youtrack Hubprojects
----------------------------------------------
Every Powerofficego Projects will be synchronized with a Youtrack Hubprojects.

Once a link between a Powerofficego Projects and a Youtrack Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a Youtrack Hubprojects:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     - Youtrack Hubprojects Property
     - Youtrack Data Type

