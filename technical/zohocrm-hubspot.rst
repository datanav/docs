===========================
ZohoCRM to Hubspot Dataflow
===========================

Generated: 2024-07-02 00:00:02

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Hubspot. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Hubspot Company
----------------------------------
Every ZohoCRM Account will be synchronized with a Hubspot Company.

Once a link between a ZohoCRM Account and a Hubspot Company is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Hubspot Company:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Hubspot Company Property
     - Hubspot Data Type
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


ZohoCRM Contact to Hubspot Contact
----------------------------------
Every ZohoCRM Contact will be synchronized with a Hubspot Contact.

Once a link between a ZohoCRM Contact and a Hubspot Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Hubspot Contact:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Hubspot Contact Property
     - Hubspot Data Type
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


ZohoCRM Deal to Hubspot Deal
----------------------------
When a HubSpot Deal has a 100% probability of beeing sold, it  will be synchronized with a Hubspot Deal.

Once a link between a ZohoCRM Deal and a Hubspot Deal is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Deal and a Hubspot Deal:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Deal Property
     - Hubspot Deal Property
     - Hubspot Data Type
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

