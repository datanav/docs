Partial webhook events
======================

Need to do a lookup to find the complete entity. Avoid doing the look up in the pipe that receives the event, as the lookup can take time and block the receiver. Instead set up a pipeline with two pipes and call the second one ``-event2``.