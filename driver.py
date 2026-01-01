import random
    
class Driver:
    def __init__(self, name, _skill = random.randint(0, 100)):
        self.name = name
        self._skill = _skill if 0 <= _skill <= 100 else random.randint(0, 100)

    def driver_coef(self):
        return 0.8 + 0.004 * self.skill
    
    def skill_range_check(func):
        def wrapper(self, value):
            if not 0 <= value <= 100:
                raise ValueError("Error! The skill level must be between 0-100!")
            func(self, value)
        return wrapper
    
    def __str__(self):
        return f"Name : {self.name} | Skill : {self.skill} -> {self.driver_level} level"
    
    @property
    def skill(self):
        return self._skill

    @skill.setter
    @skill_range_check
    def skill(self, new_skill):
        self._skill = new_skill
    
    @property
    def driver_level(self):
        if self._skill > 100 or self._skill < 0:
            return "Please enter a skill level between 0-100!"
        elif self._skill < 40:
            return "Low"
        elif self._skill < 70:
            return "Mid"
        elif self._skill <= 100:
            return "High"