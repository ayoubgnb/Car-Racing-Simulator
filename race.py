from cars import F1Car

class Race:
    def __init__(self, name, driver, car=None):
        self.name = name
        self.driver = driver
        self.car = F1Car.factory_car() if car is None else car
    
    def __str__(self):
        return f"Race Name : {self.name} | Race Driver : {self.driver.name} | Race Car : {self.car.brand} {self.car.car_class}"
    
    def log_race(func):
        def wrapper(self):
            print(f"Start of the {self.name} race")
            func(self)
            print(f"End of the {self.name} race")
        return wrapper
    
    @log_race
    def run(self):
        print(f"{self.name} Race :")
        print(f"Driver | {self.driver}")
        print(f"Car | {self.car}")
        print(f"Final score : {self.final_score():.2f}")
    
    def final_score(self):
        return self.car.performance_score * self.driver.driver_coef() * 100