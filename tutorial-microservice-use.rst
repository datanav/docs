
Import to Sesam node
^^^^^^^^^^^^^^^^^^^^

Now that the Docker image has been pushed to our Docker platform we need to spin up the container in our Sesam node.

Create a new system in your node. Choose **microservice prototype** as template. Give it a proper name. Inside the **"docker"** parameter write:

::

 "docker": {
    "image": "<docker_username>/<your_repository_name>:<tagname>",
    "port":5000
 }

.. image:: images/getting-started/systemconfigms.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

Save it and click on **Status**. Click **Pull** and **restart**, then **Refresh** and **Check health**. You can also hit **Refresh** in the log so you see that it's running as it should.

.. image:: images/getting-started/system-microservice.gif
    :width: 800px
    :align: center
    :alt: Generic pipe concept

The final step is to create an inbound pipe to get all the data from our microservice into Sesam datahub. Because our dataset does not have an **"_id"** property we need to add that. We could just use a normal **["add"]** function, but as you can see from the microservice, we’ve actually just created one property as a dictionary. We really want these as three entities and that reason we use this function:

::

  ["create",
      ["apply", "create-entity", "_S.orders"]]

This creates a new rule where we can add the **"_id"**. Since the **"id"** in the microservice is an integer and Sesam only accepts string values for the **"_id"** we convert it with the **["string"]** function.

.. image:: images/getting-started/remade-pipe.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

.. image:: images/getting-started/pipe-orders-ms-output.png
    :width: 800px
    :align: center
    :alt: Generic pipe concept

