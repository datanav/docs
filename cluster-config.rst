=====================
Cluster Configuration
=====================

A single Sesam Node is a fully functional service for collecting, storing, tramsforming and deliverying data. However some workloads can benefit from multiple nodes running at the same time. These nodes could be on different machines, or be working with different data. When running multiple nodes it would still be nice to access them as though they were a single Sesam service instance.

It is possible to configure a Sesam Node to act just as a Sesam API node. In this mode it is configured to sit in front of a number of Sesam nodes and expose a unified API across them all.

The Sesam API Node needs to be told about all the nodes that it should connect to. The configuration file for the Sesam API Node will look like this (minus the linenumbers)::


    01.  [
    02.     {
    03.        "_id": "apiconfig",
    04.        "type": "apiconfig:main",
    05.        "endpoints": {
    06.            "node1": {
    07.                "url": "http://subnode1:9042"
    08.            },
    09.            "node2": {
    10.                "url": "http://subnode2:9042"
    11.            }
    12.        }
    13.    }
    14. ]

The Sesam Node configuration file normally contains a list of configuration entities. In this case, the list starts
at line (01), ends on line (14) and contains only one entity. This entity is of type "apiconfig:main" (04) and has the
"_id"-value "apiconfig" (03).

The Sesam API Node gets told about the other nodes with the "endpoints" object (05). This object maps from unique
endpointids ((06) and (09)) to the information the Sesam Api Node needs in order to connect to the endpoint. In this case
only the "url" ((07) and (10)) is needed.

We can demonstrate this functionality by creating two "normal" Sesam Nodes and one Sesam API Node that connects to
both the normal Sesam Nodes.

First, create the configuration files for the three nodes::

    $ mkdir apinodetest
    $ cd apinodetest
    $ mkdir --parents subnode1/conf
    $ echo '[]' > subnode1/conf/nodeconfig.json
    $ mkdir --parents subnode2/conf
    $ echo '[]' > subnode2/conf/nodeconfig.json
    $ mkdir --parents apinode/conf
    $ echo '
        [
            {
                "_id": "apiconfig",
                "type": "apiconfig:main",
                "endpoints": {
                    "node1": {
                        "url": "http://subnode1:9042"
                    },
                    "node2": {
                        "url": "http://subnode2:9042"
                    }
                }
            }
        ]
        ' > apinode/conf/nodeconfig.json

Then, start a new "sesam/sesam-node" docker container for each of the node-configs. Note that the docker container for
the Sesam API Node must be linked to the docker container of the two normal nodes::

    $ docker run -d --name subnode1 -v $(pwd)/subnode1:/sesam sesam/sesam-node
    $ docker run -d --name subnode2 -v $(pwd)/subnode2:/sesam sesam/sesam-node
    $ docker run --rm --name apinode -p 9042:9042 --link subnode1 --link subnode2 -v $(pwd)/apinode:/sesam sesam/sesam-node

Now you should be able to open the url "http://localhost:9042". The response from this url is a json-object that looks
something like this::

    {
        "_id": "http://b940ed31b36c:9042/SERVICE_SUBJECT_IDENTIFIER_has_not_been_set",
        "endpoints": {
            "node1": {
                "_id": "http://d04d742bc44d:9042/SERVICE_SUBJECT_IDENTIFIER_has_not_been_set",
                "status": {
                    "version": "0.1"
                }
            },
            "node2": {
                "_id": "http://ee6002797bdd:9042/SERVICE_SUBJECT_IDENTIFIER_has_not_been_set",
                "status": {
                    "version": "0.1"
                }
            }
        },
        "status": {
            "version": "0.1"
        }
    }

It may take a minute or two for the Sesam API Node to read its configuration, so if the endpoints don't show up at once
try again in a minute.

When you are done, press Ctrl+C to stop the apinode docker container, stop and remove the two other docker containers and
delete the "apinodetest" folder::

    $ docker stop subnode1 subnode2
    $ docker rm subnode1 subnode2
    $ cd ..
    $ sudo rm -rf apinodetest

