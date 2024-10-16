==================================
WooCommerce to Tidsbanken Dataflow
==================================

Generated: 2024-10-16 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WooCommerce to Tidsbanken. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WooCommerce Customer to Tidsbanken Kunde
----------------------------------------
Every WooCommerce Customer will be synchronized with a Tidsbanken Kunde.

Once a link between a WooCommerce Customer and a Tidsbanken Kunde is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WooCommerce Customer and a Tidsbanken Kunde:

.. list-table::
   :header-rows: 1

   * - WooCommerce Customer Property
     - Tidsbanken Kunde Property
     - Tidsbanken Data Type

