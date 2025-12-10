:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.10 Assignment
###############

Now that you understand the basics of the ROS2 elements, you can 
create a robot that will act like a dumb vacuum cleaner. You should 
have all the ingredients needed to build this:

1. In your training workspace, create a new package called 'vacuum_cleaning'.
2. Create a node that subscribes to the Range data from the left ultrasonic sensors, 
   and publishes to the Twist message.
3. The logic of your vacuum cleaning can still be dumb: if range < 30, turn around. 
   Please note that turning around is not a function and will definitely not be a 
   perfect 180 degrees.





