==================================
Powerofficego to Youtrack Dataflow
==================================

Generated: 2024-06-29 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to Youtrack Users
---------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a Youtrack Users must be established.

A Powerofficego Contactperson will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     - Youtrack Users Property
   * - emailAddress
     - profile.email.email

Once a link between a Powerofficego Contactperson and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
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


Powerofficego Customers person to Youtrack Users
------------------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a Youtrack Users must be established.

A Powerofficego Customers person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     - Youtrack Users Property
   * - EmailAddress
     - profile.email.email

Once a link between a Powerofficego Customers person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
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

