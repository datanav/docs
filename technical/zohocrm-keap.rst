====================
ZohoCRM to  Dataflow
====================

Generated: 2024-09-03 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to . It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to  Companies
-----------------------------
Every ZohoCRM Account will be synchronized with a  Companies.

Once a link between a ZohoCRM Account and a  Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a  Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     -  Companies Property
     -  Data Type
   * - Account_Name
     - company_name
     - "string"
   * - Billing_City
     - address.locality
     - "string"
   * - Billing_Code
     - address.zip_code
     - "string"
   * - Shipping_City
     - address.locality
     - "string"
   * - Shipping_Code
     - address.zip_code
     - "string"
   * - id
     - id
     - "string"


ZohoCRM Contact to  Contacts
----------------------------
Every ZohoCRM Contact will be synchronized with a  Contacts.

Once a link between a ZohoCRM Contact and a  Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a  Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     -  Contacts Property
     -  Data Type


ZohoCRM Deal to  Opportunity
----------------------------
Every ZohoCRM Deal will be synchronized with a  Opportunity.

Once a link between a ZohoCRM Deal and a  Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a  Opportunity:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     -  Opportunity Property
     -  Data Type
   * - Deal_Name
     - opportunity_title
     - "string"
   * - Owner.id
     - contact.id
     - "string"

