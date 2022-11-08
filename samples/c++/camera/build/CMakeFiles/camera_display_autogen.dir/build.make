# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build

# Utility rule file for camera_display_autogen.

# Include any custom commands dependencies for this target.
include CMakeFiles/camera_display_autogen.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/camera_display_autogen.dir/progress.make

CMakeFiles/camera_display_autogen: protobuf/SensorNearData/BaseImage.pb.cc
CMakeFiles/camera_display_autogen: protobuf/SensorNearData/BaseImage.pb.h
CMakeFiles/camera_display_autogen: protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.cc
CMakeFiles/camera_display_autogen: protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.h
CMakeFiles/camera_display_autogen: protobuf/header.pb.cc
CMakeFiles/camera_display_autogen: protobuf/header.pb.h
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Automatic MOC for target camera_display"
	/usr/bin/cmake -E cmake_autogen /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles/camera_display_autogen.dir/AutogenInfo.json ""

protobuf/SensorNearData/BaseImage.pb.cc: /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/BaseImage.proto
protobuf/SensorNearData/BaseImage.pb.cc: /usr/bin/protoc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Running C++ protocol buffer compiler on /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/BaseImage.proto"
	/usr/bin/protoc --proto_path=/home/ubuntu/hackchallenge-hack-the-truck/datatypes --cpp_out=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/protobuf /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/BaseImage.proto

protobuf/SensorNearData/BaseImage.pb.h: protobuf/SensorNearData/BaseImage.pb.cc
	@$(CMAKE_COMMAND) -E touch_nocreate protobuf/SensorNearData/BaseImage.pb.h

protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.cc: /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/SurroundViewImage/SurroundViewImage.proto
protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.cc: /usr/bin/protoc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Running C++ protocol buffer compiler on /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/SurroundViewImage/SurroundViewImage.proto"
	/usr/bin/protoc --proto_path=/home/ubuntu/hackchallenge-hack-the-truck/datatypes --cpp_out=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/protobuf /home/ubuntu/hackchallenge-hack-the-truck/datatypes/SensorNearData/SurroundViewImage/SurroundViewImage.proto

protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.h: protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.cc
	@$(CMAKE_COMMAND) -E touch_nocreate protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.h

protobuf/header.pb.cc: /home/ubuntu/hackchallenge-hack-the-truck/datatypes/header.proto
protobuf/header.pb.cc: /usr/bin/protoc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Running C++ protocol buffer compiler on /home/ubuntu/hackchallenge-hack-the-truck/datatypes/header.proto"
	/usr/bin/protoc --proto_path=/home/ubuntu/hackchallenge-hack-the-truck/datatypes --cpp_out=/home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/protobuf /home/ubuntu/hackchallenge-hack-the-truck/datatypes/header.proto

protobuf/header.pb.h: protobuf/header.pb.cc
	@$(CMAKE_COMMAND) -E touch_nocreate protobuf/header.pb.h

camera_display_autogen: CMakeFiles/camera_display_autogen
camera_display_autogen: protobuf/SensorNearData/BaseImage.pb.cc
camera_display_autogen: protobuf/SensorNearData/BaseImage.pb.h
camera_display_autogen: protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.cc
camera_display_autogen: protobuf/SensorNearData/SurroundViewImage/SurroundViewImage.pb.h
camera_display_autogen: protobuf/header.pb.cc
camera_display_autogen: protobuf/header.pb.h
camera_display_autogen: CMakeFiles/camera_display_autogen.dir/build.make
.PHONY : camera_display_autogen

# Rule to build all files generated by this target.
CMakeFiles/camera_display_autogen.dir/build: camera_display_autogen
.PHONY : CMakeFiles/camera_display_autogen.dir/build

CMakeFiles/camera_display_autogen.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/camera_display_autogen.dir/cmake_clean.cmake
.PHONY : CMakeFiles/camera_display_autogen.dir/clean

CMakeFiles/camera_display_autogen.dir/depend:
	cd /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build /home/ubuntu/hackchallenge-hack-the-truck/samples/c++/camera/build/CMakeFiles/camera_display_autogen.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/camera_display_autogen.dir/depend

