========================
ZohoCRM to Keap Dataflow
========================

Generated: 2024-09-13 00:00:01

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Keap. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Keap Companies
---------------------------------
Every ZohoCRM Account will be synchronized with a Keap Companies.

Once a link between a ZohoCRM Account and a Keap Companies is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Keap Companies:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Keap Companies Property
     - Keap Data Type
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


ZohoCRM Contact to Keap Contacts
--------------------------------
Every ZohoCRM Contact will be synchronized with a Keap Contacts.

Once a link between a ZohoCRM Contact and a Keap Contacts is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Keap Contacts:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Keap Contacts Property
     - Keap Data Type


ZohoCRM Deal to Keap Opportunity
--------------------------------
Every ZohoCRM Deal will be synchronized with a Keap Opportunity.

Once a link between a ZohoCRM Deal and a Keap Opportunity is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Keap Opportunity:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Keap Opportunity Property
     - Keap Data Type
   * - Deal_Name
     - opportunity_title
     - "string"
   * - Owner.id
     - contact.id
     - "string"

