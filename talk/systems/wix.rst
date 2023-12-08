.. _talk_wix:

Wix
===

`Wix <https://wix.com>`_ website builder offers a complete solution from enterprise-grade infrastructure and business features to advanced SEO and marketing tools–enabling anyone to create and grow online.

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
#. In the Name field write the name of the API-Key, for example: Making Wave Talk.
#. Under **All site permissions** choose **Wix Stores** and **Wix Contacts & Members**.
#. Follow the steps and once you get your API-Key, also called key's token, Copy it and store it somewhere.
#. Get back to `The onboarding process <https://talk.sesam.cloud/onboarding/wix/connect>`_ 
#. Follow the steps and paste your generated API-Key.

Find your Wix Site ID
---------------------

The site ID for a current site can be obtained from the site URL in your browser. For example, the site ID appears after the **/dashboard/** part of this URL:

.. image:: images/find-site-id-wix.png
    :width: 800px
    :align: left
    :alt: Wix Site ID


Frequently Asked Questions
--------------------------

Why are not my ERP orders created in Wix?
*****************************************

The Wix API does not allow general updates of orders, so we do not write any orders as we are not able to keep them in sync after creation.
