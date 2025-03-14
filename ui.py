import PySide6
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from timezone import Timezone
import pytz

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.timezone = Timezone()
        self.setWindowTitle("Timezones")
        self.setWindowIcon(PySide6.QtGui.QIcon("world.jpg"))
        self.setStyleSheet("""
            background-color: #999999;
            border-radius: 15px;
        """)
        
        mainLayout = PySide6.QtWidgets.QVBoxLayout()
        current_timeLayout = PySide6.QtWidgets.QHBoxLayout()
        result_timeLayout = PySide6.QtWidgets.QHBoxLayout()

        font = PySide6.QtGui.QFont("Helvetica Neue", 14)
        fontbox = PySide6.QtGui.QFont("Helvetica Neue")

        #DropDown Box
        self.box = PySide6.QtWidgets.QComboBox()
        self.box.addItems(self.timezone.get_custom_timezones())
        self.box.setStyleSheet("""
            background-color: white;
            color: #333;
            border: 2px solid #bbb;
            border-radius: 8px;
            padding: 8px;
        """)
        self.box.setFont(fontbox)

        mainLayout.addWidget(self.box)

        self.box.activated.connect(self.change_result_time)

        #Current Time and Current Timezone Lable
        current_time_widget = PySide6.QtWidgets.QWidget()
        current_time_widget.setLayout(current_timeLayout)
        current_time = self.timezone.get_current_time()
        self.time_lable = PySide6.QtWidgets.QLabel(current_time)
        current_timezone = self.timezone.get_current_timezone()
        self.timezone_lable = PySide6.QtWidgets.QLabel(str(current_timezone))
        self.time_lable.setFont(font)
        self.timezone_lable.setFont(font)
        self.time_lable.setStyleSheet("color: #333;")
        self.timezone_lable.setStyleSheet("color: #666;")
        
        current_timeLayout.addWidget(self.time_lable)
        current_timeLayout.addWidget(self.timezone_lable)
        current_time_widget.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;  
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        """)
        mainLayout.addWidget(current_time_widget)

        #Result Time and Result Timezone Lable
        result_time_widget = PySide6.QtWidgets.QWidget()
        result_time_widget.setLayout(result_timeLayout)
        self.result_time = self.timezone.get_result_time()
        self.result_time_lable = PySide6.QtWidgets.QLabel(str(self.result_time))
        self.result_timezone = self.timezone.get_result_timezone()
        self.result_timezone_lable = PySide6.QtWidgets.QLabel(str(self.result_timezone))
        self.result_time_lable.setFont(font)
        self.result_timezone_lable.setFont(font)
        self.result_time_lable.setStyleSheet("color: #333;")
        self.result_timezone_lable.setStyleSheet("color: #666;")

        result_timeLayout.addWidget(self.result_time_lable)
        result_timeLayout.addWidget(self.result_timezone_lable)  
        result_time_widget.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        """)
        mainLayout.addWidget(result_time_widget)

        widegt = PySide6.QtWidgets.QWidget()
        widegt.setLayout(mainLayout)
        self.setCentralWidget(widegt)
        

        self.timer = PySide6.QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.resize(500,300)

    def update_time(self):
        current_time = self.timezone.get_current_time()
        result_time = self.timezone.get_result_time()
        self.time_lable.setText(str(current_time))
        self.result_time_lable.setText(str(result_time))

    def change_result_time(self):
        self.result_timezone = self.box.currentText()
        self.result_timezone_lable.setText(self.result_timezone)
        self.timezone.change_result_timezone(self.result_timezone)


if __name__ == '__main__':
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    