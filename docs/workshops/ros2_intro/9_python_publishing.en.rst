:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.9 Publishing to topics
########################

Although we are able to get some sensordata (as topics) from the robot, and 
also drive around (by calling services), this might not be the ideal way
of driving your robot. In ROS the default of driving around a mobile platform
is not by calling services, but by publishing to a topic of the Twist type. As
you can :abbr:`see ($ ros2 interface show /geomerty_msgs/msg/Twist)` this interface
has two components:

.. code-block:: console
 
   Vector3  linear
        float64 x
        float64 y
        float64 z
   Vector3  angular
        float64 x
        float64 y
        float64 z
        
This message type is expressing the velocity of the robot brokin into linear and
angular speed (in m/s). For a dirrential drive robot this means we can only use
linear.x (forward/backward) and angular.z (turning around its axis).

This also means there needs to be someting (a ROS node) that is listening to a topic
with this Twist type. Usually this is a topic with 'cmd_vel' (command velocity) in its
name. Up till now, we only started the ROS telemtrix node to commuicate with the 
mictrocontroller. From now on it makes more sense to start the full MIRTE ROS system.
To do so, you first need to stop the telemetrix node by pressing CTRL-C in the terminal
where we started this node. Only then are we able to start the full MIRTE ROS system:

.. code-block:: console

   $ ros2 launch mirte_bringup minimal.launch.py
   
This will start the telemtrix node, but also some others responsible for controlling the
motors. And again you can have a look which :abbr:`nodes are running ($ ros2 node list)`,
find out that the cmd_vel topis :abbr:`is called /diffbot_base_controller/cmd_vel_unstamped
($ ros2 topic list)`.

We again have all the information we need to publish to this topic:

1) :abbr:`Creating a new node called drive.py (in ~/training_ws/src/my_package/mypackage)`
2) Put the code below in that file
3) :abbr:`Adding this node to setup.py (in ~/training_ws/src/my_package/setup.py)`
4) :abbr:`Build everything ($ cd ~training_ws && colcon build --symlink-install)`
5) :abbr:`Start the node ($ ros2 run my_package <the name you've put in setup.py>)`


.. admonition:: info

   For debugging purposes, you can again also send data to this topic from the commandline:
   
   .. code-block:: console

      $ ros2 topic pub --once /diffbot_base_controller/cmd_vel_unstamped geometry_msgs/msg/Twist "{linear: {x: 1}}"
   

.. code-block:: python
  :linenos:
  :emphasize-lines: 3, 9, 10, 17, 18

  import rclpy
  from rclpy.node import Node
  from geometry_msgs.msg import Twist

  class MinimalPublisher(Node):
     def __init__(self):
        super().__init__('drive_publisher')
        self.publisher_ = self.create_publisher(
            Twist, 
            '/diffbot_base_controller/cmd_vel_unstamped', 
            10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

     def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0  # m/s
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing linear.x: "%f"' % msg.linear.x)

  def main(args=None):
     rclpy.init(args=args)
     minimal_publisher = MinimalPublisher()
     rclpy.spin(minimal_publisher)
     minimal_publisher.destroy_node()
     rclpy.shutdown()

  if __name__ == '__main__':
     main()








