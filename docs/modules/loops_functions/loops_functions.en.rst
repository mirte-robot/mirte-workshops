:orphan:

Reusing code
################################

.. article-info::
    :author: :fa:`brain` Programming
    :read-time: 15 min


1
---

We have already learnt how the line following sensor works, and that your
robot can respond to it by controlling the motors. You will probably create
a bigger and more complex program quite fast. You will also notice that you
will be using the same blocks over and over again. In this workshop you will
learn how to reuse these.

2
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      In the 'Drive' workshop you have tried to let your robot drive in square.
      Your code will probably have looked someting like this code. 

      You probably noticed that you are doing the same thing over and over again.
      You can easily reuse these blocks by adding a loop around it.

   .. grid-item::

      .. image:: _media/drive_square.png
        :width: 350
        :alt: Drive square

3
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      A loop makes sure your code is executed a certain amount of times. With that
      we can replace the original code, and make it more compact.

      This already looks way more clean. It is also way easier to modify in case you
      and the robot to drive 2 quares. But it is also less prone to errors, since there
      is less code that could go wrong.

   .. grid-item::

      .. image:: _media/drive_square_loop.png
        :width: 350
        :alt: Drive square

4
---

.. grid:: 1 2 2 2
   :gutter: 2

   .. grid-item::

      But we are still using three blocks to just drive straight, and another 3
      to just turn around. These might be things that could be useful in other
      scenarios as well. When you would like to reuse some code, you can create
      a so called 'function' for this. 

      By adding this function block, we can easily make this even more easy to understand.
      Now we can create one function for driving straight, and one for turning around.

   .. grid-item::

      .. image:: _media/drive_square_function.png
        :width: 350
        :alt: Drive square

5
---

You can also extend these functions so it can drive forward, backward, turn clockwise and
anti-clockwise.


