from cars import F1Car, GTCar, RallyCar
from driver import Driver
from race import Race

def main():
    drivers = []
    cars = []
    races = []
    def display_drivers(): # FUNCTION THAT DISPLAYS ALL THE DRIVERS
        num_display = 0
        for driver in drivers:
            num_display += 1
            print(f"Driver {num_display}. | {driver}")
    def display_cars(): # FUNCTION THAT DISPLAYS ALL THE CARS
        num_display = 0
        for car in cars:
            num_display += 1
            print(f"Car {num_display}. | {car}")
    def display_races(): # FUNCTION THAT DISPLAYS ALL THE RACES
        num_display = 0
        for race in races:
            num_display += 1
            print(f"Race {num_display}. | {race}")
    is_running = True
    while is_running:
        print("Welcome to the Car Racing Simulator !\n\n"
              "1. Create a driver\n"
              "2. Create a car\n"
              "3. Create a race\n"
              "4. Run a race\n"
              "5. Display my creations\n"
              "6. Quit")
        while True: # MENU CHOICE
            try:
                player_choice = int(input("Please make your choice : "))
            except ValueError:
                print("Error ! Please enter a valid menu NUMBER !")
            else:
                break
        print()
        match player_choice:
            case 1: # DRIVER CREATION
                print("Alright ! Let's create a driver !")
                temp_name = input("Choose a name for your driver : ")
                while True: # SKILL LEVEL CHOICE
                    try:
                        temp_skill = int(input(f"Choose a skill level between 0-100 for {temp_name} : "))
                    except ValueError:
                        print("Error ! You have to enter a NUMBER between 0-100 !")
                    else:
                        if 0 <= temp_skill <= 100:
                            break
                        else:
                            print("Error ! You have to enter a skill level between 0-100 !")
                temp_driver = Driver(temp_name, temp_skill)
                drivers.append(temp_driver)
                print(f"{temp_name} has been created succesfully !")
                input("Enter to return to the main menu ")
            case 2: # CAR CREATION
                print("Alright ! Let's create a car !")
                temp_brand = input("Choose a brand for your car : ")
                while True: # CAR POWER CHOICE
                    try:
                        temp_power = int(input(f"Choose the power of your {temp_brand} car in hp : "))
                    except ValueError:
                        print("Error ! The power of your car must be a NUMBER !")
                    else:
                        if temp_power <= 0:
                            print("Error ! The power of your car must be POSITIVE !")
                        else:
                            break
                while True: # CAR WEIGHT CHOICE
                    try:
                        temp_weight = int(input(f"Choose the weight of your {temp_brand} car in kg : "))
                    except ValueError:
                        print("Error ! The weight of your car must be a NUMBER !")
                    else:
                        if temp_weight <= 0:
                            print("Error ! The weight of your car must be POSITIVE !")
                        else:
                            break
                while True: # CAR CLASS CHOICE
                    try:
                        temp_class = int(input("1. F1 Car\n"
                                               "2. GT Car\n" \
                                               "3. Rally Car\n" \
                                              f"What class do you want your {temp_brand} car to be ? : "))
                    except ValueError:
                        print("Error ! Please enter the NUMBER corresponding to the car's class !")
                    else:
                        if 0 < temp_class <= 3:
                            break
                        else:
                            print("Error ! Please enter the number corresponding to the car's class BETWEEN 1-3 !")
                match temp_class: # CAR CREATION BY CLASS
                    case 1: # IF F1 CAR
                        while True:
                            try:
                                temp_downforce = float(input("For an F1 Car, you need to choose a downforce between 1.0-1.4 (higher downforce -> better performance) : "))
                            except ValueError:
                                print("Error ! Please enter a DECIMAL NUMBER between 1.0-1.4")
                            else:
                                if 1 <= temp_downforce <= 1.4:
                                    break
                                else:
                                    print("Error ! Please enter a decimal number BETWEEN 1.0-1.4")
                        temp_car = F1Car(temp_brand, temp_power, temp_weight, temp_downforce)
                        cars.append(temp_car)
                        print(f"Your {temp_brand} F1∟ car has been created successfully !")
                    case 2: # IF GT CAR
                        while True:
                            temp_tc = input("For a GT Car, you need to choose if it has traction control (y/n) (traction control on -> better performance) : ")
                            match temp_tc.lower():
                                case "y":
                                    temp_tc = True
                                    break
                                case "n":
                                    temp_tc = False
                                    break
                                case _:
                                    print("Error ! Please enter 'y' or 'n' to choose whether you want traction control on your GT car or not !")
                        temp_car = GTCar(temp_brand, temp_power, temp_weight, temp_tc)
                        cars.append(temp_car)
                        print(f"Your {temp_brand} GT car has been created successfully !")
                    case 3: # IF RALLY CAR
                        while True:
                            try:
                                temp_bonus = float(input("For a Rally Car, you need to choose a bonus between 0.1-0.3 : "))
                            except ValueError:
                                print("Error ! Please enter a DECIMAL NUMBER between 0.1-0.3 !")
                            else:
                                if 0.1 <= temp_bonus <= 0.3:
                                    break
                                else:
                                    print("Error ! Please enter a decimal number BETWEEN 0.1-0.3 !")
                        temp_car = RallyCar(temp_brand, temp_power, temp_weight, temp_bonus)
                        cars.append(temp_car)
                        print(f"Your {temp_brand} Rally car has been created successfully !")
                input("Enter to return to the main menu ")
            case 3: # RACE CREATION
                print("Alright ! Let's create a race !")
                temp_name = input("Enter a name for your race : ")
                while True: # DRIVER CHOICE
                    display_drivers()
                    try:
                        temp_driver = int(input("Choose the number of the driver you want to use for this race : "))
                    except ValueError:
                        print("Error ! Please enter a valid driver NUMBER !")
                    else:
                        if temp_driver > len(drivers) or temp_driver == 0:
                            print("Error ! Please enter a valid driver number !")
                        else:
                            break
                while True: # CAR CHOICE
                    display_cars()
                    try:
                        temp_car = int(input("Choose the number of the car you want to use for this race : "))
                    except ValueError:
                        print("Error ! Please enter a valid car NUMBER !")
                    else:
                        if temp_car > len(drivers) or temp_car == 0:
                            print("Error ! Please enter a valid car number !")
                        else:
                            break
                temp_race = Race(temp_name, drivers[temp_driver - 1], cars[temp_car - 1])
                races.append(temp_race)
                print(f"Race '{temp_name}' has been created succesfully !")
                input("Enter to return to main menu ")
            case 4: # RACE RUN
                while True: # RACE CHOICE
                    display_races()
                    try:
                        temp_race = int(input("Choose the number of the race you want to run : "))
                    except ValueError:
                        print("Error ! Please enter a valid race NUMBER !")
                    else:
                        if temp_race > len(races) or temp_race == 0:
                            print("Error ! Please enter a valid race number !")
                        else:
                            break
                print()
                races[temp_race - 1].run()
                print()
                input("Enter to return to main menu ")
            case 5: # CREATIONS DISPLAY
                while True:
                    while True:
                        try:
                            display_choice = int(input("1. Drivers\n"
                                                   "2. Cars\n"
                                                   "3. Races\n"
                                                   "What do you want to display ? : "))
                        except ValueError:
                            print("Error ! Please enter a valid choice NUMBER !")
                        else:
                            break
                    match display_choice:
                        case 1: # DRIVERS DISPLAY
                            display_drivers()
                            break
                        case 2: # CARS DISPLAY
                            display_cars()
                            break
                        case 3: # RACES DISPLAY
                            display_races()
                            break
                        case _: # ERROR
                            print("Error ! Please enter a valid choice number BETWEEN 1-3 !")
                input("Enter to return to the main menu ")
            case 6: # QUIT
                is_running = False
            case _: # IF NO MATCH
                print("Error ! Please enter a valid menu number BETWEEN 1-6 !")
if __name__ == "__main__":
    main()