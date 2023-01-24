import json
import os.path

def render(system):
    id = system["_id"]
    label = system["label"]
    description = system["description"]
    url = system["url"]
    label_underline = "="*len(label)
    return f""".. _talk_{id}:

{label}
{label_underline}

{description}

{url}


.. jinja:: talk_system_{id}
   :file: _jinja/system_mapping.jinja

Known issues
------------
No known issues."""

with open("_data/talk_systems.json") as s:
    systems = json.load(s)
    for system in systems:
        id = system["_id"]
        filename = "talk/systems/%s.rst" % id
        if not os.path.exists(filename):
            with open(filename, 'wt', encoding='utf-8') as f:
                f.write(render(system))