:html_theme.sidebar_secondary.remove:

.. toctree::
   :maxdepth: 0
   :hidden:

   self
   1_viewing_pointcloud_data
   2_listener_to_pointcloud_topic
   3_converting_to_PCL_datatypes
   4_downsampling_PCL_datatypes
   5_publishing_filtered_pointcloud
   6_using_other_PCL_functions

Welcome
=======

In this workshop we will use the `MIRTE Master <https://mirte.org/>`_ 
robot. After this workshop you will be able to understand the basics of using
the Point Cloud Library (PCL) in ROS2.

**Prerequisites**

.. tab-set::

   .. tab-item:: VSCode on computer

      If you have not installed VSCode yet, please do wo following the instructions below:

      - `Installing VSCode <https://code.visualstudio.com/download>`_

   .. tab-item:: VSCode on MIRTE

      No need to install anything. But please note that developing on VSCode on the robot
      might be a bit slow.


**Preparations**

Before we start you have to install a couple of ROS2 packages. As this migth take
some time, it is usefull to already start doing this, while you can continue with
the workshops.

Make sure the robot is `connected to the internet <https://docs.mirte.org/develop/doc/mirte_os/connect_to_mirte.html#wireless-client-mode>`_.
Please make sure that you are not using your mobile data as we are going to install
a lot of data. And login to the robot through ssh and install the packages:

.. code-block:: console

   $ ssh mirte@<robot-ip>
   mirte$ sudo apt update
   mirte$ sudo apt install ros-humble-pcl-ros





