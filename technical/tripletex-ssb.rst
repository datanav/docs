=========================
Tripletex to Ssb Dataflow
=========================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Tripletex to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Tripletex Country to Ssb Country
--------------------------------
Every Tripletex Country will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the Tripletex Country will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A Tripletex Country will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Ssb Country Property
   * - name
     - name
   * - isoAlpha3Code
     - code

Once a link between a Tripletex Country and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Tripletex Country and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - Tripletex Country Property
     - Ssb Country Property
     - Ssb Data Type

