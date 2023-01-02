.. _custom_data_transform:

===========================
Creating a Custom Transform
===========================

:ref:`DTL <dtl_transform>` and the other :ref:`transform types <transform_section>` provide support for the majority
of data transformation use-cases. However, there are times when a special kind of transform needs to be performed. In these
cases it is possible add a customized transform. Typically, this is a transform where some external service should be contacted in order to convert a value or to import data based on entity specific information. :ref:`Optimistic locking <optimistic_locking>` is an example of a Sesam pattern based on a custom transform. 

Much like the :ref:`Custom Data Source <custom_data_source>` a custom transform can be connected to either an existing endpoint supporting Sesam protocols, or to a microservice.  

The custom transform is generally configured as an :ref:`HTTP transform <http_transform>` connected to either a :ref:`URL system <url_system>` or a :ref:`Microservice system <microservice_system>`. This is defined as part of the transformation pipeline of a :ref:`pipe <pipe_section>`.

The service that data is sent to as part of this transform is where the custom code should reside. 

The set of transforms is wrapped in an array, and in this case the first transform sends the pipe's source entities to the custom transform which in turn sends them to an other transform which copies all the returned data and adds a ``_id`` property. 

Custom Transform - The HTTP transform
-------------------------------------

In the following configurations we will see how the :ref:`HTTP transform <http_transform>` in combination with the :ref:`URL system <url_system>` can be used to create a Custom Data Transform. In the example below we show an example of an HTTP transform connected to a Microservice system. 

.. code-block:: json
  :linenos:

    {
      "_id": "custom-transform-pipe",
      "type": "pipe",
      "source": {
        "type": "dataset",
        "dataset": "my-dataset"
      },
      "transform": [{
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "foo", "_S.some-attribute"]
          ]
        }
      }, {
        "type": "http",
        "system": "custom-transform-microservice",
        "url": "/some-endpoint"
      }, {
        "type": "dtl",
        "rules": {
          "default": [
            ["copy", "*"],
            ["add", "_id", "_S.some-property"]
          ]
        }
      }]
    }

    {
      "_id": "custom-transform-microservice",
      "type": "system:microservice",
      "docker": {
        "environment": {
          "some-other-variable": "some-other-value",
          "some-variable": "some-value"
        },
        "image": "my-image-url",
        "port": 5000
      }
    }

In addition to the information on :ref:`Microservices in Sesam <microservices_in_sesam>`, following microservice template projects for common languages are provided.

    - The `Python template <https://github.com/sesam-io/python-transform-template>`__. Requires Python 3 and uses the `Flask <http://flask.pocoo.org>`_ framework.

The transform will stream an array of JSON objects to the registered endpoint and expect back a list of entities. The result of the HTTP transform is passed along the transformation pipeline and into the pipe's sink.

|

.. panels::
    :body: text-left
    :container: container-lg-12
    :column: col-lg-6 p-1

    :badge:`Tutorials, badge-success text-white`
    
    **Custom Data Source - The HTTP Transform**

    Look closer into how to create a custom data transform with a microservice. 

 
    .. link-button:: tutorial-custom-data-transform-http-transform.html
        :type: url
        :text: Start tutorial
        :classes: btn-all-sections btn-all

|