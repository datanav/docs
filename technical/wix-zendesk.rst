===========================
Wix.com to Zendesk Dataflow
===========================

Generated: 2024-03-26 14:14:24

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Zendesk. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Users
--------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Users must be established.

A Wix.com Contacts will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Users Property
   * - primaryInfo.email
     - email

Once a link between a Wix.com Contacts and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Users Property
     -  Data Type
   * - info.emails
     - email
     - "string"
   * - info.name.first
     - name
     - "string"
   * - info.name.last
     - name
     - "string"
   * - primaryInfo.email
     - email
     - "string"


Wix.com Members to  Users
-------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Users must be established.

A Wix.com Members will merge with a  Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Users Property
   * - loginEmail
     - email

Once a link between a Wix.com Members and a  Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Users Property
     -  Data Type
   * - loginEmail
     - email
     - "string"

