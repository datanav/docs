==============================
ZohoCRM to Unieconomy Dataflow
==============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Unieconomy. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Unieconomy Countries
---------------------------------------
Every ZohoCRM Account will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the ZohoCRM Account will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A ZohoCRM Account will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Unieconomy Countries Property
   * - Billing_Country
     - Name
   * - Shipping_Country
     - Name

Once a link between a ZohoCRM Account and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Unieconomy Countries Property
     - Unieconomy Data Type


ZohoCRM Contact to Unieconomy Countries
---------------------------------------
Every ZohoCRM Contact will be synchronized with a Unieconomy Countries.

If a matching Unieconomy Countries already exists, the ZohoCRM Contact will be merged with the existing one.
If no matching Unieconomy Countries is found, a new Unieconomy Countries will be created.

A ZohoCRM Contact will merge with a Unieconomy Countries if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Unieconomy Countries Property
   * - Other_Country
     - Name
   * - Mailing_Country
     - Name

Once a link between a ZohoCRM Contact and a Unieconomy Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Unieconomy Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Unieconomy Countries Property
     - Unieconomy Data Type

