# This file contains the general practice we use in the training part of the documentation.

## File structure

```
File structure overview. Structure is the same for each chapter.

docs/
-training/
--010_Architecture_and_Concepts/
---_include_file.rst
---010_Introduction.rst
---020_Beginner.rst
---030_Novice.rst
---040_Intermediate.rst
---050_Advanced.rst
---060_Expert.rst
---070_Epilogue.rst
---media/
----beginner-different_types_of_architecture_ESB.png
----novice-joining_data-Left_join.png
----<difficulty>-<sub_chapter>-<image_name>.png
--020_Systems/
---media/
---010_Introduction.rst
   … Same as 010_Architecture_and_Concepts.
```

## Title and headers syntax in RST.
```
Title level | Example of title for level.

=========================================
Chapter         | Architecture & Concepts
=========================================

Chapter Section | Architecture & Concepts: Beginner
---------------------------------------------------

Topic           | Different types of Architectures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Title in topic  | Point to Point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
