import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QCheckBox,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
)


class MacOrder(QWidget):
    def __init__(self):
        super(MacOrder, self).__init__()
        self.setWindowTitle("Заказ в Макдональдсе")
        self.menu_checkboxes = {
            "Чизбургер": 0,
            "Гамбургер": 0,
            "Кока-кола": 0,
            "Наггетсы": 0
        }
        self.menu_checkboxes = [QCheckBox(self), QCheckBox(self), QCheckBox(self), QCheckBox(self)]
        self.main_layout = QVBoxLayout(self)
        self.menu_checkboxes[0].setText("Чизбургер")
        self.main_layout.addWidget(self.menu_checkboxes[0])
        self.menu_checkboxes[1].setText("Гамбургер")
        self.main_layout.addWidget(self.menu_checkboxes[1])
        self.menu_checkboxes[2].setText("Кока-кола")
        self.main_layout.addWidget(self.menu_checkboxes[2])
        self.menu_checkboxes[3].setText("Наггетсы")
        self.main_layout.addWidget(self.menu_checkboxes[3])
        self.order_btn = QPushButton(self)
        self.order_btn.setText("Заказать")
        self.order_btn.clicked.connect(self.order_button_fun)
        self.main_layout.addWidget(self.order_btn)
        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.main_layout.addWidget(self.result)

    def order_button_fun(self):
        orders_str = '\n'.join([x.text() for x in self.menu_checkboxes if x.checkState()])
        self.result.setPlainText(
            f"Ваш заказ:\n\n{orders_str}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MacOrder()
    wnd.show()
    sys.exit(app.exec())
