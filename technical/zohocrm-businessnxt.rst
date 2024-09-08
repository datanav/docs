===============================
ZohoCRM to Businessnxt Dataflow
===============================

Generated: 2024-09-08 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Businessnxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Businessnxt Address
--------------------------------------
Every ZohoCRM Account will be synchronized with a Businessnxt Address.

Once a link between a ZohoCRM Account and a Businessnxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Businessnxt Address:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Businessnxt Address Property
     - Businessnxt Data Type
   * - Account_Name
     - name
     - "string"
   * - Fax
     - fax
     - "string"
   * - Phone
     - phone
     - "string"


ZohoCRM Deal to Businessnxt Order
---------------------------------
Every ZohoCRM Deal will be synchronized with a Businessnxt Order.

Once a link between a ZohoCRM Deal and a Businessnxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Businessnxt Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Businessnxt Order Property
     - Businessnxt Data Type
   * - Closing_Date
     - orderDate
     - "string"
   * - Deal_Name
     - name
     - "string"


ZohoCRM Account to Businessnxt Country
--------------------------------------
Every ZohoCRM Account will be synchronized with a Businessnxt Country.

Once a link between a ZohoCRM Account and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to Businessnxt Country
--------------------------------------
Every ZohoCRM Contact will be synchronized with a Businessnxt Country.

Once a link between a ZohoCRM Contact and a Businessnxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Businessnxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Businessnxt Country Property
     - Businessnxt Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

