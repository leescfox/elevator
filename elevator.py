class Elevator:
    def __init__(self, capacity=8):
        self.current_floor = 1
        self.is_moving = False
        self.direction = 0
        self.passengers = []
        self.capacity = capacity
        self.buttons_pressed = []

    def call(self, floor, direction, passengers):
        print('Вызов лифта на этаже {} направление {} количество пассажиров {}'.format(floor, 'вверх' if direction > 0 else 'вниз', passengers))
        self.buttons_pressed.append(floor)
        self.buttons_pressed = list(set(self.buttons_pressed))  # удаление повторных вызовов
        self.direction = direction

    def press_button(self, floor):
        print('Нажата кнопка этажа {}'.format(floor))
        self.buttons_pressed.append(floor)
        self.buttons_pressed = list(set(self.buttons_pressed))  # удаление повторных нажатий

    def enter(self, passengers):
        print('Зашли в лифт {} пассажиров'.format(passengers))
        if len(self.passengers) + passengers <= self.capacity:
            self.passengers.extend([1] * passengers)

    def exit(self, passengers):
        print('Вышли из лифта {} пассажиров'.format(passengers))
        self.passengers = self.passengers[:-passengers]

    def move(self):
        if not self.buttons_pressed:
            # если нет вызовов, приостанавливаемся
            self.is_moving = False
            print('Лифт остановился')
            return
        next_floor = min(self.buttons_pressed, key=lambda f: abs(f - self.current_floor))
        if next_floor > self.current_floor:
            self.current_floor += 1
            self.direction = 1
        elif next_floor < self.current_floor:
            self.current_floor -= 1
            self.direction = -1
        else:
            # если приехали на этаж, выходим пассажирам и удаляем этот вызов
            self.exit(len([p for p in self.passengers if p == self.current_floor]))
            self.buttons_pressed.remove(self.current_floor)

        print('Лифт на {} этаже направление {}'.format(self.current_floor, 'вверх' if self.direction > 0 else 'вниз'))
        self.is_moving = True