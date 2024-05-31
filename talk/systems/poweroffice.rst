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
#. Select **Sesam Talk** from the list, this will generate your **Client Key**
#. Copy your **Client Key** and store it somewhere
#. Use the **Client Key** when you connect your PowerOffice to Sesam Talk, as shown bellow

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

Make sure that the companies and contacts you are trying to synchronise are not duplicated in PowerOffice.


Why contact person is not synched to PowerOffice?
*************************************************

Your contact person might already exist in PowerOffice, and is associated with another customer. We identify contacts by their emails, so if the email is the same as another contact person, the data will be merged, and you will not see your contact flow as you would expect.

.. Note ::

    Contact persons may have different names across systems. It is important to verify whether the contact you are attempting to synchronise shares the same email address as any other contact present in PowerOffice.

In PowerOffice a contact person can only be associatied with one customer at a time. That means that in order to associate this contact with another company, you need first to remove it from the customer he is currently associated with.

To delete a contact person association to a customer you can do the following:

#. Find the customer associated with your contact person
#. Click on **Contact Persons** on the left menu once on the customer card
#. Select the contact person you want to remove and click **Remove**

Why are my deleted HubSpot lineitems not deleted in PowerOffice order
*********************************************************************

Sesam Talk does not delete data in HubSpot and PowerOffice. This means that deleting lineitems in either of the systems will not be reflected in the other system.

To ensure data consistency, we recommend that you manually delete corresponding line items in both systems whenever adjustments are made to an order.

Why are customers that share the same email address merged?
***********************************************************

We merge customers on email address to avoid duplicates when syncing with other systems. We do not expect multiple customers to share the same email address. If two customers share the same real contact person, we expect that there exist one contact person per customer. If that person is to be contacted on the same email regardless of the customer, we expect those contacts to share the same email address. When two contacts share the same email those will be merged and kept in sync, but the customers will remain separated.

Synchronisation of Products
***************************************************
Sesam Talk synchronises all products from PowerOffice, active and non-active.
