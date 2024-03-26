====================
Wix.com to  Dataflow
====================

Generated: 2024-03-26 00:00:04

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to  Ansatt
---------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a  Ansatt must be established.

A Wix.com Contacts will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Ansatt Property
   * - primaryInfo.email
     - Epost

Once a link between a Wix.com Contacts and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     -  Ansatt Property
     -  Data Type
   * - info.name.first
     - Etternavn
     - "string"
   * - info.name.first
     - Fornavn
     - "string"
   * - info.name.first
     - Navn
     - "string"
   * - info.name.last
     - Etternavn
     - "string"
   * - info.name.last
     - Fornavn
     - "string"
   * - info.name.last
     - Navn
     - "string"


Wix.com Members to  Ansatt
--------------------------
Before any synchronization can take place, a link between a Wix.com Members and a  Ansatt must be established.

A Wix.com Members will merge with a  Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Ansatt Property
   * - loginEmail
     - Epost

Once a link between a Wix.com Members and a  Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a  Ansatt:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     -  Ansatt Property
     -  Data Type

