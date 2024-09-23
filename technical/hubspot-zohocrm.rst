===========================
HubSpot to ZohoCRM Dataflow
===========================

Generated: 2024-09-23 00:00:22

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from HubSpot to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

HubSpot Company to ZohoCRM Account
----------------------------------
Every HubSpot Company will be synchronized with a ZohoCRM Account.

Once a link between a HubSpot Company and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Company and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - HubSpot Company Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - properties.city
     - Billing_City
     - "string"
   * - properties.city
     - Shipping_City
     - "string"
   * - properties.country
     - Billing_Country
     - "string"
   * - properties.country
     - Shipping_Country
     - "string"
   * - properties.description
     - Created_Time
     - "string"
   * - properties.name
     - Account_Name
     - "string"
   * - properties.phone
     - Phone
     - "string"
   * - properties.state
     - Billing_State
     - "string"
   * - properties.state
     - Shipping_State
     - "string"
   * - properties.website
     - Website
     - "string"
   * - properties.zip
     - Billing_Code
     - "string"
   * - properties.zip
     - Shipping_Code
     - "string"


HubSpot Deal to ZohoCRM Deal
----------------------------
Every HubSpot Deal will be synchronized with a ZohoCRM Deal.

Once a link between a HubSpot Deal and a ZohoCRM Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a HubSpot Deal and a ZohoCRM Deal:

.. list-table::
   :header-rows: 1

   * - HubSpot Deal Property
     - ZohoCRM Deal Property
     - ZohoCRM Data Type

