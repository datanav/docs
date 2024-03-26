==================================
Powerofficego to Youtrack Dataflow
==================================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Powerofficego Contactperson to  Users
-------------------------------------
Before any synchronization can take place, a link between a Powerofficego Contactperson and a  Users must be established.

A Powerofficego Contactperson will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Users Property
   * - emailAddress
     - profile.email.email

Once a link between a Powerofficego Contactperson and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Contactperson and a  Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Contactperson Property
     -  Users Property
     -  Data Type
   * - emailAddress
     - profile.email
     - "string"
   * - emailAddress
     - profile.email.email
     - "string"
   * - residenceCountryCode
     - userType.id
     - "string"


Powerofficego Customers person to  Users
----------------------------------------
Before any synchronization can take place, a link between a Powerofficego Customers person and a  Users must be established.

A Powerofficego Customers person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Users Property
   * - EmailAddress
     - profile.email.email

Once a link between a Powerofficego Customers person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers person and a  Users:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers person Property
     -  Users Property
     -  Data Type
   * - EmailAddress
     - profile.email
     - "string"
   * - MailAddress.CountryCode
     - userType.id
     - "string"


Powerofficego Customers to  Groups
----------------------------------
Every Powerofficego Customers will be synchronized with a  Groups.

Once a link between a Powerofficego Customers and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a  Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     -  Groups Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to  Groups
------------------------------------
Every Powerofficego Departments will be synchronized with a  Groups.

Once a link between a Powerofficego Departments and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a  Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     -  Groups Property
     -  Data Type
   * - Name
     - name
     - "string"


Powerofficego Projects to  Hubprojects
--------------------------------------
Every Powerofficego Projects will be synchronized with a  Hubprojects.

Once a link between a Powerofficego Projects and a  Hubprojects is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Projects and a  Hubprojects:

.. list-table::
   :header-rows: 1

   * - Powerofficego Projects Property
     -  Hubprojects Property
     -  Data Type

