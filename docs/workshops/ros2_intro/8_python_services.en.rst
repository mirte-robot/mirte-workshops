:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.8 Calling a service in Python
###############################

Although calling the services from commandline might be useful for
debuggin perposes (like with the topics), it is more useful to
be able to call services from the ROS2 Python or C++ API. 

Like with the service we first need to find out the type of the service
message. Although the :abbr:`commandline command ($ ros2 service call /mirte/set_right_speed mirte_msgs/srv/SetMotorSpeed "{speed: 0}")` already needed it, you can 
still get the type: 

.. code-block:: console
   :class: margin

   mirte_msgs/srv/SetMotorSpeed


.. code-block:: console
 
   mirte$ ros2 service type /mirte/set_right_speed

And like the services, we can also have a look at how the interface
itself is defined. 

.. code-block:: console
   :class: margin

   int32 speed
   ---
   bool status
   
.. code-block:: console
 
   mirte$ ros2 interface show mirte_msgs/srv/SetMotorSpeed

As you can see, there is a difference with the interface we used for
topics. The topics just used a message type containing data. The 
interface for services also contain the direction of this data. In this
case the service gets a speed (as int32) as input and returns a status
(as bool). 

Now that we have all the ingredients to call this service from python. Since
we do not want to get rid of the previous node that subscribed to the
sensordata, we can make another node to call the setSpeed service. As a 
reminder, this involves:

.. code-block:: console
   :class: margin
   
   [INFO] [1715679971.177088773] [client_example_node]: Initialized example client
   [INFO] [1715679971.189915283] [client_example_node]: Response: True

1) :abbr:`Creating a new node called service.py (in ~/training_ws/src/my_package/mypackage)`
2) Put the code below in that file
3) :abbr:`Adding this node to setup.py (in ~/training_ws/src/my_package/setup.py)`
4) :abbr:`Build everything ($ cd ~training_ws && colcon build --symlink-install)`
5) :abbr:`Start the node ($ ros2 run my_package <the name you've put in setup.py>)`

.. code-block:: python
  :linenos:
  :emphasize-lines: 3, 9, 10

  import rclpy
  from rclpy.node import Node
  from mirte_msgs.srv import SetMotorSpeed

  class ClientExampleNode(Node):
     def __init__(self):
        super().__init__("client_example_node")
        self._client = self.create_client(
           SetMotorSpeed, 
           "/mirte/set_left_speed")

        while not self._client.wait_for_service(timeout_sec=10.0):
           self.get_logger().info("Service not available")

        self.get_logger().info("Initialized example client")

     def send_request(self, request):
        future = self._client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

  def main():
     rclpy.init()
     client_node = ClientExampleNode()
     request = SetMotorSpeed.Request()
     request.speed = 50
     response = client_node.send_request(request)
     client_node.get_logger().info("Response: " + str(response.status))
     rclpy.shutdown()
