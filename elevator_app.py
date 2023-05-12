from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (QWidget, QSpinBox, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QPushButton,
                             QApplication)


class ElevatorApp(QWidget):
    def __init__(self, elevator):
        super().__init__()

        self.elevator = elevator

        self.create_layout()

    def create_layout(self):
        # создание виджетов
        floor_label = QLabel()
        capacity_label = QLabel()
        passengers_label = QLabel()
        direction_label = QLabel()

        self.floor_label = floor_label
        self.capacity_label = capacity_label
        self.passengers_label = passengers_label
        self.direction_label = direction_label

        call_label = QLabel('Вызов лифта')
        call_floor_spinbox = QSpinBox()
        call_direction_radio_up = QRadioButton('вверх')
        call_direction_radio_down = QRadioButton('вниз')
        call_passengers_spinbox = QSpinBox()
        call_button = QPushButton('Вызвать')
        self.call_floor_spinbox = call_floor_spinbox
        self.call_direction_radio_up = call_direction_radio_up
        self.call_direction_radio_down = call_direction_radio_down
        self.call_passengers_spinbox = call_passengers_spinbox

        floor_buttons_layout = QHBoxLayout()
        for i in range(1, 6):
            button = QPushButton(str(i))
            button.clicked.connect(lambda checked, f=i: self.press_floor_button(f))
            floor_buttons_layout.addWidget(button)

        enter_label = QLabel('Зайти в лифт')
        enter_passenger_spinbox = QSpinBox()
        enter_button = QPushButton('Зайти')
        self.enter_passenger_spinbox = enter_passenger_spinbox

        exit_label = QLabel('Выйти из лифта')
        exit_passenger_spinbox = QSpinBox()
        exit_button = QPushButton('Выйти')
        self.exit_passenger_spinbox = exit_passenger_spinbox

        move_button = QPushButton('Двигаться')
        move_button.clicked.connect(self.move_elevator)
        enter_button.clicked.connect(self.enter_elevator)
        exit_button.clicked.connect(self.exit_elevator)
        # создание компоновки
        vbox = QVBoxLayout()
        vbox.addWidget(floor_label)
        vbox.addWidget(capacity_label)
        vbox.addWidget(passengers_label)
        vbox.addWidget(direction_label)
        vbox.addWidget(call_label)
        vbox.addWidget(call_floor_spinbox)
        hbox = QHBoxLayout()
        hbox.addWidget(call_direction_radio_up)
        hbox.addWidget(call_direction_radio_down)
        vbox.addLayout(hbox)
        vbox.addWidget(call_passengers_spinbox)
        vbox.addWidget(call_button)
        vbox.addLayout(floor_buttons_layout)
        vbox.addWidget(enter_label)
        vbox.addWidget(enter_passenger_spinbox)
        vbox.addWidget(enter_button)
        vbox.addWidget(exit_label)
        vbox.addWidget(exit_passenger_spinbox)
        vbox.addWidget(exit_button)
        vbox.addWidget(move_button)

        # установка компоновки и параметров окна
        self.setLayout(vbox)
        self.setGeometry(100, 100, 300, 500)
        self.setWindowTitle('Лифт')

        # создание таймера для обновления информации о лифте
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_elevator_info)
        self.timer.start(100)

    def call_elevator(self):
        # получение параметров вызова
        floor = self.call_floor_spinbox.value()
        direction = 1 if self.call_direction_radio_up.isChecked() else -1
        passengers = self.call_passengers_spinbox.value()

        # вызов лифта
        self.elevator.call(floor, direction, passengers)

    def press_floor_button(self, floor):
        # нажатие кнопки этажа
        self.elevator.press_button(floor)

    def enter_elevator(self):
        # зайти в лифт
        passengers = self.enter_passenger_spinbox.value()
        self.elevator.enter(passengers)

    def exit_elevator(self):
        # выйти из лифта
        passengers = self.exit_passenger_spinbox.value()
        self.elevator.exit(passengers)

    def move_elevator(self):
        # движение лифта
        self.elevator.move()

    def update_elevator_info(self):
        # обновление информации о лифте
        floor = self.elevator.current_floor
        capacity = self.elevator.capacity
        passengers = len(self.elevator.passengers)
        direction = self.elevator.direction if self.elevator.is_moving else 'стоит на месте'

        self.floor_label.setText('Этаж: {}'.format(floor))
        self.capacity_label.setText('Вместимость: {}'.format(capacity))
        self.passengers_label.setText('Количество пассажиров: {}'.format(passengers))
        self.direction_label.setText('Направление: {}'.format(direction))