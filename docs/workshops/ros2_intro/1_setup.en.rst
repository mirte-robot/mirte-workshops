:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.1 Setup
#########

In this training we will use Ubuntu to run ROS2 on. This means we have
already installed Ubuntu 22.04 and ROS Humble (ros-humble-desktop) for
you on the laptop. But during this training we will also develop a lot
of our own ROS packages and nodes. To be able to do so, you need to install
ros-dev-tools as well:

.. code-block:: console

  $ sudo apt install ros-dev-tools

And we need to ‘activate’ ROS by sourcing it. Note that you need to do
this in each terminal you will be using:

.. code-block:: console

  $ source /opt/ros/humble/setup.bash
