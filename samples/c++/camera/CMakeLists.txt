# Copyright (c) 2022 Continental Autonomous Mobility Germany GmbH
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

cmake_minimum_required(VERSION 3.15)

project(camera_display)

set(CMAKE_FIND_PACKAGE_PREFER_CONFIG ON)
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


if(WIN32)
    include(${CMAKE_CURRENT_LIST_DIR}/cmake/qt_windeployqt.cmake)
    # Deploy Qt DLLs in the binary folder. This is necessary for starting the application from whithin the IDE without having to copy QtCore.dll, QtWidgets.dll etc. by hand each time
    qt_add_windeployqt_postbuild(--no-system-d3d-compiler --no-compiler-runtime --no-opengl-sw --pdb "$<TARGET_FILE:${PROJECT_NAME}>")
endif()