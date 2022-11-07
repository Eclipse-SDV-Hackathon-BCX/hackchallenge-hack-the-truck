/*
Copyright (c) 2022 Continental Autonomous Mobility Germany GmbH
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

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