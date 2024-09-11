===============================
BusinessNxt to ZohoCRM Dataflow
===============================

Generated: 2024-09-11 08:35:29

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from BusinessNxt to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Visma Address to ZohoCRM Account
--------------------------------
Every Visma Address will be synchronized with a ZohoCRM Account.

Once a link between a Visma Address and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Address and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Visma Address Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - fax
     - Fax
     - "string"
   * - name
     - Account_Name
     - "string"
   * - phone
     - Phone
     - "string"


Visma Company to ZohoCRM Account
--------------------------------
Every Visma Company will be synchronized with a ZohoCRM Account.

Once a link between a Visma Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Visma Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Visma Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

