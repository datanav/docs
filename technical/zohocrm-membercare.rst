====================
ZohoCRM to  Dataflow
====================

Generated: 2024-09-02 14:00:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Companycategories
-------------------------------------
Every ZohoCRM Account will be synchronized with a  Companycategories.

Once a link between a ZohoCRM Account and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Companycategories Property
     -  Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Account to  Countries
-----------------------------
Every ZohoCRM Account will be synchronized with a  Countries.

Once a link between a ZohoCRM Account and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Countries Property
     -  Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to  Companycategories
-------------------------------------
Every ZohoCRM Contact will be synchronized with a  Companycategories.

Once a link between a ZohoCRM Contact and a  Companycategories is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Companycategories:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Companycategories Property
     -  Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"


ZohoCRM Contact to  Countries
-----------------------------
Every ZohoCRM Contact will be synchronized with a  Countries.

Once a link between a ZohoCRM Contact and a  Countries is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Countries:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Countries Property
     -  Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

