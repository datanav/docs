================================
SuperOffice to Youtrack Dataflow
================================

Generated: 2024-07-01 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to Youtrack Users
------------------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a Youtrack Users must be established.

A SuperOffice Person will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Youtrack Users Property
   * - Emails.Value
     - profile.email.email

Once a link between a SuperOffice Person and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - Emails.Value
     - profile.email
     - "string"
   * - Emails.Value
     - profile.email.email
     - "string"


SuperOffice Contact to Youtrack Groups
--------------------------------------
Every SuperOffice Contact will be synchronized with a Youtrack Groups.

Once a link between a SuperOffice Contact and a Youtrack Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a Youtrack Groups:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     - Youtrack Groups Property
     - Youtrack Data Type
   * - Name
     - name
     - "string"


SuperOffice Ticket to Youtrack Issues
-------------------------------------
Every SuperOffice Ticket will be synchronized with a Youtrack Issues.

Once a link between a SuperOffice Ticket and a Youtrack Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a Youtrack Issues:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     - Youtrack Issues Property
     - Youtrack Data Type
   * - OwnedBy.AssociateId
     - reporter.id
     - "string"


SuperOffice User to Youtrack Users
----------------------------------
Every SuperOffice User will be synchronized with a Youtrack Users.

If a matching Youtrack Users already exists, the SuperOffice User will be merged with the existing one.
If no matching Youtrack Users is found, a new Youtrack Users will be created.

A SuperOffice User will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Youtrack Users Property
   * - personEmail
     - profile.email.email

Once a link between a SuperOffice User and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - personEmail
     - profile.email
     - "string"
   * - personEmail
     - profile.email.email
     - "string"

