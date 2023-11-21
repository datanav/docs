.. _talk_poweroffice:

Poweroffice
===========

`PowerOffice <https://poweroffice.no>`_ is an all-in-one business solution. It is a cloud-based software that allows small and medium businesses to manage their accounting, invoicing, payroll, and human resources.

Contact support@sesam.io if you want to learn more about this offering.

How to find your PowerOffice Client Key
---------------------------------------
In order to connect your PowerOffice account to Sesam Talk you need to create a Client Key in PowerOffice. Simply follow these steps to create one:

#. Login to your PowerOffice account
#. Navigate to **Menu** then click on **Settings**
#. Under System, click **Extensions**
#. Click on **Add Extension**
#. Pick **Custom** from the Extension menu
#. Paste this key in the Application Key field : **109b9cac-bafd-45f0-a996-94169765502c**
#. Copy your Client Key and store it somewhere
#. Use the Client Key when you connect your PowerOffice to Sesam Talk, as shown bellow

|

.. image:: images/poweroffice-client-key.png
    :width: 800px
    :align: left
    :alt: PowerOffice Client Key 

|

Frequently Asked Questions
--------------------------

Why is Product data not in sync with PowerOffice?
*************************************************

Make sure you have selected **Standard Sales Account** for your products in PowerOffice.

#. Navigate to **Settings** in PowerOffice
#. Click on a **Invoice Settings**
#. Click on **Sales Accounts** on left menu
#. Make sure you have selected an account for **Standard Sales Account**

.. image:: images/poweroffice-standard-sales-account.png
    :width: 800px
    :align: left
    :alt: PowerOffice Standard Sales Account

Why can I not see my CRM companies and contacts?
************************************************

Companies and contacts in CRM will only sync to PowerOffice if they are associated or involved with a closed/won deal.

Make sure that the companies and contacts you are trying to synchronise are associated with a closed or won deal in your CRM.


What to Expect When Connecting Your PowerOffice to other systems
****************************************************************

Contacts
^^^^^^^^

- **PowerOffice Contacts:** All contacts in your PowerOffice will sync to other systems as humans.

- **todo link Humans:** Only humans link to human associated with a closed/won deal will synchronize to your PowerOffice.

- **Merging:** Contacts will merge if they share the same email. todo link merging of humans


.. admonition:: **Example**

   HubSpot also merges on email so contacts are merged between Poweroffice and Hubspot if they have the same email. For contacts that do not have email duplicates might occur. If contacts share the same email, they will be merged. For guidance on avoiding duplicates, refer to :ref:`avoid_duplicates`. For guidance on avoiding merges, refer to `:ref:avoid_merges`.

Customers
^^^^^^^^^

- **PowerOffice Customers:** All PowerOffice customers will sync to other systems as organisation.

- **todo link Organisations:** Only organisation associated with a closed/won deal will synchronize to your PowerOffice. todo link to _customer

todo figure out if we support human customers
- **todo link Human:** Only organisation associated with a closed/won deal will synchronize to your PowerOffice. todo link to _customer

- **Merging:** Companies will not merge as we have not idenfied any safe merging criterias in PowerOffice, refer to :ref:`avoid_duplicates`.

Suppliers
^^^^^^^^^

todo do we support this?

Sales order drafts
^^^^^^^^^^^^^^^^^^

Found under 'Invoices'.

- **PowerOffice sales order drafts:** All closed or won deals will generate sales order drafts in your PowerOffice, along with associated data such as company, contact, products, and line items.

Products
^^^^^^^^

- **PowerOffice Products:** All products will synchronize to other systems products.

- **todo link Products:** All products will synchronize with PowerOffice products.

- **Merging:** Products will not merge as we have not idenfied any safe merging criterias,  refer to :ref:`avoid_duplicates`.





