===========================
Wave to Unieconomy Dataflow
===========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wave to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wave Country to Unieconomy Countries
------------------------------------
Every Wave Country will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the Wave Country will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A Wave Country will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Unieconomy Countries Property
   * - name
     - Name
   * - code
     - CountryCode

Once a link between a Wave Country and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Country and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - Wave Country Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


Wave Currency to Unieconomy Currencycodes
-----------------------------------------
Every Wave Currency will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the Wave Currency will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A Wave Currency will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Unieconomy Currencycodes Property
   * - code
     - Code

Once a link between a Wave Currency and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Currency and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - Wave Currency Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type


Wave Customer to Unieconomy Customers
-------------------------------------
Every Wave Customer will be synchronized with a Unieconomy Customers.

Once a link between a Wave Customer and a Unieconomy Customers is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wave Customer and a Unieconomy Customers:

.. list-table::
   :header-rows: 1

   * - Wave Customer Property
     - Unieconomy Customers Property
     - Unieconomy Data Type
   * - website
     - WebUrl
     - "string"

