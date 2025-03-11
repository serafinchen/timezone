import PySide6
import PySide6.QtWidgets
from timezone import Timezone

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        timezone = Timezone()

        self.setWindowTitle("Timezones")

        layout = PySide6.QtWidgets.QVBoxLayout()
        
        current_Time = timezone.get_current_time()
        time_Lable = PySide6.QtWidgets.QLabel(str(current_Time))
        
        layout.addWidget(time_Lable)

        widegt = PySide6.QtWidgets.QWidget()
        widegt.setLayout(layout)
        self.setCentralWidget(widegt)



if __name__ == '__main__':
    app = PySide6.QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    