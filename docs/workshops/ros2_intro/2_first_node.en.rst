:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.2 First ROS2 node
###################

To get your first node running, it helps to shutdown all the nodes
that are started by default on the MIRTE robot. This can be done by
typing in the terminal:

.. code-block:: console

   $ sudo systemctl stop mirte-ros

This will shutdown all MIRTE-related ROS nodes.

As you’ve seen in the presentation, one of the core elements of ROS2
are nodes. These are just small executables that connect with the ROS2 
API. In this tutorial you will learn how to create your first ROS node.
In VSCode you can open a new file and save the following code as
my_node.py:


.. code-block:: python
  :linenos:

  import rclpy
  from rclpy.node import Node

  def main():
    rclpy.init()
    my_node = Node('hello_world_node')
    my_node.get_logger().info("Hello world")
    try:
       rclpy.spin(my_node)
    except KeyboardInterrupt:
       return

  if __name__ == '__main__':
    main()

You can now run this program by typing the following in the terminal:

.. code-block:: console

   $ python3 my_node.py

You should see the string 'Hello world' being printed on the screen once.
If you did it correctly the node is still spinning, so the 
terminal is still busy. You can check that the node is indeed 
running by opening another terminal ():

.. code-block:: console
   :class: margin

   /hello_world_node
   
.. code-block:: console

   $ ros2 node list

This should give you the name of the node ('hello_world_node') as set
in line 6. Congratulations, you have your first ROS2 node running. But 
this is not the best way of doing this.

.. dropdown:: :fa:`question-circle` Help

   - I get the error 'No module named rclpy':
       - Please make sure that you have installed ros-dev-tools. 
   - I get the error 'ros2 not found':
       - Make sure that you have sourced ROS2.
