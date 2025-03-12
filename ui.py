import PySide6
import PySide6.QtCore
import PySide6.QtWidgets
from timezone import Timezone
import pytz

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timezone = Timezone()
        self.setWindowTitle("Timezones")
        mainLayout = PySide6.QtWidgets.QVBoxLayout()
        current_timeLayout = PySide6.QtWidgets.QHBoxLayout()
        result_timeLayout = PySide6.QtWidgets.QHBoxLayout()

        #DropDown Box
        self.box = PySide6.QtWidgets.QComboBox()
        for timezone in pytz.all_timezones:
            self.box.addItem(timezone)

        mainLayout.addWidget(self.box)

        #Current Time and Current Timezone Lable
        current_time_widget = PySide6.QtWidgets.QWidget()
        current_time_widget.setLayout(current_timeLayout)
        current_time = self.timezone.get_current_time()
        self.time_lable = PySide6.QtWidgets.QLabel(current_time)
        current_timezone = self.timezone.get_current_timezone()
        self.timezone_lable = PySide6.QtWidgets.QLabel(str(current_timezone))
        
        current_timeLayout.addWidget(self.time_lable)
        current_timeLayout.addWidget(self.timezone_lable)
        mainLayout.addWidget(current_time_widget)

        #Result Time and Result Timezone Lable
        result_time_widget = PySide6.QtWidgets.QWidget()
        result_time_widget.setLayout(result_timeLayout)
        result_time = self.timezone.get_result_time()
        self.result_time_lable = PySide6.QtWidgets.QLabel(str(result_time))
        result_timezone = self.timezone.get_result_timezone()
        self.result_timezone_lable = PySide6.QtWidgets.QLabel(str(result_timezone))

        result_timeLayout.addWidget(self.result_time_lable)
        result_timeLayout.addWidget(self.result_timezone_lable)  
        mainLayout.addWidget(result_time_widget)

        widegt = PySide6.QtWidgets.QWidget()
        widegt.setLayout(mainLayout)
        self.setCentralWidget(widegt)

        self.timer = PySide6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.setBaseSize(500,500)

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
    