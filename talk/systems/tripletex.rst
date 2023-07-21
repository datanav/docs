.. _talk_tripletex:

Tripletex
=========
 
`Tripletex <https://tripletex.no>`_ is a simple-to-use modular accounting system that helps businesses deal with invoicing, salaries, timetracking, yearly reports and more.

.. panels::
    :body: text-left
    :container: container-lg pb-3
    :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    **Making Tripletex Talk**

    Easily synchronise valuable data between Tripletex and your other systems.
    

    .. link-button:: https://tripletex.talk.market
        :type: url
        :text: Try for free
        :classes: btn-primary btn-block


Find your employee token
------------------------
The employee token can be created by the account administrator in Tripletex under the User Settings page, then in the tab "API access" 

Follow these steps to create your employee token:

#. Enable integrations in Tripletex
#. Navigate to the API-access tab and create a new key choose tilpasset oppset/adapted setup
#. Choose All entitlements and write "SesamTalk" into application name field
#. Name your token
#. Go back and paste the employee token into the API Key field in Sesam Talk

For more information please `read this documentation <https://hjelp.tripletex.no/hc/en/articles/4409557117713>`_

Using test accounts in Tripletex
--------------------------------
If wish to connect a Tripletex test account, please follow `these instructions <https://developer.tripletex.no/docs/documentation/getting-started/1-creating-a-test-account/>`_ .

You will be provided with your employee and consumer token as part of creating the test account. 


.. jinja:: talk_system_tripletex
  :file: _jinja/system_mapping.jinja

Known issues
------------
No known issues.
