#pragma once

#include <QObject>

#include <ecal/ecal.h>
#include <ecal/msg/protobuf/subscriber.h>

#include <SensorNearData/SurroundViewImage/SurroundViewImage.pb.h>

class AllSubscribers : public QObject
{
  Q_OBJECT

public:
  AllSubscribers() :
    image_subscriber("SvcImageRearRgbPb")
  {
    image_subscriber.AddReceiveCallback(
      [this](const char* /*topic_*/, const pb::SensorNearData::SurroundViewImage::SurroundViewImage& msg, long long /*time_*/, long long /*clock_*/, long long /*id_*/) {
        emit ImageReceived(msg);
      }
    );
  }

signals:
  void ImageReceived(const pb::SensorNearData::SurroundViewImage::SurroundViewImage& image);

private:
  eCAL::protobuf::CSubscriber<pb::SensorNearData::SurroundViewImage::SurroundViewImage> image_subscriber;
};