cmake_minimum_required(VERSION 3.15)

project(camera_display)

set(CMAKE_AUTOMOC ON)

find_package(Protobuf REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Widgets)
find_package(eCAL REQUIRED)

add_executable(camera_display)

target_sources(camera_display
  PRIVATE
    all_subscribers.h
    image_widget.cpp
    image_widget.h
    main.cpp
)

target_include_directories(camera_display
  PRIVATE
    .
)

target_link_libraries(camera_display
  PRIVATE
    Qt5::Widgets
    eCAL::core
)

set(protobuf_idl_path ${CMAKE_CURRENT_SOURCE_DIR}/../../../datatypes)
set(proto_files
  ${protobuf_idl_path}/SensorNearData/SurroundViewImage/SurroundViewImage.proto
  ${protobuf_idl_path}/SensorNearData/BaseImage.proto
  ${protobuf_idl_path}/header.proto
)

protobuf_target_cpp(camera_display ${protobuf_idl_path} ${proto_files})
