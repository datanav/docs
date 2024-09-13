============================
Wix.com to Youtrack Dataflow
============================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Youtrack. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Youtrack Users
----------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Youtrack Users must be established.

A Wix.com Contacts will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Youtrack Users Property
   * - primaryInfo.email
     - profile.email.email

Once a link between a Wix.com Contacts and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - info.name.first
     - name
     - "string"
   * - info.name.last
     - name
     - "string"
   * - primaryInfo.email
     - profile.email
     - "string"
   * - primaryInfo.email
     - profile.email.email
     - "string"


Wix.com Members to Youtrack Users
---------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Youtrack Users must be established.

A Wix.com Members will merge with a Youtrack Users if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Youtrack Users Property
   * - loginEmail
     - profile.email.email

Once a link between a Wix.com Members and a Youtrack Users is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Youtrack Users:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Youtrack Users Property
     - Youtrack Data Type
   * - loginEmail
     - profile.email
     - "string"
   * - loginEmail
     - profile.email.email
     - "string"

