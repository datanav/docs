.. _getting-started-microservices:

Microservices
-------------
The DTL in Sesam is a powerful tool to transform our data. But sometimes we need to do something with our data that is outside the scope of the DTL. We can then create a microservice that does what we need and run it inside Sesam to serve those needs. We can also use a microservice when we need to connect to an external system where the connection point is not compatible with the Sesam source systems. The microservice can be made according to our preferences and in any language.

.. image:: images/getting-started/MS-types.jpg
    :width: 800px
    :align: center
    :alt: Generic pipe concept

As shown above, irrespective of nature or technologies of external system, we can easily connect with them using microservices to read, write and update data. Microservices add flexibility to do more with data than may be possible with DTL.

Steps
-----

.. toctree::
   :maxdepth: 1

   Creating a microservice  <tutorial-microservice-create>
   Testing a microservice  <tutorial-microservice-test>
   Publish to Docker Hub <tutorial-microservice-publish>
   Using a microservice <tutorial-microservice-use>





