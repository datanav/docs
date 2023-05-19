.. _microservice_system:

Microservice system
-------------------

The microservice system is similar to the :ref:`URL system <url_system>`, except that it also spins up the microservice that it defines. This system can be used with the :ref:`JSON source <json_source>`, the :ref:`HTTP transform <http_transform>` and the :ref:`JSON push sink <json_sink>`.

The ``docker`` property lets one specify a Docker container that should be spun up. Note that the microservice system does not have the ``base_url`` property. The reason is that it is able to figure out this itself.

The microservice system supports private repositories.

A microservice must communicate with the outside world using either the ``HTTP`` protocol (the default) or the ``HTTPS`` protocol. Set the ``use_https`` property to ``true`` to enable ``HTTPS``.

The system provides session handling, connection pooling and authentication services to sources, transforms and sinks which need to communicate with the microservice.

.. _microservice_system_resource_quotas:

Resource quotas
^^^^^^^^^^^^^^^

The table below shows the total resource quotas available for the microservices per subscription type. These quotas are currently not enforced, but might they be in the future.

.. list-table::
   :header-rows: 1
   :widths: 30, 40, 30

   * - Subscription type
     - Memory quota
     - CPU quota

   * - ``developer``
     - 1GB RAM
     - 0.25 CPU

   * - ``developer-pro``
     - 4GB RAM
     - 0.75 CPU

   * - ``single``
     - 8GB RAM
     - 1 CPU

   * - ``multi``
     - 16GB RAM per compute
     - 2 CPUs per compute


Prototype
^^^^^^^^^

::

    {
        "_id": "id-of-microservice",
        "name": "Name of microservice",
        "type": "system:microservice",
        "docker": {
            "image": "some-repo/some-image:some-tag",
            "port": 5000,
            "username": null,
            "password": null,
            "memory": 128,
            "cpu_quota": 25,
            "cpu_period": 100,
            "cpuset_cpus": null,
            "environment": {
                "SOME-VARIABLE": "SOME-VALUE",
                "OTHER-VARIABLE": {
                    "key1": "value1",
                    "key2": "value2"
                }
            },
            "hosts": {
                "myhost1.mydomain.io": "157.240.20.34",
                "myhost2.mydomain.io": "157.240.20.35"
            },
            "skip_pull": false,
            "pull_image_cron_expression": "0 0 * * *"
        },
        "use_https": false,
        "verify_ssl": false,
        "username": null,
        "password": null,
        "authentication": "basic",
        "connect_timeout": 60,
        "read_timeout": 1800,
        "eager_load": true
    }

Note that due to Docker naming conventions, the ``_id`` of the microservice must start with a ASCII letter or number
character and the only non-letter or number characters allowed in the rest of the string are "_" and "-".

The microservice ``_id`` is exposed as domain names in the local network and is thus subject to domain name rules:
the maximal size of an id is 63 characters and the minimal size is 2 characters.

It should also contain only lower-case letters to avoid DNS lookup errors when used via by HTTP requests,
for example in a URL system or via its proxy API.

Properties
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 10, 10, 60, 10, 3

   * - Property
     - Type
     - Description
     - Default
     - Req

   * - ``docker.image``
     - String
     - The fully qualified name of a Docker image, e.g. ``sesam/file-share-service:latest`` or ``quay.io/someuser/someimage:1.2.3``. If the image name does not contain a fully qualified domain name it will default to assuming dockerhub.
     -
     - Yes

   * - ``docker.port``
     - Integer
     - The port on which to talk to the microservice. This should be one of the ports that the Docker container exposes.
     -
     - Yes

   * - ``docker.environment``
     - Dict<String,String|Object>
     - The environment variables that should be passed to the microservice's Docker container. Note that string
       literals are passed along to the docker container as-is, while other types of values are serialized to a string
       in JSON format.
     -
     -

   * - ``docker.username``
     - String
     - If the Docker images is located in a private repository, then the username must be specified here.
     -
     -

   * - ``docker.password``
     - String
     - If the Docker images is located in a private repository, then the password must be specified here.
     -
     -

   * - ``docker.memory``
     - Integer
     - The number of MB of RAM to allocate for the microservice.
     - ``128``
     -

   * - ``docker.cpu_quota``
     - Integer
     - The percentage of CPU resources the container is allowed to consume. *Use with extreme care* as you can easily
       starve other processes on the server for resources if you set this value incorrectly or suboptimally. See
       `the Docker documentation <https://docs.docker.com/engine/reference/run/#cpu-period-constraint>`_ for details).
       Note that the value is divided by 1000 with respects to the range in the Docker documentation. Also note that
       the value represents the *sum* of CPU resources used across *all cores*. If the container is allowed to use more
       than one CPU (by default it can use all of them) the number can exceed 100. I.e. for a 4 core CPU, 400 means
       use all resources on all CPU cores.
     - ``25``
     -

       .. _microservices_system_docker_hosts:
   * - ``docker.hosts``
     - Dict<String,String>
     - A mapping between domain names/hostnames and IP adresses. These custom hostnames will be resolvable inside the microservice container.
     - ``{}``
     -

   * - ``docker.skip_pull``
     - Boolean
     - If set to true then the system will will never try to pull a new version of the docker image. If this is
       set to false (the default), the system will attempt to pull a new version of the docker image every time
       the microservice docker container is restarted (for instance when a new config has been specified).
     - ``false``
     -

   * - ``docker.pull_image_cron_expression``
     - String
     - A cron expression that indicates when the system will attempt to pull a new version of the docker image.
       If a newer version of the docker image is pulled, the microservice docker container will restart.
     - ``null``
     -

   * - ``use_https``
     - Boolean
     - If set to true then the system will use the ``https`` protocol to communicate with the microservice.
     - ``false``
     -

   * - ``verify_ssl``
     - Boolean
     - Indicate to the client if it should attempt to verify the SSL certificate when communicating with the
       microservice over SSL/TLS.
     - ``false``
     -

   * - ``username``
     - String
     - The username to use when authenticating with the microservice. Note that you also have to specify
       authentication protocol in ``authentication`` and ``password`` for this property to have any effect.
     -
     -

   * - ``password``
     - String
     - The password to use if ``username`` and ``authentication`` is set. It is mandatory if ``username`` is provided.
     -
     - Yes*

   * - ``authentication``
     - String
     - What kind of authentication protocol to use. Note that authentication is opt-in only and the default is no
       authentication. No authentication set means means any ``username`` or ``password`` set will be ignored.
       Allowed values is either "basic" or "digest".
     -
     -

   * - ``connect_timeout``
     - Integer
     - Number of seconds to wait for connecting to the microservice before timing out.
     - ``60``
     -

   * - ``read_timeout``
     - Integer
     - Number of seconds to wait for the microservice to respond to a request before timing out.
     - ``1800``
     -

   * - ``eager_load``
     - Boolean
     - When set to false, Sesam can hold off starting up the microservice if it isn't connected to any pipes. Set to true to force the microservice to start up regardless. Overrides setting in :ref:`service metadata <service_metadata_global_defaults_eager_load_microservices>`.

       .. NOTE::

          The default value is ``false`` for developer subscriptions.
     - ``true``
     -

Documentation for deprecated properties can be found :ref:`here <microservice_system_deprecations>`.


Microservice APIs
^^^^^^^^^^^^^^^^^

The Microservice system exposes several API endpoints that can be used to access or gather information about the running
service:

* `Logs endpoint <./api.html#get--systems-system_id-logs>`_ - exposes the service's logs
* `Status endpoint <./api.html#get--systems-system_id-status>`_ - runtime information about the provisioned service
* `Reload endpoint <./api.html#post--systems-system_id-reload>`_ - pull new docker image and reload the microservice
* `Proxy endpoint <./api.html#get--systems-system_id-proxy--path-relative_path->`_ - proxy for the microservice URL through the node API

Example configuration
^^^^^^^^^^^^^^^^^^^^^

::

    {
        "_id": "our-http-server",
        "name": "My microservice",
        "type": "system:microservice",
        "docker": {
            "image": "myrepo/myimage:1.0",
            "port": 4444,
            "environment": {
               "USE_PORT": "4444"
            }
        }
    }
