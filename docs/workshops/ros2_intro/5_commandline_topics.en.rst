:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.5 Commandline topics
######################

One of the core nodes on MIRTE is the 
mirte_telemetrix node. That node is constantly communicating with the 
microcontroller to get the latest sensordata, and control the motors. 
So we first need to start that node:

.. code-block:: console

   mirte$ ros2 launch mirte_telemetrix telemetrix.launch

.. admonition:: info

  This node migth already be running. You can check this with:

  .. code-block:: console

     $ ros2 node list

As in the previous section, you can :abbr:`check which nodes are
running (mirte$ ros2 node list)`, and confirm that the node is running.
But you can also see the data from the ultrasonic sensors coming in:

.. code-block:: console
   :class: margin
   :emphasize-lines: 11

   ---
   header:
     stamp:
       sec: 1715654039
       nanosec: 122178037
     frame_id: ''
   radiation_type: 0
   field_of_view: 15.707962989807129
   min_range: 0.019999999552965164
   max_range: 1.5
   range: 8.0
   ---

.. code-block:: console
 
   mirte$ ros2 topic echo /io/distance/left

At one of the lines, you can see the distance measured by the sensor in cm.
You can also get some other information (like bandwidth used, update
frequency, message type, and delay). You can see the full list op options:

.. code-block:: console
 
   mirte$ ros2 topic -h




