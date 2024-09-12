==========================
WebCRM to ZohoCRM Dataflow
==========================

Generated: 2024-09-12 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from WebCRM to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

WebCRM Organisations to ZohoCRM Account
---------------------------------------
Every WebCRM Organisations will be synchronized with a ZohoCRM Account.

Once a link between a WebCRM Organisations and a ZohoCRM Account is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Organisations and a ZohoCRM Account:

.. list-table::
   :header-rows: 1

   * - WebCRM Organisations Property
     - ZohoCRM Account Property
     - ZohoCRM Data Type
   * - OrganisationCity
     - Billing_City
     - "string"
   * - OrganisationCity
     - Shipping_City
     - "string"
   * - OrganisationCompanyDescription
     - Created_Time
     - "string"
   * - OrganisationDeliveryCity
     - Billing_City
     - "string"
   * - OrganisationDeliveryCity
     - Shipping_City
     - "string"
   * - OrganisationDeliveryPostCode
     - Billing_Code
     - "string"
   * - OrganisationDeliveryPostCode
     - Shipping_Code
     - "string"
   * - OrganisationDeliveryState
     - Billing_State
     - "string"
   * - OrganisationDeliveryState
     - Shipping_State
     - "string"
   * - OrganisationName
     - Account_Name
     - "string"
   * - OrganisationPostCode
     - Billing_Code
     - "string"
   * - OrganisationPostCode
     - Shipping_Code
     - "string"
   * - OrganisationTelephone
     - Phone
     - "string"


WebCRM Opportunities to ZohoCRM Deal
------------------------------------
Every WebCRM Opportunities will be synchronized with a ZohoCRM Deal.

Once a link between a WebCRM Opportunities and a ZohoCRM Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a WebCRM Opportunities and a ZohoCRM Deal:

.. list-table::
   :header-rows: 1

   * - WebCRM Opportunities Property
     - ZohoCRM Deal Property
     - ZohoCRM Data Type

