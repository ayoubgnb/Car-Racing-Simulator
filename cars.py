class Vehicle:
    car_num = 0

    @classmethod
    def car_counter(cls):
        cls.car_num += 1

    def __init__(self, brand, power, weight):
        self.brand = brand
        self.power = power
        self.weight = weight
        Vehicle.car_counter()

    def __str__(self):
        return f"Class : {self.car_class} | Brand : {self.brand} | Power : {self.power} | Weight : {self.weight}"      
    
    def __eq__(self, other):
        if type(self) is type(other) and self.brand == other.brand and self.power == other.power and self.weight == other.weight:
            return True
        elif isinstance(other, Vehicle) is False:
            return NotImplemented
        else:
            return False
    
    def __gt__(self, other):
        if isinstance(other, Vehicle) is False:
            return NotImplemented
        elif self.performance_score > other.performance_score:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Vehicle) is False:
            return NotImplemented
        elif self.performance_score < other.performance_score:
            return True
        else:
            return False
        
    def validate_performance_score(func):
        def wrapper(self, *args, **kwargs):
            if self.performance_score_formula(self.power, self.weight) <= 0:
                raise ValueError("Error! The performance score of the vehicle must be higher than 0!")
            return func(self, *args, **kwargs)
        return wrapper

    @property
    @validate_performance_score
    def performance_score(self):
        return self.performance_score_formula(self.power, self.weight)
    
    @staticmethod
    def performance_score_formula(power, weight):
        return power / weight

class F1Car(Vehicle):
    @classmethod
    def factory_car(cls):
        return cls("FIA Model", 1000, 800)

    def __init__(self, brand, power, weight, downforce=1.0):
        super().__init__(brand, power, weight)
        self.downforce = downforce
        self.car_class = "F1"

    @property
    def performance_score(self):
        return super().performance_score * self.downforce
    
    def __str__(self):
        return f"{super().__str__()} | Downforce : {self.downforce} | Performance Score : {self.performance_score:.2f}"
    
class GTCar(Vehicle):
    def __init__(self, brand, power, weight, has_tc):
        super().__init__(brand, power, weight)
        self.has_tc = has_tc
        self.car_class = "GT"
    
    def __str__(self):
        return f"{super().__str__()} | Traction Control : {'On' if self.has_tc is True else 'Off'} | Performance Score : {self.performance_score:.2f}"

    @property
    def performance_score(self):
        if self.has_tc is True:
            return super().performance_score * 1.05
        else:
            return super().performance_score

class RallyCar(Vehicle):
    def __init__(self, brand, power, weight, bonus = 0.1):
        super().__init__(brand, power, weight)
        self.bonus = bonus
        self.car_class = "Rally"
    
    def __str__(self):
        return f"{super().__str__()} | Bonus : {self.bonus} | Performance Score : {self.performance_score:.2f}"
    
    @property
    def performance_score(self):
        return super().performance_score + self.bonus