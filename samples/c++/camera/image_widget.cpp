#include <image_widget.h>

#include <qlabel.h>

ImageWidget::ImageWidget(QWidget* parent)
  : QWidget(parent)
{
}

void ImageWidget::setImage(const pb::SensorNearData::SurroundViewImage::SurroundViewImage& input_image)
{
  const auto& image_ = input_image.data();
  image_data = image_.imagedata();
  image = QImage((const uchar*)image_data.c_str(), image_.width(), image_.height(), QImage::Format_RGB888);

  update();
}

void ImageWidget::paintEvent(QPaintEvent*)
{
  QPainter painter(this);
  painter.drawImage(QRect(0, 0, width(), height()), image);
}