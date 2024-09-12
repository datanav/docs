=======================
ZohoCRM to Ssb Dataflow
=======================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Ssb. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Ssb Country
------------------------------
Every ZohoCRM Account will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the ZohoCRM Account will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A ZohoCRM Account will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Ssb Country Property
   * - Billing_Country
     - name
   * - Shipping_Country
     - name

Once a link between a ZohoCRM Account and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Ssb Country Property
     - Ssb Data Type


ZohoCRM Contact to Ssb Country
------------------------------
Every ZohoCRM Contact will be synchronized with a Ssb Country.

If a matching Ssb Country already exists, the ZohoCRM Contact will be merged with the existing one.
If no matching Ssb Country is found, a new Ssb Country will be created.

A ZohoCRM Contact will merge with a Ssb Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Ssb Country Property
   * - Other_Country
     - name
   * - Mailing_Country
     - name

Once a link between a ZohoCRM Contact and a Ssb Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Ssb Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Ssb Country Property
     - Ssb Data Type

