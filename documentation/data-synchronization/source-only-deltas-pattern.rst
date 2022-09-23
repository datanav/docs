.. _pattern_source_only_deltas:

Source that only provides delta streams pattern
-----------------------------------------------

If you restart the pipe you lose a lot of data. Make two pipes, disable, reset and use durable pipe, disable :ref:`deletion tracking <deletion-tracking>`.