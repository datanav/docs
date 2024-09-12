==============================
Wix.com to Unieconomy Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Currencies to Unieconomy Currencycodes
----------------------------------------------
Every Wix.com Currencies will be synchronized with a Unieconomy Currencycodes.

If a matching Unieconomy Currencycodes already exists, the Wix.com Currencies will be merged with the existing one.
If no matching Unieconomy Currencycodes is found, a new Unieconomy Currencycodes will be created.

A Wix.com Currencies will merge with a Unieconomy Currencycodes if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Unieconomy Currencycodes Property
   * - code
     - Code

Once a link between a Wix.com Currencies and a Unieconomy Currencycodes is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Currencies and a Unieconomy Currencycodes:

.. list-table::
   :header-rows: 1

   * - Wix.com Currencies Property
     - Unieconomy Currencycodes Property
     - Unieconomy Data Type

