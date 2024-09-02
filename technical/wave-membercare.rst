===========================
Wave Financial to  Dataflow
===========================

Generated: 2024-09-02 14:18:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave Financial to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Customer to  Companies
---------------------------
Every Wave Customer will be synchronized with a  Companies.

Once a link between a Wave Customer and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a  Companies:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     -  Companies Property
     -  Data Type
   * - name
     - companyName
     - "string"
   * - website
     - url
     - "string"


Wave Country to  Countries
--------------------------
Every Wave Country will be synchronized with a  Countries.

Once a link between a Wave Country and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a  Countries:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     -  Countries Property
     -  Data Type
   * - name
     - name
     - "string"

