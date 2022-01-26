class Car:
    def __init__(self, max_speed: int, current_speed: int = 0) -> None:
        self._max_speed = max_speed  # Single underscore - hidden from IDE
        self.__current_speed = current_speed  # Double underscore - private

    def accelerate(self, speed_increase: int) -> None:
        if speed_increase > 0:
            self.__current_speed = min(self.__current_speed + speed_increase, self._max_speed)

    def brake(self, speed_decrease: int) -> None:
        if speed_decrease > 0:
            self.__current_speed = max(self.__current_speed - speed_decrease, 0)

    def get_speed(self):
        return self.__current_speed

    def print_speed(self):
        print(self.__current_speed)


tesla = Car(100)
for i in range(7):
    tesla.print_speed()
    tesla.accelerate(20)
    tesla.accelerate(-10)

for i in range(7):
    tesla.print_speed()
    tesla.brake(20)
    tesla.brake(-10)