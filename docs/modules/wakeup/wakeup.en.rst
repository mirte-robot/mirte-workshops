:orphan:

Wake up
#########################

.. article-info::
    :author: :fa:`cog` Executing
    :read-time: 15 min


1
----

Now that you have fully built your robot, it is time to wake her up. In this workshop
you will learn how to turn the robot on and off.

.. _hard_reset:

2
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      After completely building the robot, it is time to turn the robot on. You can
      do this by moving the switch on the PCB from 'off' to 'on'.

   .. grid-item::
   
      .. image:: _media/pcb_on.jpg
        :width: 350
        :alt: PCB on


3
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      The small lights on the robot will start to go on. On the computer you will first see
      the red light turning on, followed by the green one. 

      Each robot has their own unique ID. If you do not know the ID of your robot yet, and 
      there will be multiple Mirte robots around: this is the time to decode the ID by 
      counting the blinking of the leds (as shown in the video).

      It always takes some time for the robot to wake up. As soon as the robot started
      the green led on the computer will start to blink. From that point on, you should be
      able to connect to the robot.

   .. grid-item::

      .. video:: /_static/media/mirte_wifi_blinking.mp4
         :width: 500
         :autoplay:
         :loop:

.. dropdown:: :fa:`question-circle` Help

   - I see no light at all:
      - Make sure the cable from the powerbank to the PCB is correctly installed.
      - Make sure the PCB is connected to the computer correctly. 
      - Make sure you moved the switch to the 'on' position.
   - Is do see some light, but not the ones on the computer: 
      - Make sure the SD card is in the computer.
      - Are you sure the right software is installed on the SD card?
   - The green light is on, but does not start to blink:
      - Have you waited for about 2 minutes?
      - Switch the PCB off and back on again.
   - If none of this worked:
      - You will have to 'flash' your SD card again.

4
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      As soon as the red light blinked, your computer woke up and we can start. The first
      thing to do is connecting with the robot. The robot has started its own wifi-network
      with the name: Mirte-XXXXXX (where XXXXXX are the numbers you decoded in the previous
      step).

      On your laptop you can connect to this network by filling in the password 'mirte_mirte',
      and clicking 'Next'.

   .. grid-item::
      
      .. tab-set::

         .. tab-item:: Windows
            :sync: windows

            .. image:: _media/wifi_windows.png
               :width: 350
               :alt: Windows Wifi

         .. tab-item:: Chromebook
            :sync: chromebook

            .. image:: _media/wifi_chromebook.png
               :width: 350
               :alt: Chromebook Wifi

.. admonition:: BE CAREFUL
   :class: warning

   There might be multiple Mirte-XXXXXX networks around. Each robot has their own
   unique one. Make sure to connect to the right one.

.. dropdown:: :fa:`question-circle` Help

   - There is no Mirte-XXXXXX network:
      - Are you sure you saw the lights on the computer blink?
      - Check whether you can find the network on another computer (or mobile phone).

5
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      If Windows asks you this question: it should not really matter what you do. You can click 'Yes' or 'No'.

   .. grid-item::

      .. image:: _media/windows_discovery.png
        :width: 350
        :alt: Windows discovery



6
----

It might take some time for the robot to connect. At some point the connection should say: 'Connected, no internet'.

.. dropdown:: Help

   - I can not connect to the network:
      - Are you sure you used the password 'mirte_mirte' (without ')?
      - If you are sure the lights blinked, and you typed in the right password: unfortunately the only option
        is to reboot the robot by switching the PCB to 'off' and 'on' again. So back to step 2.

7
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      As soon as you have connected you can open a browser (Edge, Firefox, Chrome, etc) and visit:

      http://192.168.42.1

      It might take some time for the page to load. In that case, you can try to 'refresh' the page after
      a minute or so.

   .. grid-item::

      .. image:: _media/new_tab.png
        :width: 350
        :alt: New Tab


8
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      You will now see the starting page of Mirte (no need to worry about the 'no secure connection'). In this
      page you can tell the robot what to do. The following workshops will be done from this page. As soon as
      you see some sensordata on the left, you are ready to go.  

   .. grid-item::

      .. image:: _media/mirte_home.png
        :width: 350
        :alt: Mirte Web Interface

.. admonition:: BE CAREFUL
   :class: warning

   Sometimes you computer might disconnect with the Mirte robot and connect to another network. This might
   happen right away, or while you are working on the robot. Make sure to reconnect with the Mirte robot and
   refesh the page. 

.. dropdown:: Help

   - I do see the startpage, but no sensorvalues:
      - Try to reload by pressing F5.
   - The issue stays:
      - Try to reboot the system as explained in the next step.

.. _shutdown:

9
----

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      You will probably continue with the next workshop, but it is still good to know how to turn the robot
      off. This can be done by clicking the button on the top right of you screen.

   .. grid-item::

      .. image:: _media/shutdown.png
        :width: 70
        :alt: Shutdown

.. admonition:: BE CAREFUL
   :class: warning

   After you have pressed the shutdown button, you still need to turn of the PCB manually. **Only do this
   after the lights on the computer have turned off!** Otherwise there is a chance the robot will not wake
   up anymore (and you have to flash the SD card again).

   .. image:: _media/shutdown_message.png
      :width: 350
      :alt: Shutdown Message




