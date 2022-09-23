Late schema binding
-------------------
Ensure that transformations are done in accordance to the target schema. Bidirectional sync might not support patching, and you need the original object when sharing. When mapping, only use the namespace of the target system or the global namespace. Hops should be done on global properties. Use identifiers from the target system. If you reference other namespaces, you can no longer do all refactoring in the connect phase.
