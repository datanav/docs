============================
Invoiced to ZohoCRM Dataflow
============================

Generated: 2024-09-17 07:26:51

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Invoiced to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Invoiced Customers company to ZohoCRM Account
---------------------------------------------
Every Invoiced Customers company will be synchronized with a ZohoCRM Account.

Once a link between a Invoiced Customers company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"


Invoiced Customers company to ZohoCRM Contact
---------------------------------------------
Every Invoiced Customers company will be synchronized with a ZohoCRM Contact.

Once a link between a Invoiced Customers company and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers company and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers company Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type


Invoiced Customers person to ZohoCRM Contact
--------------------------------------------
Every Invoiced Customers person will be synchronized with a ZohoCRM Contact.

Once a link between a Invoiced Customers person and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Invoiced Customers person and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Invoiced Customers person Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type

