#pragma once

#include <QtWidgets/qwidget.h>
#include <QPainter>
#include <SensorNearData/SurroundViewImage/SurroundViewImage.pb.h>

class ImageWidget : public QWidget
{
  Q_OBJECT

public:
  ImageWidget(QWidget* parent = Q_NULLPTR);
  virtual ~ImageWidget() = default;

public slots:
  void setImage(const pb::SensorNearData::SurroundViewImage::SurroundViewImage& image);

protected:
  void paintEvent(QPaintEvent*) override;
  
private:
  std::string image_data;
  QImage image;
};