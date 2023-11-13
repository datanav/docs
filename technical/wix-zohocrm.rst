===========================
Wix.com to ZohoCRM Dataflow
===========================

Generated: 2023-11-13 13:35:44

Introduction.
------------

This technical document provides a detailed overview of the Sesam Talk data flow from Wix.com to ZohoCRM. It serves as a QA checklist for testing purposes and is the intellectual property of Sesam.io AS. The content contains confidential information regulated under an NDA agreement, and sharing or distributing it without written permission is prohibited.

Wix.com Members to ZohoCRM Contact
----------------------------------
Every Wix.com Members will be synchronized with a ZohoCRM Contact.

Once a link between a Wix.com Members and a ZohoCRM Contact is established, it will keep in sync between the two systems, regardless of where it is edited.

The following properties are synchronized between a Wix.com Members and a ZohoCRM Contact:

.. list-table::
   :header-rows: 1

   * - Wix.com Members Property
     - ZohoCRM Contact Property
     - ZohoCRM Data Type
   * - loginEmail
     - Email
     - "string"
   * - loginEmail
     - Secondary_Email
     - "string"

