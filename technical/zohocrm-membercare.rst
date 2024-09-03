==============================
ZohoCRM to Membercare Dataflow
==============================

Generated: 2024-09-03 09:11:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Membercare. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Membercare Companies
---------------------------------------
Every ZohoCRM Account will be synchronized with a Membercare Companies.

Once a link between a ZohoCRM Account and a Membercare Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Membercare Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Membercare Companies Property
     - Membercare Data Type
   * - Account_Name
     - companyName
     - "string"
   * - Website
     - url
     - "string"


ZohoCRM Account to Membercare Countries
---------------------------------------
Every ZohoCRM Account will be synchronized with a Membercare Countries.

Once a link between a ZohoCRM Account and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to Membercare Countries
---------------------------------------
Every ZohoCRM Contact will be synchronized with a Membercare Countries.

Once a link between a ZohoCRM Contact and a Membercare Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Membercare Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Membercare Countries Property
     - Membercare Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

