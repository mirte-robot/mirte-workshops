:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.6 Using other PCL functions
##################################

You have now succesfully created a template package to
use PCL in a ROS2 setup. Although filtering is nice,
you will probably want to use other functions of PCL.

A common pipeline contains filtering, segmentation, 
clustering and/or feature extraction.

For now, you can start by playing around with:

- `Passthrough filters <https://pcl.readthedocs.io/projects/tutorials/en/master/passthrough.html>`_
- `Plane segmentation <https://pcl.readthedocs.io/projects/tutorials/en/master/planar_segmentation.html#planar-segmentation>`_
- `Cluster extraction <https://pcl.readthedocs.io/projects/tutorials/en/master/cluster_extraction.html>`_

.. admonition:: info

   You might still experience a lot of CPU usage, and/or
   low update rates. Solutions to these include changing
   the update rate of the camera itself. But also offloading
   the PCL compute to another machine might help.