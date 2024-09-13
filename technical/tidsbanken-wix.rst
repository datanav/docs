==========================
Tidsbanken to Wix Dataflow
==========================

Generated: 2024-09-13 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Wix Contacts
---------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Wix Contacts must be established.

A Tidsbanken Ansatt will merge with a Wix Contacts if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wix Contacts Property
   * - Epost
     - primaryInfo.email

Once a link between a Tidsbanken Ansatt and a Wix Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Wix Contacts:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Wix Contacts Property
     - Wix Data Type
   * - Etternavn
     - info.name.last
     - "string"
   * - Fornavn
     - info.name.first
     - "string"

