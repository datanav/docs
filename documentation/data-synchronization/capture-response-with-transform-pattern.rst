.. _capture_response_with_transform:

Capture response with transform
-------------------------------

Use transform instead of a sink to capture results back into a dataset. This transform will have side effects and this pipe needs to be durable to avoid reprocessing in case of data loss. Batch size needs to be set to 1 to avoid duplicates as this is not transactional. Do not mix dependency tracking in this pipe as it can also cause duplicates. Avoid the preview API as this will trigger the transform.