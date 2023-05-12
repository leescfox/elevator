from elevator_app import ElevatorApp
from elevator import Elevator
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    elevator = Elevator()
    ex = ElevatorApp(elevator)
    ex.show()
    sys.exit(app.exec_())