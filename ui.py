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
        
        current_Time = self.timezone.get_current_time()
        self.time_Lable = PySide6.QtWidgets.QLabel(str(current_Time))
        
        layout.addWidget(self.time_Lable)

        widegt = PySide6.QtWidgets.QWidget()
        widegt.setLayout(layout)
        self.setCentralWidget(widegt)

        self.timer = PySide6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)


    def update_time(self):
        current_time = self.timezone.get_current_time()
        self.time_Lable.setText(str(current_time))


if __name__ == '__main__':
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    