======================
Tripletex to  Dataflow
======================

Generated: 2024-09-02 14:18:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Customer to  Companies
--------------------------------
Every Tripletex Customer will be synchronized with a  Companies.

Once a link between a Tripletex Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Customer Property
     -  Companies Property
     -  Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Tripletex Department to  Companies
----------------------------------
Every Tripletex Department will be synchronized with a  Companies.

Once a link between a Tripletex Department and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Department and a  Companies:

.. list-table::
   :header-rows: 1

   * - Tripletex Department Property
     -  Companies Property
     -  Data Type
   * - name
     - companyName
     - "string"


Tripletex Country to  Countries
-------------------------------
Every Tripletex Country will be synchronized with a  Countries.

Once a link between a Tripletex Country and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a  Countries:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     -  Countries Property
     -  Data Type
   * - isoAlpha2Code
     - iso2Letter
     - "string"
   * - isoAlpha3Code
     - iso3Letter
     - "string"
   * - name
     - name
     - "string"

