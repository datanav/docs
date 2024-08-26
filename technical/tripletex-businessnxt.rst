======================
Tripletex to  Dataflow
======================

Generated: 2024-08-26 15:26:44

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Country to  Country
-----------------------------
Every Tripletex Country will be synchronized with a  Country.

Once a link between a Tripletex Country and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a  Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     -  Country Property
     -  Data Type
   * - isoAlpha2Code
     - isoCode
     - "string"
   * - name
     - name
     - "string"

