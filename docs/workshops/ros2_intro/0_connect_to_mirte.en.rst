:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.1 Connecting to the MIRTE robot
#########################################

From now on we will start working on the MIRTE robot. We first need
to connect to the wifi connection of the robot. Please follow the 
instructions for the `Wireless Acces Point <https://docs.mirte.org/develop/doc/mirte_os/connect_to_mirte.html#wireless-acces-point>`_
to connect to your own MIRTE. The Unique ID is mentioned on
the sticker on the robot.

.. tab-set::

   .. tab-item:: VSCode on computer

      As soon as we are connected to the robot, we can also connect VS code to the
      MIRTE robot. If it is the first time you try to do this, you need to make
      sure that you have changed the password of the mirte user on the robot.

      This can be done by opening a terminal (or command prompt in Windows) and 
      ssh into your robot:

      .. code-block:: console

         $ ssh mirte@192.168.42.1

      It will ask you for a password (note: it will not show that you typed), And
      ask for a new password twice. Please note that whis will also be your new 
      wifi password.
      
      Now that we have set this we can connect VScode to the MIRTE:

      - In VS code press F1
      - Type Remote-SSH > Connect to Host...
      - Type: mirte@192.168.42.1

   .. tab-item:: VSCode on MIRTE

      You can also just use the VSCode already on the MIRTE robot. This is convenient
      for small test-setups, but might be a bit slow for actual development. You
      can access VSCode by opening teh following link in a browser:

      http://mirte.local/code/?folder=/home/mirte/

In order to type command, you need to open a terminal in VS code
(View > Terminal).

.. admonition:: info

   In this training we will use mirte$ for commands that will run on
   the MIRTE robot.





