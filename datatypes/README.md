# Protobuf datatypes for Conti's BCX Truck

The truck is interfaces with protobuf datatypes, using the eCAL middlerware.
A lot of sensor and vehicle state data is avaialable for consumption, and the hacker can use the roof mounted LED bar for actuation.

You can subscribe to the messages with the given topic names, and for control publish the lightbar control message.
Read below for a description of the datatypes.

---
## Actuation

### Lightbar control

A lightbar is mounted on the roof of the truck.
The lightbar has different stati, which can be turned on / off.
You will have the possiblity to control the lightbar, by sending a message that contains idications for each status.
See also the [lightbar example](/samples/python/lightbar/w3_lightbar_demo.py).

|   |  |
| --- | --- |
| File     | [Applications/Truck/W3Lightbar.proto](/datatypes/Applications/Truck/W3Lightbar.proto) |
| Message | **pb.Applications.Truck.W3LightbarRequest** |
| Direction | To vehicle |
| Topic  | W3LightbarRequestPb |

---
## Sensorics and vehicle data


### HMI Keyboard state

The cockpit of the truck contains buttons whose state are available as an eCAL datatype.
You can use it to switch ON / OFF some features of your software.

|   |  |
| --- | --- |
| File     | [HMI/HMICanKeyboard.proto](/datatypes/HMI/HMICanKeyboard.proto) |
| Message | **pb.HMI.HmiCanKeyboardState** |
| Direction | From vehicle |
| Topic  | HmiCanKeyboardStatePb |

---

### HMI Button state

|   |  |
| --- | --- |
| File     | [HMI/CanButton.proto](/datatypes/HMI/CanButton.proto) |
| Message | **pb.HMI.ButtonState** |
| Direction | From vehicle |
| Topic  | HMI_CAN_Button_State |

---

### Steering wheel angle

The truck provides a message to read out the current steering wheel angle.

|   |  |
| --- | --- |
| File     | [SensorNearData/VehicleDynamics.proto](/datatypes/SensorNearData/VehicleDynamics.proto) |
| Message | **pb.SensorNearData.VehicleDynamics** |
| Direction | From vehicle |
| Topic  | VehicleDynamicsInPb |

---

### Brake pedal state

We provide a message to access the break pedal status of the vehicle.

|   |  |
| --- | --- |
| File     | [SensorNearData/Brake.proto](/datatypes/SensorNearData/Brake.proto) |
| Message | **pb.SensorNearData.Brake** |
| Direction | From vehicle |
| Topic  | BrakeInPb |

---

### Camera image

Several cameras are mounted on the truck. 
Data coming from the cameras are accessible via eCAL.
The image is not compressed but contains binary data in RGB8 format.
For a reference on how to access the data, refer to the [camera sample](/samples/c%2B%2B/camera/image_widget.cpp#L23)

|   |  |
| --- | --- |
| File     | [SensorNearData/SurroundViewImage/SurroundViewImage.proto](/datatypes/SensorNearData/SurroundViewImage/SurroundViewImage.proto) |
| Message | **pb.SensorNearData.SurroundViewImage.SurroundViewImage** |
| Direction | From vehicle |
| Topic  | CameraImage(Front\|Left\|Right\|Rear)RgbPb |

---

### Lidar point cloud
|   |  |
| --- | --- |
| File     | [ros/sensor_msgs/PointCloud2.proto](/ros/sensor_msgs/PointCloud2.proto) |
| Message | **pb.sensor_msgs.PointCloud2** |
| Direction | From vehicle |
| Topic  | ROSLidarRoof(Left\|Right) |
