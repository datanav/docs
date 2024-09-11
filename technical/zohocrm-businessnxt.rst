===============================
ZohoCRM to BusinessNxt Dataflow
===============================

Generated: 2024-09-11 08:49:20

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to BusinessNxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Visma Address
--------------------------------
Every ZohoCRM Account will be synchronized with a Visma Address.

Once a link between a ZohoCRM Account and a Visma Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Visma Address:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Visma Address Property
     - Visma Data Type
   * - Account_Name
     - name
     - "string"
   * - Fax
     - fax
     - "string"
   * - Phone
     - phone
     - "string"


ZohoCRM Deal to Visma Order
---------------------------
Every ZohoCRM Deal will be synchronized with a Visma Order.

Once a link between a ZohoCRM Deal and a Visma Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Visma Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Visma Order Property
     - Visma Data Type
   * - Closing_Date
     - orderDate
     - "string"
   * - Deal_Name
     - name
     - "string"


ZohoCRM Account to BusinessNxt Country
--------------------------------------
Every ZohoCRM Account will be synchronized with a BusinessNxt Country.

Once a link between a ZohoCRM Account and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to BusinessNxt Country
--------------------------------------
Every ZohoCRM Contact will be synchronized with a BusinessNxt Country.

Once a link between a ZohoCRM Contact and a BusinessNxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a BusinessNxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - BusinessNxt Country Property
     - BusinessNxt Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

