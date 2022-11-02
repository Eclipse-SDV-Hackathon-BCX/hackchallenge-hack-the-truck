#include <QApplication>
#include <QMainWindow>

#include <ecal/ecal.h>

#include <all_subscribers.h>
#include <image_widget.h>

int main(int argc, char* argv[])
{
  eCAL::Initialize();
  QApplication app(argc, argv);
  QGuiApplication::setApplicationDisplayName("Camera Viewer");

  ImageWidget widget;
  widget.resize(1920/2, 1280/2);

  AllSubscribers subscribers;

  // connect the data
  qRegisterMetaType<pb::SensorNearData::SurroundViewImage::SurroundViewImage>("pb::SensorNearData::SurroundViewImage::SurroundViewImage");
  QObject::connect(&subscribers, &AllSubscribers::ImageReceived,
    &widget, &ImageWidget::setImage, Qt::QueuedConnection);

  widget.show();

  return app.exec();
}