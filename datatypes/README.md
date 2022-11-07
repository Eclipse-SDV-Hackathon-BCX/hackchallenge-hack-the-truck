# Protobuf datatypes for Conti's BCX Truck

---

### Lightbar control
|   |  |
| --- | --- |
| File     | [Applications/Truck/W3Lightbar.proto](/Applications/Truck/W3Lightbar.proto) |
| Message | **pb.Applications.Truck.W3LightbarRequest** |
| Direction | To vehicle |
| Topic  | W3LightbarRequestPb |

---

### HMI Keyboard state
|   |  |
| --- | --- |
| File     | [HMI/HMICanKeyboard.proto](/HMI/HMICanKeyboard.proto) |
| Message | **pb.HMI.HmiCanKeyboardState** |
| Direction | From vehicle |
| Topic  | HmiCanKeyboardStatePb |

---

### HMI Button state
|   |  |
| --- | --- |
| File     | [HMI/CanButton.proto](/HMI/CanButton.proto) |
| Message | **pb.HMI.ButtonState** |
| Direction | From vehicle |
| Topic  | HMI_CAN_Button_State |

---

### Steering wheel angle
|   |  |
| --- | --- |
| File     | [SensorNearData/VehicleDynamics.proto](/SensorNearData/VehicleDynamics.proto) |
| Message | **pb.SensorNearData.VehicleDynamics** |
| Direction | From vehicle |
| Topic  | VehicleDynamicsInPb |

---

### Brake pedal state
|   |  |
| --- | --- |
| File     | [SensorNearData/Brake.proto](/SensorNearData/Brake.proto) |
| Message | **pb.SensorNearData.Brake** |
| Direction | From vehicle |
| Topic  | BrakeInPb |

---

### Camera image
|   |  |
| --- | --- |
| File     | [SensorNearData/SurroundViewImage/SurroundViewImage.proto](/SensorNearData/SurroundViewImage/SurroundViewImage.proto) |
| Message | **pb.SensorNearData.SurroundViewImage.SurroundViewImage** |
| Direction | From vehicle |
| Topic  | CameraImage(Front\|Left\|Right\|Rear)RgbPb |

### Lidar point cloud
|   |  |
| --- | --- |
| File     | [ros/sensor_msgs/PointCloud2.proto](/ros/sensor_msgs/PointCloud2.proto) |
| Message | **pb.sensor_msgs/PointCloud2** |
| Direction | From vehicle |
| Topic  | ROSLidarRoof(Left\|Right) |
