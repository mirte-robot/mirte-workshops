:orphan:
:hide-toc:
:html_theme.sidebar_secondary.remove:

.. WARNING_SPOT

1.2 Listener to PointCloud2 topic
#################################

Now that we have seen some PointCloud2 data, it is time to downsample
this on the ROS2 side. For this we will first need to create a node
that will listen to the pointcloud topic.

So the first thing to do is creating a new ROS2 package:

.. code-block:: console

   $ mkdir -p ~/training_ws/src/pcl_workshop
   $ cd ~/training_ws/src/pcl_workshop
   $ ros2 pkg create pcl_workshop --build-type ament_cmake --dependencies rclcpp sensor_msgs pcl_conversions pcl_ros

.. admonition:: info

   Since the PCL itself only has a C++ interface, we will have to 
   create a C++ ROS package.

And lets make sure that is builds (there is nothing really to compile
yet):

.. code-block:: console

   $ colcon build --packages-select pcl_workshop

Now that we have the new ROSpackage ready, we can create a new node. 
You can create a new file called pcl_node.cpp in the src directory of
this new package. And add the following code to it:

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 4, 5, 11, 14-15, 18-19, 22, 31

   #include <memory>

   // ROS2 includes
   #include "rclcpp/rclcpp.hpp"
   #include "sensor_msgs/msg/point_cloud2.hpp"

   class PCLDetector : public rclcpp::Node
   {
   public:
   PCLDetector()
   : Node("pcl_filter")
   {
   
      auto qos = rclcpp::QoS(rclcpp::KeepLast(10));
      qos.best_effort();

      subscription_ =
         this->create_subscription<sensor_msgs::msg::PointCloud2>(
         "/camera/depth/points",
         qos,
         std::bind(
            &PCLDetector::cloudCallback,
            this,
            std::placeholders::_1));

      RCLCPP_INFO(get_logger(), "PCL filter started");
   }

   private:
   void cloudCallback(
      const sensor_msgs::msg::PointCloud2::SharedPtr msg)
   {
      RCLCPP_INFO(
         get_logger(),
         "Received cloud: width=%u height=%u points=%u",
         msg->width,
         msg->height,
         msg->width * msg->height);
   }

   rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr subscription_;
   };

   int main(int argc, char * argv[])
   {
     rclcpp::init(argc, argv);

     auto node = std::make_shared<PCLDetector>();

     rclcpp::spin(node);

     rclcpp::shutdown();
     return 0;
   }

.. admonition:: info

   Note the following parts of this code:

   .. code-block:: console

      4-5: Include the C++ ROS API, and the PointCloud2 message type
      11: The name of the node
      14-15: Setting the right QoS profile for this topic
      18: The (message)type of the data to lister to (ie. sensor_msgs::msg::PointCloud2)
      19: The name of the (topic)data to listen to (ie. /camera/depth/points)
      22: The callback function to call when data arrives on this topic
      31: The data itself as variable (with name msg)

But we also need to tell colcon/CMake that this file is added, and which libraries it 
need to link with. So in the pcl_workshop/CMakeLists.txt file, add the following:

.. code-block:: cpp
  :linenos:
  :emphasize-lines: 7-30

  # find dependencies
  find_package(ament_cmake REQUIRED)
  find_package(rclcpp REQUIRED)
  find_package(sensor_msgs REQUIRED)
  find_package(pcl_conversions REQUIRED)
  find_package(pcl_ros REQUIRED)
  find_package(PCL REQUIRED)

  include_directories( ${PCL_INCLUDE_DIRS} include)
  link_directories(${PCL_LIBRARY_DIRS})
  add_definitions(${PCL_DEFINITIONS})

  add_executable(my_pcl_filter src/pcl_node.cpp)

  ament_target_dependencies(
    my_pcl_filter
    rclcpp
    sensor_msgs
    pcl_conversions
  )

  target_link_libraries(
    my_pcl_filter
    ${PCL_LIBRARIES}
  )

  install(
    TARGETS my_pcl_filter
    DESTINATION lib/${PROJECT_NAME}
  )

  ament_package()


.. admonition:: info

   Note that, in line 13, we now renamed the node to 'my_pcl_filter'. So this
   overrules the name that we have set in line 11 of pcl_node.cpp.

Now that we have setup everything. We can see if we indeed can build
and run this node:

.. code-block:: console

   $ cd ~/training_ws
   $ colcon build --packages-select pcl_workshop
   $ source install/setup.bash
   $ ros2 run pcl_workshop my_pcl_filter
