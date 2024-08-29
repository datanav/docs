====================
ZohoCRM to  Dataflow
====================

Generated: 2024-08-29 08:00:40

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Address
---------------------------
Every ZohoCRM Account will be synchronized with a  Address.

Once a link between a ZohoCRM Account and a  Address is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Address:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Address Property
     -  Data Type
   * - Account_Name
     - name
     - "string"
   * - Fax
     - fax
     - "string"
   * - Phone
     - phone
     - "string"


ZohoCRM Deal to  Order
----------------------
Every ZohoCRM Deal will be synchronized with a  Order.

Once a link between a ZohoCRM Deal and a  Order is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Order:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Order Property
     -  Data Type
   * - Closing_Date
     - orderDate
     - "string"
   * - Deal_Name
     - name
     - "string"


ZohoCRM Account to  Country
---------------------------
Every ZohoCRM Account will be synchronized with a  Country.

Once a link between a ZohoCRM Account and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Country Property
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


ZohoCRM Contact to  Country
---------------------------
Every ZohoCRM Contact will be synchronized with a  Country.

Once a link between a ZohoCRM Contact and a  Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Country Property
     -  Data Type
   * - Mailing_Country
     - name
     - "string"
   * - Other_Country
     - name
     - "string"

