:orphan:

.. _getting-started-upload-baseline-configuration:

Upload baseline configuration
-----------------------------

.. warning::

  Please note that uploading a config, as described below, **will overwrite** any existing config on the subscription. 

  We recommand that you use your `private subscription <tutorial-signup.html#set-up-a-private-subscription>`__, or create a dedicated subscription for the purpose of this tutorial.

#. Download the :download:`getting-started-config.json<files/getting-started-config.json>` and save it locally on your computer.
#. Open your subscription on the Sesam portal. 
#. Choose **Datahub** from the left menu and select the tab called **Tools**.
#. Upload the getting-started-config.json file through the drag & drop interface. 
#. Navigate to the **Variables** tab and paste the code below as environment variables.

.. code-block:: json
  :linenos:

  {
    "node-env": "test",
    "pump-mode": "manual",
    "udir-baseurl": "https://data-nxr-fellestjeneste.udir.no/api/%s"
  }

You should now have several pipes available in the **pipes** tab. 

|

Populate the subscription
-------------------------

Do the following on the pipe tab to populate your subscription:

#. Select all pipes and click the **Enable** button. This will populate the input pipes' datasets with test data.

#. Click the **Start** button. This will make the rest of the pipes run to make the data flow downstream and populate the subscription. 

#. You can click on a pipe in the list to see details on how it's configured.

|

Config contents
---------------

Your subscription now contains 8 input pipes:

- 6 pipes have embedded person data.
- 1 pipe has postal codes.
- 1 pipe has embedded orders from a webshop.

In addition there is:

- 1 merge pipe for person data.
- 2 global pipes.
- 2 example pipes for modelling and exporting person address data.

Have a look at how the pipes are connected by navigating between them through their Graph-tabs. The "merged-person" pipe is a good place to start.


..
  .. image:: images/getting-started/importdata.png
      :width: 800px
      :align: center
      :alt: Generic pipe concept