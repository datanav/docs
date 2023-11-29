==========================
Powerofficego to  Dataflow
==========================

Generated: 2023-11-29 23:37:14

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Powerofficego to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

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


Powerofficego Currency to YouTrack Organizationroles
----------------------------------------------------
Every Powerofficego Currency will be synchronized with a YouTrack Organizationroles.

Once a link between a Powerofficego Currency and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Currency and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Powerofficego Currency Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type


Powerofficego Customers to YouTrack Groups
------------------------------------------
Every Powerofficego Customers will be synchronized with a YouTrack Groups.

Once a link between a Powerofficego Customers and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Customers and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Customers Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Departments to YouTrack Groups
--------------------------------------------
Every Powerofficego Departments will be synchronized with a YouTrack Groups.

Once a link between a Powerofficego Departments and a YouTrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Departments and a YouTrack Groups:

.. list-table::
   :header-rows: 1

   * - Powerofficego Departments Property
     - YouTrack Groups Property
     - YouTrack Data Type
   * - Name
     - name
     - "string"


Powerofficego Productgroup to YouTrack Organizationroles
--------------------------------------------------------
Every Powerofficego Productgroup will be synchronized with a YouTrack Organizationroles.

Once a link between a Powerofficego Productgroup and a YouTrack Organizationroles is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Powerofficego Productgroup and a YouTrack Organizationroles:

.. list-table::
   :header-rows: 1

   * - Powerofficego Productgroup Property
     - YouTrack Organizationroles Property
     - YouTrack Data Type

