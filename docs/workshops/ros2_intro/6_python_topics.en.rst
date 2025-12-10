:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.6 Subscribing to topics in Python
###################################

Printing the data from a topic in the commandline might be useful for 
debudding purposes, but with that you will not be able to program 
your robot. For this we need to use the ROS2 Python or C++ API. In
order to connect to this topic from our own node, we need to have some 
more information of this topic. We already have the name 
(‘/mirte/distance/left’), but we also need to know the data type (what 
kind of information is it sending.

.. code-block:: console
   :class: margin

   /sensor_msgs/Range


.. code-block:: console
 
   mirte$ ros2 topic type /mirte/distance/left


.. admonition:: info

   ROS already has lots of predefined message types which are commonly
   used in robots. For example:
   
   - std_msgs: All kinds of standard basic types like Int, Float, etc.
   - sensor_msgs: All kinds of sensor types like Range, Image, etc.
   
   You can find a list of all common interfaces `here <https://github.com/ros2/common_interfaces>`_.
   
This shows us that is of type sensor_msgs/Range. But let’s also have a 
look at how this data is organized:

.. code-block:: console
 
   mirte$ ros2 interface show sensor_msgs/msg/Range

Please note the extra ‘msg’ part. This could be found by listing all interfaces 
($ ros2 interface list). We can now see that the data we are interested in is 
in Range.range, which we could also see when we echo’d the topic. Now that we have both 
the type and the name, we can create our own node which listens to this data. 
Create a new node in your package and run it:

.. code-block:: python
  :linenos:
  :emphasize-lines: 3, 9, 10

  import rclpy
  from rclpy.node import Node
  from sensor_msgs.msg import Range

  class SubscriberExampleNode(Node):
     def __init__(self):
        super().__init__("subscriber_node")
        self._subscription = self.create_subscription(
           Range,
           "/mirte/distance/left",
           self.receive_message_callback,
           1
        )

     def receive_message_callback(self, message):
        self.get_logger().info("I got range: " + str(message.range))

  def main():
     rclpy.init()
     my_subscriber_node = SubscriberExampleNode()
     try:
        rclpy.spin(my_subscriber_node)
     except KeyboardInterrupt:
        return

.. code-block:: console
   :class: margin

   [INFO] [1715670084.126321319] [subscriber_node]: I got range: 20.0

Since we ran colcon with --symlink-install, there is no need to :abbr:`build it again ($ros2 colcon build)`. So we can right away :abbr:`start the node ($ros2 run my_package my_first_node)`. And if you like to, you can also see the ROS system using :abbr:`rqt_graph ($ ros2 run rqt_graph rqt_graph)`.






