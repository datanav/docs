=============================
ZohoCRM to Tripletex Dataflow
=============================

Generated: 2024-09-12 12:58:41

Introduction
------------

This technical document provides a detailed overview of the Sesam Talk data flow from ZohoCRM to Tripletex. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

ZohoCRM Account to Tripletex Country
------------------------------------
Every ZohoCRM Account will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the ZohoCRM Account will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A ZohoCRM Account will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Tripletex Country Property
   * - Billing_Country
     - name
   * - Shipping_Country
     - name

Once a link between a ZohoCRM Account and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Account and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Account Property
     - Tripletex Country Property
     - Tripletex Data Type


ZohoCRM Contact to Tripletex Country
------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Country.

If a matching Tripletex Country already exists, the ZohoCRM Contact will be merged with the existing one.
If no matching Tripletex Country is found, a new Tripletex Country will be created.

A ZohoCRM Contact will merge with a Tripletex Country if one of the following property combinations match:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Country Property
   * - Other_Country
     - name
   * - Mailing_Country
     - name

Once a link between a ZohoCRM Contact and a Tripletex Country is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Country:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Country Property
     - Tripletex Data Type


ZohoCRM Contact to Tripletex Customer person
--------------------------------------------
Every ZohoCRM Contact will be synchronized with a Tripletex Customer person.

Once a link between a ZohoCRM Contact and a Tripletex Customer person is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a ZohoCRM Contact and a Tripletex Customer person:

.. list-table::
   :header-rows: 1

   * - ZohoCRM Contact Property
     - Tripletex Customer person Property
     - Tripletex Data Type
   * - Email
     - email
     - "string"
   * - Full_Name
     - name
     - "string"
   * - Mailing_City
     - deliveryAddress.city
     - "string"
   * - Mailing_City
     - physicalAddress.city
     - "string"
   * - Mailing_City
     - postalAddress.city
     - "string"
   * - Mailing_Country
     - deliveryAddress.country.id
     - "string"
   * - Mailing_Country
     - physicalAddress.country.id
     - "integer"
   * - Mailing_Country
     - postalAddress.country.id
     - "integer"
   * - Mailing_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Mailing_Zip
     - physicalAddress.postalCode
     - "string"
   * - Mailing_Zip
     - postalAddress.postalCode
     - "string"
   * - Mobile
     - phoneNumberMobile
     - "string"
   * - Other_City
     - deliveryAddress.city
     - "string"
   * - Other_City
     - physicalAddress.city
     - "string"
   * - Other_City
     - postalAddress.city
     - "string"
   * - Other_Country
     - deliveryAddress.country.id
     - "string"
   * - Other_Country
     - physicalAddress.country.id
     - "integer"
   * - Other_Country
     - postalAddress.country.id
     - "integer"
   * - Other_Phone
     - phoneNumber
     - "string"
   * - Other_Zip
     - deliveryAddress.postalCode
     - "string"
   * - Other_Zip
     - physicalAddress.postalCode
     - "string"
   * - Other_Zip
     - postalAddress.postalCode
     - "string"
   * - Phone
     - phoneNumber
     - "string"
   * - Secondary_Email
     - email
     - "string"
   * - id
     - id
     - "integer"

