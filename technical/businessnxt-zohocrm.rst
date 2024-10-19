================================
Business Nxt to ZohoCRM Dataflow
================================

Generated: 2024-10-19 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Business Nxt to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Business Nxt Address to ZohoCRM Account
---------------------------------------
Every Business Nxt Address will be synchronized with a ZohoCRM Account.

Once a link between a Business Nxt Address and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Address and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Business Nxt Address Property
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


Business Nxt Company to ZohoCRM Account
---------------------------------------
Every Business Nxt Company will be synchronized with a ZohoCRM Account.

Once a link between a Business Nxt Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Business Nxt Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Business Nxt Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - name
     - Account_Name
     - "string"

