:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.7 Commandline services
########################

Apart from topics, nodes can also commnicate through services.
There are two main differences between topics and services. For one,
topics only communitcate in one direction (from one node to another),
while services can comminucate in two directions (back and forth between
nodes). The other difference is that services are 'blocking', which
means that the node calling the service has to wait for the other node
to respond.

Like with topics, you can also commincate with services usign the 
commandline. For the next steps, you need to make sure the MIRTE
telemetrix node is running, and if this is not the case 
:abbr:`start it ($ sudo systemctl start mirte-ros)`.

First we can have a look which services are active in the ROS system:

.. code-block:: console
 
   mirte$ ros2 service list

.. admonition:: warning

   When you want to drive around with the robot, please make sure that
   the robot is either on the groud, or unable to drive from the table.
   
One of the services is called '/io/motor/front_left/set_speed', which will set 
the speed of the left motor (values range from -100 to 100). You
can set the speed of the motor:

.. code-block:: console
   :class: margin
   
   requester: making request: mirte_msgs.srv.SetMotorSpeed_Request(speed=50)

   response:
   mirte_msgs.srv.SetMotorSpeed_Response(status=True)

.. code-block:: console
 
   mirte$ ros2 service call /io/motor/front_left/set_speed mirte_msgs/srv/SetMotorSpeed "{speed: 50}"

.. admonition:: warning

   This will start the motor, and probably also stop the motor. This is because
   ROS2 control is also controlling the robot, and did not get a command, so it
   actively tries to stop it. You can disable this controller with:

   .. code-block:: console
 
      mirte$ ros2 control switch_controllers --deactivate  mirte_base_controller

This will set the motor speed to 50% forward. You will probably want to
set the speed back to 0 againg to stop the motor.



