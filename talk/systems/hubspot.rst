.. _talk_hubspot:

Hubspot
=======
`HubSpot's <https://hubspot.com>`_ integrated CRM platform contains marketing, sales, service, operations, and website-building tools.

.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    **Making Hubspot Talk**

    Easily synchronise valuable data between Hubspot and your other systems.
    
    |
    
    .. link-button:: https://hubspot.talk.market
        :type: url
        :text: Try for free
        :classes: btn-primary btn-block

Frequently Asked Questions
--------------------------


Why do I get company duplicates in HubSpot when I connect other systems?
************************************************************************

HubSpot does not have a unique identifier for companies that is safe enough to perform a merge of companies. In other words, we are unable to safely merge companies in HubSpot and duplicates might appear over time.

Please see `this section <https://docs.sesam.io/talk/merging/index.html#company-duplicates-when-onboarding-hubspot>`_ for instructions on how how to utilize the Hubspot deduplication feature together with Talk to avoid duplicates during onboarding.

.. note ::

    Remember that we **do not delete** data from your systems. You will need to manage deduplication in your other systems, if duplication accurs.

Why is the address of my contact in HubSpot not up to date?
***********************************************************

In Hubspot the contact field for **address** is read-only. That means that we can not write data into this field. 

If you want to change the address of a contact, you should do it in HubSpot.

How to disable the synchronisation
**********************************

Follow these steps to disable the synchronisation of your HubSpot account:

#. Log in to `Sesam Management Console <https://talk.sesam.io/>`_ 
#. Select **HubSpot**
#. Click on **Configuration** on the left menu
#. Click on **Disconnect**

.. note::

    We suggest that you delete the **Wave by Sesam** application in HubSpot settings > Connected applications.
