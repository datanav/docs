==================================
Tidsbanken to Superoffice Dataflow
==================================

Generated: 2024-03-26 14:23:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Superoffice. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Superoffice Person
---------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Superoffice Person must be established.

A Tidsbanken Ansatt will merge with a Superoffice Person if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Superoffice Person Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Ansatt and a Superoffice Person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Superoffice Person:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Superoffice Person Property
     - Superoffice Data Type


Tidsbanken Kunde to Superoffice Contact
---------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Kunde and a Superoffice Contact must be established.

A Tidsbanken Kunde will merge with a Superoffice Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Superoffice Contact Property
   * - Epost
     - Emails.Value

Once a link between a Tidsbanken Kunde and a Superoffice Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Kunde and a Superoffice Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Kunde Property
     - Superoffice Contact Property
     - Superoffice Data Type

