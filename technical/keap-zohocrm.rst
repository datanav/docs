========================
Keap to ZohoCRM Dataflow
========================

Generated: 2024-09-14 00:00:00

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Keap to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Keap Companies to ZohoCRM Account
---------------------------------
Every Keap Companies will be synchronized with a ZohoCRM Account.

Once a link between a Keap Companies and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Companies and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - Keap Companies Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - address.locality
     - Billing_City
     - "string"
   * - address.locality
     - Shipping_City
     - "string"
   * - address.zip_code
     - Billing_Code
     - "string"
   * - address.zip_code
     - Shipping_Code
     - "string"
   * - company_name
     - Account_Name
     - "string"


Keap Opportunity to ZohoCRM Deal
--------------------------------
Every Keap Opportunity will be synchronized with a ZohoCRM Deal.

Once a link between a Keap Opportunity and a ZohoCRM Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Keap Opportunity and a ZohoCRM Deal:

.. list-table::
   :header-rows: 1

   * - Keap Opportunity Property
     - ZohoCRM Deal Property
     - ZohoCRM Data Type
   * - contact.id
     - Owner.id
     - "string"
   * - opportunity_title
     - Deal_Name
     - "string"

