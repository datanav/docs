==============================
Wix.com to Tidsbanken Dataflow
==============================

Generated: 2024-06-30 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Contacts to Tidsbanken Ansatt
-------------------------------------
Before any synchronization can take place, a link between a Wix.com Contacts and a Tidsbanken Ansatt must be established.

A Wix.com Contacts will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tidsbanken Ansatt Property
   * - primaryInfo.email
     - Epost

Once a link between a Wix.com Contacts and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Contacts and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Wix.com Contacts Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type
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


Wix.com Members to Tidsbanken Ansatt
------------------------------------
Before any synchronization can take place, a link between a Wix.com Members and a Tidsbanken Ansatt must be established.

A Wix.com Members will merge with a Tidsbanken Ansatt if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tidsbanken Ansatt Property
   * - loginEmail
     - Epost

Once a link between a Wix.com Members and a Tidsbanken Ansatt is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a Tidsbanken Ansatt:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - Tidsbanken Ansatt Property
     - Tidsbanken Data Type

