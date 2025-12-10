:orphan:

Line following
################################

.. article-info::
    :author: :fa:`brain` Programming
    :read-time: 30 min

1
---

By now you should have a good understanding of the capabilities of the robot.
In this workshop you will put this knowledge together and follow a line. That
could be the starting point for competing in a RoboCupJunior competition.


2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      In the 'Measuring light' workshop you have learned when the sensor sees
      a black line, and when it doesn't. You can use these values to determine
      what your robot should do. To do so, you need to create a program (also
      called algorithm) that does this.

      There are multiple ways of creating this program. It might help to have
      a look at this picture. What should the robot do if it sees black? What
      should the robot do if it sees white? You can also use the functions
      you created in the previous workshop.

      Since we are only using 1 sensor, we are actually going to follow the
      left or the right side of the line. You are mostly checking whether
      the sensor is on the line or not. The example in this image follows the
      right side of the line.

   .. grid-item::

      .. image:: _media/mirte_line_1_sensor_theory.png
         :width: 350
         :alt: Mirte sensor on a line


.. dropdown:: :fa:`question-circle` Help

   - I do not know what to do:
      - You computer program could be someting like: turn right if you see black, turn
        left if you see white.
   - How can I determine the perfect values:
      - You are trying to see the difference between black and white. You can use the
        measurement for black, and the measurement for white. The best value to use is
        the one in between these two values.
   - The robot worked just now/yesterday, but it fails to work now. And I made no changes:
      - The sensor measures the value of the surface. But the actual value it measures
        can still depend on lots of things. Did the lighting condition change? Are there
        clouds? Can you close the curtains?
