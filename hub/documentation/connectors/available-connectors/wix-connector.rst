.. _wix_connector:

===
Wix
===

`Wix <https://wix.com>`_ website builder offers a complete solution from enterprise-grade infrastructure and business features to advanced SEO and marketing tools–enabling anyone to create and grow online.

The Wix connector configuration can be found in the  `wix-connector github repository <https://github.com/sesam-io/wix-connector>`_. The `playground branch <https://github.com/sesam-io/wix-connector/tree/playground>`_ is typically the most complete branch.

Find your API key
-----------------

To connect your Wix account you need to create an API-key. 

.. image:: images/generate-api-key-wix.png
    :width: 100%
    :align: left
    :alt: Generate Wix API-Key 

Follow these steps to generate an API-key for Wix
*************************************************

.. note::
	You need to be the **owner** on your Wix site to be able to create a new API-key.

	If you don't have direct access to the site, request the key and the account ID from the site owner.

#. On your Wix account. Open the `Wix API Keys Manager <https://manage.wix.com/account/api-keys>`_ 
#. Click Create API-Key
#. In the Name field write the name of the API-Key, for example: Sesam.
#. Under **All site permissions** choose **Wix Stores** and **Wix Contacts & Members**.
#. Follow the steps and once you get your API-Key, also called key's token, Copy it and store it somewhere.


Frequently Asked Questions
--------------------------

Why are my ERP orders not created in Wix?
*************************************************

The Wix API does not allow general updates of orders, so we do not write any orders as we are not able to keep them in sync after creation.

We are looking into using the new Wix E-commerce API to provide this functionality in future releases.

How do I edit the API permissions?
************************************

If you want to edit the permissions in your API-key, please follow these steps:

#. On your Wix account. Open the `Wix API Keys Manager <https://manage.wix.com/account/api-keys>`_ .
#. Click the three dotted button on the API-key you want to edit.
#. Click **Edit**.
#. We suggest the following permissions: Under **All site permissions** choose **Wix Stores** and **Wix Contacts & Members**.
#. Click **Save & Close**

.. image:: images/edit-permissions-api-key-wix.png
    :width: 100%
    :align: left
    :alt: Edit Wix API-Key



