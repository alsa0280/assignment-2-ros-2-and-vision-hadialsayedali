# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target aisd_msgs::aisd_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${aisd_msgs_TARGETS}.
if(aisd_msgs_TARGETS AND NOT TARGET aisd_msgs::aisd_msgs)
  add_library(aisd_msgs::aisd_msgs INTERFACE IMPORTED)
  set_target_properties(aisd_msgs::aisd_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${aisd_msgs_TARGETS}")
endif()
