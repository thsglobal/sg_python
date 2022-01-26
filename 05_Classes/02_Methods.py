class Car:
    def __init__(self, max_speed: int, current_speed: int = 0) -> None:
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self, speed_increase: int) -> None:
        if speed_increase > 0:
            self.current_speed = min(self.current_speed + speed_increase, self.max_speed)

    def brake(self, speed_decrease: int) -> None:
        if speed_decrease > 0:
            self.current_speed = max(self.current_speed - speed_decrease, 0)