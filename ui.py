import PySide6
import PySide6.QtCore
import PySide6.QtWidgets
from timezone import Timezone

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timezone = Timezone()

        self.setWindowTitle("Timezones")

        layout = PySide6.QtWidgets.QVBoxLayout()
        
        current_time = self.timezone.get_current_time()
        self.time_lable = PySide6.QtWidgets.QLabel(current_time)
        current_timezone = self.timezone.get_current_timezone()
        self.timezone_lable = PySide6.QtWidgets.QLabel(str(current_timezone))
        
        layout.addWidget(self.time_lable)
        layout.addWidget(self.timezone_lable)

        result_time = self.timezone.get_result_time()
        self.result_time_lable = PySide6.QtWidgets.QLabel(str(result_time))
        result_timezone = self.timezone.get_result_timezone()
        self.result_timezone_lable = PySide6.QtWidgets.QLabel(str(result_timezone))

        layout.addWidget(self.result_time_lable)
        layout.addWidget(self.result_timezone_lable)

        widegt = PySide6.QtWidgets.QWidget()
        widegt.setLayout(layout)
        self.setCentralWidget(widegt)

        self.timer = PySide6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.setFixedSize(200,100)

    def update_time(self):
        current_time = self.timezone.get_current_time()
        result_time = self.timezone.get_result_time()
        self.time_lable.setText(str(current_time))
        self.result_time_lable.setText(str(result_time))


if __name__ == '__main__':
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    