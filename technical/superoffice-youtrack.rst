========================
SuperOffice to  Dataflow
========================

Generated: 2024-03-26 13:42:34

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from SuperOffice to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

SuperOffice Person to  Users
----------------------------
Before any synchronization can take place, a link between a SuperOffice Person and a  Users must be established.

A SuperOffice Person will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
   * - Emails.Value
     - profile.email.email

Once a link between a SuperOffice Person and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Person and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice Person Property
     -  Users Property
     -  Data Type
   * - Emails.Value
     - profile.email
     - "string"
   * - Emails.Value
     - profile.email.email
     - "string"


SuperOffice Contact to  Groups
------------------------------
Every SuperOffice Contact will be synchronized with a  Groups.

Once a link between a SuperOffice Contact and a  Groups is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Contact and a  Groups:

.. list-table::
   :header-rows: 1

   * - SuperOffice Contact Property
     -  Groups Property
     -  Data Type
   * - Name
     - name
     - "string"


SuperOffice Ticket to  Issues
-----------------------------
Every SuperOffice Ticket will be synchronized with a  Issues.

Once a link between a SuperOffice Ticket and a  Issues is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice Ticket and a  Issues:

.. list-table::
   :header-rows: 1

   * - SuperOffice Ticket Property
     -  Issues Property
     -  Data Type
   * - OwnedBy.AssociateId
     - reporter.id
     - "string"


SuperOffice User to  Users
--------------------------
Every SuperOffice User will be synchronized with a  Users.

If a matching  Users already exists, the SuperOffice User will be merged with the existing one.
If no matching  Users is found, a new  Users will be created.

A SuperOffice User will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
   * - personEmail
     - profile.email.email

Once a link between a SuperOffice User and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a SuperOffice User and a  Users:

.. list-table::
   :header-rows: 1

   * - SuperOffice User Property
     -  Users Property
     -  Data Type
   * - personEmail
     - profile.email
     - "string"
   * - personEmail
     - profile.email.email
     - "string"

