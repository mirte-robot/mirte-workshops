:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.3 Converting to PCL datatypes
#################################

In the previous section we were able to listen to ROS2 topics of the
PointCloud2 datatypes. This data is still in the PointCloud2 message
format. To use PCL we need to convert this into a PCL datatype.

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 7-10

   #include <memory>

   // ROS2 includes
   #include "rclcpp/rclcpp.hpp"
   #include "sensor_msgs/msg/point_cloud2.hpp"

   // PCL includes
   #include <pcl/point_cloud.h>
   #include <pcl/point_types.h>
   #include <pcl_conversions/pcl_conversions.h>


.. code-block:: cpp
  :linenos:
  :emphasize-lines: 5-15

   void cloudCallback(
      const sensor_msgs::msg::PointCloud2::SharedPtr msg)
   {
 
     auto cloud = std::make_shared<pcl::PointCloud<pcl::PointXYZ>>();

     std::make_shared<pcl::PointCloud<pcl::PointXYZ>>();
 
     pcl::fromROSMsg(*msg, *cloud);
 
     RCLCPP_INFO(
       get_logger(),
       "Received cloud with %zu points",
       cloud->size()
     );

   }

With these changes, the package should again be able to build an run:

.. code-block:: console

   $ colcon build --packages-select pcl_workshop
   $ ros2 run pcl_workshop my_pcl_filter

.. admonition:: info

   Make sure that you compile from your workspace folder.


