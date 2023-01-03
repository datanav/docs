.. _api_config_groups:

:badge:`Free feature,badge-success badge-pill`

Config groups
=============

There are multiple ways to configure a sesam-node. One way is to add and modify single systems and
pipes via these endpoints:

`/api/pipes/{pipe_id}/config GET <./api.html#get--pipes-pipe_id-config>`_

`/api/pipes/{pipe_id}/config PUT <./api.html#put--pipes-pipe_id-config>`_

`/api/systems/{systems_id}/config GET <./api.html#get--systems-system_id-config>`_

`/api/systems/{systems_id}/config PUT <./api.html#put--systems-system_id-config>`_

Another way is to upload the configuration for multiple systems and pipes as via these endpoints:

`/api/config GET <./api.html#get--config>`_

`/api/config PUT <./api.html#put--config>`_

`/api/config/{config-group} GET <./api.html#get--config-config-group>`_

`/api/config/{config-group} PUT <./api.html#put--config-config-group>`_

Regardless of which endpoint is used, each pipe or system is placed in a **config-group**. For the first set of
of endpoints the config-group is specified by adding a "$config-group"-property to the "metadata"-property in
the configuration. Example::

    {
      "_id": "testpipe",
      "type": "pipe",
      "metadata": {
        "$config-group": "my-first-group"
      }
    }

For the second set of endpoints the config-group is specified in the url. In either case, if no config-group is
explicitly given, the pipe/system is placed in the "default" config-group (i.e. the `/api/config PUT <./api.html#put--config>`_
endpoint places the uploaded config into the "default" config-group).

Note: The `/api/config PUT <./api.html#put--config>`_ and `/api/config/{config-group} PUT <./api.html#put--config-config-group>`_
endpoints will replace **all** the config in the specified config-group.