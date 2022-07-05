from PyQt6.QtWidgets import *
from media_viewing_widgets.slide_view import SlideView
from graphics_view import GraphicsView


if __name__ == '__main__':
    # may need High DPI scaling
    app = QApplication(['test'])

    slide_view = SlideView()

    scene = QGraphicsScene()
    scene.addItem(slide_view)

    viewer = GraphicsView(scene)
    viewer.resize(1000, 600)
    viewer.show()
    slide_view.load_new_image(QFileDialog().getOpenFileName()[0])
    viewer.fitInView()

    app.exec()
