# C++ camera sample

This sample shows how to read the camera Images sent by the truck and display them in a Window.

To compile this example, you will need an eCAL installation as well as a QT installation.

You can also use it as a reference for interpreting the camera information in C++.

## How to build

1. Install CMake

    - Windows: 

        https://cmake.org/download/

    - Linux: 
        
        ```bash
        sudo apt install cmake
        ```

2. Install eCAL, as described in the [eCAL Documentation](https://eclipse-ecal.github.io/ecal/getting_started/setup.html)

3. Configure your system's UDP Multicast routes as described [here](https://eclipse-ecal.github.io/ecal/getting_started/cloud.html)

4. Install the Qt SDK. This is not required for eCAL, but as this sample uses Qt, you need this as well.

    - Windows: Download from the Qt Website and install the x64 SDK of Qt 5.15

        https://www.qt.io/download

    - Linux: 

        ```bash
        sudo apt install qtbase5-dev
        ```

5. Create a build directory, cmake and build

    - Windows:

        - Execute `CMakeWindows.bat`
        - Open the visual Studio solution and build it

    - Linux:
    
        ```bash
        mkdir _build
        cd _build
        cmake ..
        make
        ```