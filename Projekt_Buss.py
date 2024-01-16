from operator import attrgetter

class Passenger:
    # Constructor Method - Ran when class is created.
    def __init__(self, name, age, gender):
        # Attributes in classes are called fields.
        self.name = name
        self.age = age
        self.gender = gender


class Bus:
    MAX_PASSENGERS = 3

    def __init__(self):
        self.all_passengers = []  # Vektor för att lagra alla passagerare
        self.passenger_ages = []  # Vektor för att lagra passagerarnas åldrar
    
    # Method #1: Start the bus program
    def start_bus_program(self):
        while True:
            print("\nWelcome to the Bus Simulator:")
            print("1. Add passenger")
            print("2. Remove passenger")
            print("3. Show passenger information")
            print("4. Calculate the average age of all passengers")
            print("5. Calculate the total age of all passengers")
            print("6. Exit the program")

            choice = input("Please choose an option (1-6): ")

# Menyval 1: Lägg till passagerare
            if choice == '1':
                self.add_passenger()
# Menyval 2: Ta bort passagerare
            elif choice == '2':
                self.remove_passenger()
# Menyval 3: Visa passagerarinformation
            elif choice == '3':
                self.show_passenger_info()
# Menyval 4: Beräkna medelåldern för alla passagerare
            elif choice == '4':
                self.calc_age_average()
# Menyval 5: Beräkna den totala åldern för alla passagerare
            elif choice == '5':
                self.calc_age_total()
# Menyval 6: Avsluta programmet
            elif choice == '6':
                print("The program is exiting. Thank you for using the Bus Simulator!")
                break
            else:
                print("Invalid choice. Please try again.")

# Method #2: Add a passenger to the bus
    def add_passenger(self):
        try:
            # Inmatningshantering för namn
            while True:
                name = input("Enter the passenger's name: ").strip().capitalize()

                if not (1 <= len(name) <= 20) or not name.isalpha():
                    print("Invalid name. Please enter a name with 1-20 alphabetical characters.")
                else:
                    break

            age = input("Enter the passenger's age: ")
            gender = None  # Initialize gender as None to start the loop

            while gender not in ['M', 'F']:
                gender = input("Enter the passenger's gender (M/F): ").strip().upper()

                if gender not in ['M', 'F']:
                    print("Invalid choice. Please enter 'M' or 'F'.")

            age = int(age)
            if not (1 <= age <= 100):
                raise ValueError("Age must be between 1 and 100.")

            if len(self.all_passengers) < self.MAX_PASSENGERS:
                gender_full = "Male" if gender == 'M' else "Female"
                new_passenger = Passenger(name, age, gender)
                self.all_passengers.append(new_passenger)
                self.passenger_ages.append(age)  # Lägg till åldern i den nya vektorn
                print(f"Passenger added: Name: {name}, Gender: {gender_full}, Age: {age}")
            else:
                print(f"Maximum number of passengers ({self.MAX_PASSENGERS}) reached. Cannot add more passengers.")

        except ValueError as e:
            print(f"Invalid input: {e}")

    # Method #3: Delete a passenger from the bus
    def remove_passenger(self):
        try:
            if not self.all_passengers:
                print("No passengers found.")
                return

            index = input("Enter the index of the passenger to remove: ")
            index = int(index)

            if not (0 <= index < len(self.all_passengers)):
                raise ValueError("No passenger found at the chosen index.")

            removed_passenger = self.all_passengers.pop(index)
            print(f"Passenger removed: Age {removed_passenger.age}, Gender {removed_passenger.gender}")

        except ValueError as e:
            print(f"Invalid input: {e}")

# Method #4: Display passenger information based on user's choice
    def show_passenger_info(self):
        try:
            if not self.all_passengers:
                print("No passengers found.")
                return

            print("Display passenger information:")
            print("1. Show all passengers")
            print("2. Show men")
            print("3. Show women")
            print("4. Show passenger ages")
            print("5. Show passengers within age interval")
            print("6. Sort all passengers by name")
            print("7. Sort all passengers by age")

            display_choice = input("Please choose an option (1-6): ")

            if display_choice == '1':
                self.display_passenger_group("All Passengers", self.all_passengers)
            elif display_choice == '2':
                men = [passenger for passenger in self.all_passengers if passenger.gender.lower() == 'm']
                if not men:
                    print("No male passengers found.")
                else:
                    self.display_passenger_group("Men", men)
            elif display_choice == '3':
                women = [passenger for passenger in self.all_passengers if passenger.gender.lower() == 'f']
                if not women:
                    print("No female passengers found.")
                else:
                    self.display_passenger_group("Women", women)
            elif display_choice == '4':
                self.display_passenger_ages()
            elif display_choice == '5':
                self.display_passengers_within_age_interval()
            elif display_choice == '6':
                self.sort_passengers_by_name()
            elif display_choice == '7':
                self.sort_passengers_by_age()
            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")



# Helper method to display the vector of passenger group
    def display_passenger_group(self, passenger_group_name, passengers):
        print(f"\n{passenger_group_name} Information:")
        for i, passenger in enumerate(passengers, 1):
            print(f"{i}. Name: {passenger.name}, Age: {passenger.age}, Gender: {passenger.gender}")

# Helper method to display the vector of passenger ages
    def display_passenger_ages(self):
        print("\nPassenger Ages:")
        for i, age in enumerate(self.passenger_ages, 1):
            print(f"{i}. Age: {age}")

# Helper method to display passengers within age interval
    def display_passengers_within_age_interval(self):
        try:
            start_age = int(input("Enter the first and lowest number of the age interval: "))
            end_age = int(input("Enter the second and highest number of the age interval: "))

            if not (1 <= start_age <= 100) or not (1 <= end_age <= 100) or start_age > end_age:
                raise ValueError("Invalid age interval.")

            passengers_within_interval = [passenger for passenger in self.all_passengers if start_age <= passenger.age <= end_age]

            if not passengers_within_interval:
                print(f"No passengers found within the age interval {start_age}-{end_age}.")
            else:
                self.display_passenger_group(f"Passengers within [ {start_age}-{end_age}", passengers_within_interval)

        except ValueError as e:
            print(f"Invalid input: {e}")
            
    # Method #5: Calculate the average age of all passengers
    def calc_age_average(self):
        try:
            # Kontrollera om det finns några passagerare
            if not self.all_passengers:
                print("No passengers found.")
                return

            total_age = sum(passenger.age for passenger in self.all_passengers)
            average_age = total_age // len(self.all_passengers)

            print(f"\nThe average age of all passengers is: {average_age} years.")

        except ValueError as e:
            print(f"Error: {e}")


    # Method #6: Calculate the total age of all passengers
    def calc_age_total(self):
        try:
            # Kontrollera om det finns några passagerare
            if not self.all_passengers:
                print("No passengers found.")
                return

            total_age = sum(passenger.age for passenger in self.all_passengers)

            print(f"\nThe total age of all passengers is: {total_age} years.")

        except ValueError as e:
            print(f"Error: {e}")


# Method #7: Sort all passengers by name
    def sort_passengers_by_name(self):
        try:
            if not self.all_passengers:
                print("No passengers found.")
                return

            # Använd attrgetter för att sortera passagerarna efter namn
            sorted_passengers = sorted(self.all_passengers, key=attrgetter('name'))

            print("\nPassengers sorted by name:")
            for i, passenger in enumerate(sorted_passengers, 1):
                print(f"{i}. Name: {passenger.name}, Age: {passenger.age}, Gender: {passenger.gender}")

        except Exception as e:
            print(f"Error: {e}")

# Method #8: Sort all passengers by age
    def sort_passengers_by_age(self):
        try:
            if not self.all_passengers:
                print("No passengers found.")
                return

            # Använd attrgetter
            sorted_passengers = sorted(self.all_passengers, key=attrgetter('age'))

            print("\nPassengers sorted by age:")
            for i, passenger in enumerate(sorted_passengers, 1):
                print(f"{i}. Name: {passenger.name}, Age: {passenger.age}, Gender: {passenger.gender}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    bus_program = Bus()
    bus_program.start_bus_program()
