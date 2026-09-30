:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.4 Downsampling PCL
####################

Now that we have access to the PCL types, we can actually start
using the `PCL library <https://pcl.readthedocs.io/projects/tutorials/en/master/index.html>`_. 
The first thing we want to do is downsampling using `voxelgrids <https://pcl.readthedocs.io/projects/tutorials/en/master/voxel_grid.html#voxelgrid>`_.

To get this to work, we need to include a new PCL header:

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 5

   // PCL includes
   #include <pcl/point_cloud.h>
   #include <pcl/point_types.h>
   #include <pcl_conversions/pcl_conversions.h>
   #include <pcl/filters/voxel_grid.h>

And again change the callback function:

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 11-25

   void cloudCallback(
      const sensor_msgs::msg::PointCloud2::SharedPtr msg)
   {

     auto cloud = std::make_shared<pcl::PointCloud<pcl::PointXYZ>>();

     std::make_shared<pcl::PointCloud<pcl::PointXYZ>>();
 
     pcl::fromROSMsg(*msg, *cloud);

     auto downsampled_cloud = std::make_shared<pcl::PointCloud<pcl::PointXYZ>>();

     pcl::VoxelGrid<pcl::PointXYZ> voxel_filter;

     voxel_filter.setInputCloud(cloud);

     // 3 cm voxels
     voxel_filter.setLeafSize(0.03f, 0.03f, 0.03f);

     voxel_filter.filter(*downsampled_cloud);
     RCLCPP_INFO(
       get_logger(),
       "Original: %zu points, Downsampled: %zu points",
       cloud->size(),
       downsampled_cloud->size());
   }

With these changes, you should now be able to run this node:

.. code-block:: console

   $ colcon build --packages-select pcl_workshop
   $ ros2 run pcl_workshop my_pcl_filter


