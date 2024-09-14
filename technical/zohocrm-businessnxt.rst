================================
ZohoCRM to Business Nxt Dataflow
================================

Generated: 2024-09-14 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Business Nxt. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Business Nxt Address
---------------------------------------
Every ZohoCRM Account will be synchronized with a Business Nxt Address.

Once a link between a ZohoCRM Account and a Business Nxt Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Business Nxt Address:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Business Nxt Address Property
     - Business Nxt Data Type
   * - Account_Name
     - name
     - "string"
   * - Fax
     - fax
     - "string"
   * - Phone
     - phone
     - "string"


ZohoCRM Deal to Business Nxt Order
----------------------------------
Every ZohoCRM Deal will be synchronized with a Business Nxt Order.

Once a link between a ZohoCRM Deal and a Business Nxt Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Business Nxt Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Business Nxt Order Property
     - Business Nxt Data Type
   * - Closing_Date
     - orderDate
     - "string"
   * - Deal_Name
     - name
     - "string"


ZohoCRM Account to Business Nxt Country
---------------------------------------
Every ZohoCRM Account will be synchronized with a Business Nxt Country.

Once a link between a ZohoCRM Account and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - Billing_Country
     - name
     - "string"
   * - Industry
     - name
     - "string"
   * - Shipping_Country
     - name
     - "string"


ZohoCRM Contact to Business Nxt Country
---------------------------------------
Every ZohoCRM Contact will be synchronized with a Business Nxt Country.

Once a link between a ZohoCRM Contact and a Business Nxt Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Business Nxt Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Business Nxt Country Property
     - Business Nxt Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

