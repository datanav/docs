==============================
ZohoCRM to Tidsbanken Dataflow
==============================

Generated: 2024-09-23 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Contact to Tidsbanken Kunde
-----------------------------------
Every ZohoCRM Contact will be synchronized with a Tidsbanken Kunde.

Once a link between a ZohoCRM Contact and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type

