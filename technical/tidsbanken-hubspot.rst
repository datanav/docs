==============================
Tidsbanken to Hubspot Dataflow
==============================

Generated: 2024-03-26 14:23:23

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tidsbanken to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tidsbanken Ansatt to Hubspot Contact
------------------------------------
Before any synchronization can take place, a link between a Tidsbanken Ansatt and a Hubspot Contact must be established.

A Tidsbanken Ansatt will merge with a Hubspot Contact if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Hubspot Contact Property
   * - Epost
     - properties.email

Once a link between a Tidsbanken Ansatt and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tidsbanken Ansatt and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - Tidsbanken Ansatt Property
     - Hubspot Contact Property
     - Hubspot Data Type

