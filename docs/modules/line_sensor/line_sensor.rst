:orphan:

Measuring light
########################

.. article-info::
    :author: :fa:`eye` Sensors
    :read-time: 30 min

1
---

In order for your robot to do some smart stuff, it should be able to measure
its environment. A robot can do this buy using sensors. In this workshop you
will learn how your robot can measure light and with that can detect a
black line.

2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      In order for a robot to know what happens around it the robot needs sensors.
      Humans and animals also need this, but they are called senses. A robot
      might have different sensors, and therefore also measure other things.

      You can see the actual values of the sensors in the 'Sensors' tab.

   .. grid-item::

      .. image:: _media/sensors_tab.png
         :width: 350
         :alt: Sensoren

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Assignment:** In this workshop we will take look at the infrared intensity 
      sensor. If you take a good look at the sensor you will see two rounds with a 
      piece in between them. One of them is sending out infrared (IR) light, while
      the other one is the actual sensor. That one is measuring the amount of
      infrared light. You can put your robot on the table and check what values
      the sensor returns. You can also move your finger in front of the sensor
      to see the difference.

   .. grid-item::

      +-------------------+-------+
      | Where:            |       |
      +===================+=======+
      | on table:         | . . . |
      +-------------------+-------+
      | on floor:         | . . . |
      +-------------------+-------+
      | finger on sensor: | . . . |
      +-------------------+-------+
      | on.......:        | . . . |
      +-------------------+-------+

.. admonition:: BE CAREFUL
   :class: warning

   Even thouh your robot might be stationary on the table it will still measure
   a slightly different value everytime. This is because the sensor is quite
   sensitive, but also because it might make some small errors while measuring.
   These errors are called the 'noise' in your signal.

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      **Assignment:** Try to find the biggest (maximum) en smallest (minimum)
      values of this sensor:

   .. grid-item::

      +-------------------+-------+
      | minimum value:    | . . . |
      +-------------------+-------+
      | maximum value:    | . . . |
      +-------------------+-------+


4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      This sensor has a minimum value of 0 and a maximum value of 4095. As explained
      in the first assignment this is a measure of how many infrared light got bounced
      back.

      When the value is low, it saw a lot. The surface it is measuring will probably be
      light.

      When the value is high, not much of the light got back. The surface it is measuring
      will probably be dark.

      But, the sensor will also return a high value if it is just not looking at an 
      infrared source at all.

   .. grid-item::

      .. image:: _media/line_sensor_theory.png
         :width: 350
         :alt: Line volg sensor

.. admonition:: BE CAREFUL
   :class: warning

   Is is possible that the sensor is not looking at anything at all. 

   The value can also be low if there is another infrared source shining on the sensor.
   For example a lamp or the sun.
 
   The value can also be high when no light is reflected. This can happen when your sensor
   is too far away from the surface.

.. admonition:: INFO
   :class: note

   The maximum value of the sensor is actually not depending on the sensor, but on the
   microcontroller. The microcontroller is translating the value of the sensor (in Volts)
   to a value with a maximum value.


5
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      Reading out the sensor value can of course also be done in the 'programming' tab.

      With a combination of blocks from 'sensors' and 'actuators' you can create
      some code and press 'play'.

      You will now see the value being printed on the screen. Like with the motors, this
      will only do it once.

   .. grid-item::

      .. tab-set::

         .. tab-item:: Blokken
            :sync: blokken

            .. image:: _media/line_sensor_blockly.png
               :width: 350
               :alt: Line volg sensor Blockly

         .. tab-item:: Python
            :sync: python

            .. image:: _media/line_sensor_python.png
               :width: 350
               :alt: Line volg sensor Python







