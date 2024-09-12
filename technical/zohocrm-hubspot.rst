===========================
ZohoCRM to HubSpot Dataflow
===========================

Generated: 2024-09-12 13:14:11

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to HubSpot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to HubSpot Company
----------------------------------
Every ZohoCRM Account will be synchronized with a HubSpot Company.

Once a link between a ZohoCRM Account and a HubSpot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a HubSpot Company:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - HubSpot Company Property
     - HubSpot Data Type
   * - Account_Name
     - properties.name
     - "string"
   * - Billing_City
     - properties.city
     - "string"
   * - Billing_Code
     - properties.zip
     - "string"
   * - Billing_Country
     - properties.country
     - "string"
   * - Billing_State
     - properties.state
     - "string"
   * - Created_Time
     - properties.description
     - "string"
   * - Phone
     - properties.phone
     - "string"
   * - Shipping_City
     - properties.city
     - "string"
   * - Shipping_Code
     - properties.zip
     - "string"
   * - Shipping_Country
     - properties.country
     - "string"
   * - Shipping_State
     - properties.state
     - "string"
   * - Website
     - properties.website
     - "string"
   * - id
     - id
     - "string"


ZohoCRM Contact to HubSpot Contact
----------------------------------
Every ZohoCRM Contact will be synchronized with a HubSpot Contact.

Once a link between a ZohoCRM Contact and a HubSpot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a HubSpot Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - HubSpot Contact Property
     - HubSpot Data Type
   * - Email
     - properties.email
     - "string"
   * - First_Name
     - properties.firstname
     - "string"
   * - Last_Name
     - properties.lastname
     - "string"
   * - Mailing_City
     - properties.city
     - "string"
   * - Mailing_Country
     - properties.country
     - "string"
   * - Mailing_State
     - properties.state
     - "string"
   * - Mailing_Zip
     - properties.zip
     - "string"
   * - Mobile
     - properties.mobilephone
     - "string"
   * - Other_City
     - properties.city
     - "string"
   * - Other_Country
     - properties.country
     - "string"
   * - Other_Phone
     - properties.phone
     - "string"
   * - Other_State
     - properties.state
     - "string"
   * - Other_Zip
     - properties.zip
     - "string"
   * - Phone
     - properties.phone
     - "string"
   * - Secondary_Email
     - properties.email
     - "string"
   * - id
     - id
     - "string"


ZohoCRM Deal to HubSpot Deal
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a HubSpot Deal.

Once a link between a ZohoCRM Deal and a HubSpot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a HubSpot Deal:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - HubSpot Deal Property
     - HubSpot Data Type
   * - Amount
     - properties.amount
     - "string"
   * - Closing_Date
     - properties.closedate
     - "string"
   * - Deal_Name
     - properties.dealname
     - "string"
   * - Owner.id
     - properties.hubspot_owner_id
     - "string"
   * - Probability
     - properties.dealstage
     - "string"
   * - Stage
     - properties.pipeline
     - "string"

