Combine all and webhook events
==============================
When combining the ``-all`` and ``-event`` datasets, one should use the ``merge_datasets`` source as it will pick the version of the entity that has the most recent change. The ``-collect`` will with this pattern be the most representative copy we can get of the external data.