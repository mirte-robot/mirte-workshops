:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.4 Creating a package on the MIRTE robot
#########################################

Since we mainly be working in the MIRTE robot, it makes more sense to
move our working environment to the MIRTE robot as well. In order for
this to work, we need to move our ROS workspace folder, and 
setup VS code in a way that we are working on the robot.

From now on we will start working on the MIRTE robot. We first need
to connect to the wifi connection of the robot. Please follow the 
instructions for the `Wireless Acces Point <https://docs.mirte.org/doc/connect_to_mirte.html#wireless-acces-point>`_
to connect to your own MIRTE. The Unique ID is mentioned on
the sticker on the robot.

After doing so we need to login to the robot. By using a Secure
SHell (SSH) we can login to a linux terminal one the robot. Since we 
will be logging in to the robot a lot, it is easier to do this login 
via keys rather then via passwords. To do so, you can follow the
instructions for `Keybased SSH login <https://docs.mirte.org/doc/access_interface.html#keybased-ssh-login>`_.

We can now easily login with SSH to the MIRTE, which will get
you into the terminal of mirte:

.. code-block:: console
   :class: margin

   mirte@Mirte-XXXXXX:~$


.. code-block:: console
 
   $ ssh mirte@192.168.42.1

.. admonition:: info

   In this training we will use mirte$ for commands that will run on
   the MIRTE robot.

Note that we are now 'on the MIRTE robot', so everything we type will
be executed on the robot. Moving our workspace to the robot is easy:

.. code-block:: console

   mirte$ exit
   $ scp -r ~/training_ws/src mirte@192.168.42.1:training_ws

.. admonition:: info

   Note that you should only copy the src folder in the workspace. All 
   other folders are artefacts, and might not be compatible with other
   machines.

We can now test if we can still run the node. To do this, rember that
you have to:

1) :abbr:`Build the code while in the training_ws directory ($ colcon build --symlink-install)`
2) :abbr:`Source the workspace ($ source ~/training_ws/install/setup.bash)`
3) :abbr:`Run your node ($ ros2 run my_package my_first_node)`

As soon as we confirmed that this is all working as intended, we can 
also connect VS code to the MIRTE robot. In VS code, connect to the MIRTE:

- In VS code press F1
- Type Remote-SSH > Connect to Host...
- Type: 192.168.42.1

You can now open the files you want to edit in the MIRTE. These are
probably in the workspace you just copied.

.. admonition:: info

   For convenience, you can also open a terminal in VS code (View > Terminal).





