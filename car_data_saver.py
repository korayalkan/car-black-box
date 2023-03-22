# Car class
class Car:

    def __init__(self, car_brand, car_model, car_age, car_plate):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_age = car_age
        self.car_plate = car_plate
        self.car_current_gear = []
        self.car_engine_situation = False



    # Start the engine function
    def car_start(self):

        # If the engine is already running
        if self.car_engine_situation:
            print('Car is already running!')

        self.car_engine_situation = True
        print(f'"{self.car_brand} {self.car_model}" is ready for a ride !\n')
        # Save the data here
        return



    # Stop the engine function
    def car_stop(self):

        # If the engine is already stopped
        if not self.car_engine_situation:
            print('Car is already not running!\n')

        elif self.car_engine_situation:
            # Save the data here
            print(f'That was a good ride with "{self.car_brand} {self.car_model}" !\n')



    # Car signal function
    def car_signal(self):

        # If car is not running
        if not self.car_engine_situation:
            print('You should start the engine first.\n')
            quit()

        try:
            signal_direction = int(input('Left  | 1\n'
                                         'Right | 2 : '))

        # Only integer
        except ValueError:
            print(f'Invalid input!\n')
            Car.car_signal(self)
            return

        # Signal to left
        if signal_direction == 1:
            print('Turning left..\n')
            # Save the data here

        # Signal to right
        elif signal_direction == 2:
            print('Turning right..\n')
            # Save the data here



    # Car brakes function
    def car_brakes(self):

        # If car is not running
        if not self.car_engine_situation:
            print('You should start the engine first.\n')
            quit()

        try:
            brake_percentage = int(input('Brake percentage: %'))
            brake_distance = int(input('Brake Distance (meters): '))

        # Only integer
        except ValueError:
            print('Invalid input!\n')
            Car.car_brakes(self)
            return

        # Sudden brake
        if brake_percentage >= 100:
            print('Emergency brakes engaged. Car stopped.\n')
            self.car_engine_situation = False
            # Save the data here

        # If the brakes are used at %0 or lower
        elif brake_percentage <= 0:
            print('You can not use brakes at 0% or lower than 0%.\n')
            # Save the data here
            Car.car_brakes(self)
            return

        # If brakes are used lower than 50%
        elif brake_percentage <= 50:
            print(f'Car slowed down at {brake_percentage}% for {brake_distance} meters.\n')
            # Save the data here

        elif brake_percentage >= 50:
            print(f'Car slowed down at {brake_percentage}% for {brake_distance} meters.\n')
            # Save the data here

        else:
            print('Something went wrong.\n')
            # Save the data here



    # Gear up the car function
        # Current gear has to be entered manually before gearing up
    def car_gear_up(self, starting_gear=1):

        # If car is not running
        if not self.car_engine_situation:
            print('You should start the engine first.\n')
            quit()

        # If user enters current_gear an unavailable number
        elif 0 >= starting_gear >= 6:
            print('System failed!\n'
                  'Car stopped..\n')
            quit()

        try:
            gear_up = int(input('Gear Up to (2-3-4-5) : '))

        # Only integer
        except ValueError:
            print('Invalid input!\n')
            Car.car_gear_up(self, starting_gear)
            return

        # Example: When user gears up from 1 to 3
        if (gear_up - starting_gear) > 1:
            print('Failed gearing up!\n')
            # Save the data here
            Car.car_gear_up(self, starting_gear)
            return

        # Example: Current gear is 3, user tries to change it to 2. Automatically fails
        elif starting_gear > gear_up:
            print('Failed gearing up!\n')
            # Save the data here
            Car.car_gear_up(self, starting_gear)
            return

        # Example: Gear is 1, user tries to change it to 1 again
        elif gear_up == starting_gear:
            print(f'Already on gear {gear_up}!\n')
            # Save the data here
            Car.car_gear_up(self, starting_gear)
            return

        # Gearing up to 2
        elif gear_up == 2:
            starting_gear += 1
            print('Geared up to 2..\n')
            # Save the data here

        # Gearing up to 3
        elif gear_up == 3:
            starting_gear += 1
            print('Geared up to 3..\n')
            # Save the data here

        # Gearing up to 4
        elif gear_up == 4:
            starting_gear += 1
            print('Geared up to 4..\n')
            # Save the data here

        # Gearing up to 5
        elif gear_up == 5:
            starting_gear += 1
            print('Geared up to 5..\n')
            # Save the data here

        # If user gears up to a non-existing number
        elif 0 <= gear_up <= 6:
            print('Can not gear up to non-existing gears.\n')
            Car.car_gear_up(self, starting_gear)
            return



    # Downshift the car function
        # Current gear has to be entered manually before downshifting
    def car_downshift(self, current_gear=5):

        # If car is not running
        if not self.car_engine_situation:
            print('You should start the engine first.\n')
            quit()

        # If user enters current_gear an unavailable number
        elif 0 >= current_gear >= 6:
            print('System failed!\n'
                  'Car stopped..\n')
            quit()

        try:
            downshift_to = int(input('Downshift to (4-3-2-1) : '))

        # Only integer
        except ValueError:
            print('Invalid input!\n')
            Car.car_downshift(self, current_gear)
            return

        # Example: When user downshifts from 3 to 1
        if (current_gear - downshift_to) > 1:
            print('Downshifting failed!\n')
            # Save the data here
            Car.car_downshift(self, current_gear)
            return

        # Example: Current gear is 2, user tries to change it to 3. Automatically fails
        elif downshift_to > current_gear:
            print('Downshifting failed!\n')
            # Save the data here
            Car.car_downshift(self, current_gear)
            return

        # Example: Gear is 1, user tries to change it to 1 again
        elif downshift_to == current_gear:
            print(f'Already on gear {downshift_to}!\n')
            # Save the data here
            Car.car_downshift(self, current_gear)
            return

        # Downshifting to 4
        elif downshift_to == 4:
            print('Downshifted to 4..')
            # Save the data here

        # Downshifting to 3
        elif downshift_to == 3:
            print('Downshifted to 3..')
            # Save the data here

        # Downshifting to 2
        elif downshift_to == 2:
            print('Downshifted to 2..')
            # Save the data here

        # Downshifting to 1
        elif downshift_to == 1:
            print('Downshifted to 1..')
            # Save the data here

        # If user gears up to a non-existing number
        elif 0 <= downshift_to <= 6:
            print('Can not downshift to non-existing gears.\n')
            Car.car_gear_up(self, downshift_to)
            return



car1 = Car("Mercedes", "E250", 10, "01 KA 0508")
# Car.car_start(car1)
# Car.car_signal(car1)
# Car.car_gear_up(car1, 3)
# Car.car_brakes(car1)
# Car.car_downshift(car1, 4)
# Car.car_stop(car1)
