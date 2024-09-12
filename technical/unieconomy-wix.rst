==========================
Unieconomy to Wix Dataflow
==========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Unieconomy to Wix. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Unieconomy Currencycodes to Wix Currencies
------------------------------------------
Every Unieconomy Currencycodes will be synchronized with a Wix Currencies.

If a matching Wix Currencies already exists, the Unieconomy Currencycodes will be merged with the existing one.
If no matching Wix Currencies is found, a new Wix Currencies will be created.

A Unieconomy Currencycodes will merge with a Wix Currencies if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Wix Currencies Property
   * - Code
     - code

Once a link between a Unieconomy Currencycodes and a Wix Currencies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Unieconomy Currencycodes and a Wix Currencies:

.. list-table::
   :header-rows: 1

   * - Unieconomy Currencycodes Property
     - Wix Currencies Property
     - Wix Data Type

