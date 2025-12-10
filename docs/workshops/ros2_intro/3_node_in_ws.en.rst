:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.3 Node in ROS2 workspace
##########################

In the previous section you just started the node which connected 
to the ROS2 API (rclpy), but the node itself can not be found by ROS2.
So that was for sure not the preferred ROS-way fo doing it. This also
means we cannot start the node with ‘ros2 run’. In order to do so, we 
first need to create a ROS2 workspace and then a ROS2 package.

Creating a ROS2 workspace usually is a folder with _ws as appendix. So 
we can just create one in our home directory:

.. code-block:: console
   :class: margin
   :emphasize-lines: 1,2

        training_ws/
      >    src/

.. code-block:: console

   $ mkdir -p ~/training_ws/src
   $ cd ~/training_ws/src

We can put all packages we want to use for this project in this src 
(source) directory. The easiest way to do so is using the ‘ros2 pkg’ 
command. With this command we can create our first ROS package:

.. code-block:: console
   :class: margin
   :emphasize-lines: 3,4,5,6,7

        training_ws/
      >    src/
              my_package/
                 CMakelist.txt
                 setup.py
                 package.xml
                 my_package/

.. code-block:: console

  $ ros2 pkg create --build-type ament_python my_package

This will create a Python package for us. Usually you will also include
the licensing information, and ROS dependencies, but for now, we will just 
create a minimal package. This will create a folder ‘my_first_package’ with 
all the files and folders needed.

.. admonition:: info

   In this training we are using python. In future projects you might also
   want/need to develop in C++. To setup a C++ package you can run the 
   command:

   .. code-block:: console

      $ ros2 pkg create --build-type ament_cmake my_package

Usually this is where you will create your own nodes. But since we already 
created one, we just need to copy this one in:

.. code-block:: console
   :class: margin
   :emphasize-lines: 8

        training_ws/
      >    src/
              my_package/
                 CMakelist.txt
                 setup.py
                 package.xml
                 my_package/
                    my_node.py

.. code-block:: console

  $ mv ~/my_node.py ~/training_ws/src/my_package/my_package

Now that we have all files in place, we still need to create an entry point
in setup.py. By doing so the package knows which functions can be used 
as entry points. In our case this should be the main() function in the my_node.py
file. To do so you have to add this line to the setup.py:

.. code-block:: python
   :emphasize-lines: 3

   entry_points={ 
     'console_scripts': [
        'my_first_node = my_package.my_node:main'
     ],
   }

The only thing we still want to do is build this whole package, which needs to be
done from the workspace:

.. code-block:: console
   :class: margin
   :emphasize-lines: 2,3,4

      > training_ws/
           build/
           install/
           log/  
           src/
              my_package/
                 CMakelist.txt
                 setup.py
                 package.xml
                 my_package/
                    my_node.py

.. code-block:: console

   $ cd ~/training_ws
   $ colcon build --symlink-install
   
.. admonition:: info

   The --symlink-install is not necessary, but very useful in a development
   context. This ensures that you do not have to run this on every modification
   of your Python script.

.. admonition:: warning

   You might get an error/warning about setuptools. You can ignore this one. It is
   a known issue in ROS Humble, but only a warning.

This will generate a build, install and log folder in your workspace. In order to 
‘activate’ this workspace we also need to source this:

.. code-block:: console

   $ source ~/training_ws/install/setup.bash

Now we have everything in place to really run the same node again, but now using 
‘ros2 run’:

.. code-block:: console

   $ ros2 run my_package my_first_node

Please note that the setup.py renamed the nodename to my_first_node, even though
the name in my_node.py is my_node. 
