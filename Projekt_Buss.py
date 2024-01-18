from operator import attrgetter

class Passenger:
    def __init__(self, name, age, gender):
        """
        Skapar en passagerare med angivet namn, ålder och kön.

        Args:
        - name (str): Namnet på passageraren.
        - age (int): Åldern på passageraren.
        - gender (str): Könet på passageraren ('M' för man eller 'F' för kvinna).
        """
        self.name = name
        self.age = age
        self.gender = gender


class Bus:
    MAX_PASSENGERS = 25

    def __init__(self):
        """
        Skapar en instans av bussklassen.

        Attributes:
        - all_passengers (list): Lista som lagrar alla passagerare.
        - passenger_ages (list): Lista som lagrar åldrarna på passagerarna.
        """
        self.all_passengers = []
        self.passenger_ages = []

    def start_bus_program(self):
        """
        Startar bussprogrammet och visar huvudmenyn för användaren.
        Användaren kan välja olika alternativ som att lägga till passagerare,
        ta bort passagerare, visa passagerarinformation, beräkna medelåldern,
        beräkna totalåldern eller avsluta programmet.
        """
        while True:
            print("\nVälkommen till bussimulatorn:")
            print("1. Lägg till passagerare")
            print("2. Ta bort passagerare")
            print("3. Visa passagerarinformation")
            print("4. Beräkna medelåldern för alla passagerare")
            print("5. Beräkna den totala åldern för alla passagerare")
            print("6. Avsluta programmet")

            choice = input("Vänligen välj ett alternativ (1-6): ")

            if choice == '1':
                self.add_passenger()
            elif choice == '2':
                self.remove_passenger()
            elif choice == '3':
                self.show_passenger_info()
            elif choice == '4':
                self.calc_age_average()
            elif choice == '5':
                self.calc_age_total()
            elif choice == '6':
                print("Programmet avslutas. Tack för att du använder bussimulatorn!")
                break
            else:
                print("Ogiltigt val. Var vänlig försök igen.")

    def add_passenger(self):
        """
        Lägger till en passagerare till bussen efter att ha hanterat korrekt inmatning av information.
        """
        try:
            while True:
                name = input("Ange passagerarens namn: ").strip().capitalize()
                if not (1 <= len(name) <= 20) or not name.isalpha():
                    print("Ogiltigt namn. Ange ett namn med 1-20 bokstäver.")
                else:
                    break

            while True:
                age_input = input("Ange passagerarens ålder: ")
                if age_input.isdigit():
                    age = int(age_input)
                    if 0 <= age <= 100:
                        break
                    else:
                        print("Ogiltig ålder. Åldern måste vara mellan 0 och 100.")
                else:
                    print("Ogiltig ålder. Ange ett numeriskt värde.")

            gender = None
            while gender not in ['M', 'F']:
                gender = input("Ange passagerarens kön (M/F): ").strip().upper()
                if gender not in ['M', 'F']:
                    print("Ogiltigt val. Ange 'M' för man eller 'F' för kvinna.")

            if len(self.all_passengers) < self.MAX_PASSENGERS:
                gender_full = "Man" if gender == 'M' else "Kvinna"
                new_passenger = Passenger(name, age, gender)
                self.all_passengers.append(new_passenger)
                self.passenger_ages.append(age)
                print(f"Passagerare tillagd: Namn: {name}, Kön: {gender_full}, Ålder: {age}")
            else:
                print(f"Maximalt antal passagerare ({self.MAX_PASSENGERS}) nått. Kan inte lägga till fler passagerare.")

        except ValueError as e:
            print(f"Ogiltig inmatning: {e}")

    def remove_passenger(self):
        """
        Tar bort en passagerare från bussen baserat på användarens valda index.
        """
        try:
            if not self.all_passengers:
                print("Inga passagerare hittade.")
                return

            index = input("Ange index för passageraren att ta bort: ")
            index = int(index)

            if not (0 <= index < len(self.all_passengers)):
                raise ValueError("Ingen passagerare hittades på det valda indexet.")

            removed_passenger = self.all_passengers.pop(index)
            print(f"Passagerare borttagen: Namn {removed_passenger.name}, Ålder {removed_passenger.age}, Kön {removed_passenger.gender}")

        except ValueError as e:
            print(f"Ogiltig inmatning: {e}")

    def show_passenger_info(self):
        """
        Visar information om passagerarna, inklusive olika alternativ som att visa alla passagerare,
        visa män, visa kvinnor, visa passagerarnas åldrar, visa passagerare inom ett åldersintervall,
        sortera passagerare efter namn eller sortera passagerare efter ålder.
        """
        while True:
            try:
                if not self.all_passengers:
                    print("Inga passagerare hittade.")
                    return

                print("Visa passagerarinformation:")
                print("3-A-[1]: Visa alla passagerare")
                print("3-B-[2]: Visa män")
                print("3-C-[3]: Visa kvinnor")
                print("3-D-[4]: Visa passagerarnas åldrar")
                print("3-E-[5]: Visa passagerare inom åldersintervallet")
                print("3-F-[6]: Sortera alla passagerare efter namn")
                print("3-G-[7]: Sortera alla passagerare efter ålder")

                display_choice = input("Vänligen välj ett alternativ (1-7): ")

                if display_choice == '1':
                    self.display_passenger_group("Alla Passagerare", self.all_passengers)
                elif display_choice == '2':
                    men = [passenger for passenger in self.all_passengers if passenger.gender.lower() == 'm']
                    if not men:
                        print("Inga manliga passagerare hittade.")
                    else:
                        self.display_passenger_group("Män", men)
                elif display_choice == '3':
                    women = [passenger for passenger in self.all_passengers if passenger.gender.lower() == 'f']
                    if not women:
                        print("Inga kvinnliga passagerare hittade.")
                    else:
                        self.display_passenger_group("Kvinnor", women)
                elif display_choice == '4':
                    self.display_passenger_ages()
                elif display_choice == '5':
                    self.display_passengers_within_age_interval()
                elif display_choice == '6':
                    self.sort_passengers_by_name()
                elif display_choice == '7':
                    self.sort_passengers_by_age()
                else:
                    print("Ogiltigt val. Var vänlig försök igen.")
                    continue 

            except ValueError as e:
                print(f"Fel: {e}")
            except Exception as e:
                print(f"Fel: {e}")

    def display_passenger_group(self, passenger_group_name, passengers):
        """
        Visar information om en grupp av passagerare.

        Args:
        - passenger_group_name (str): Namnet på passagerargruppen.
        - passengers (list): En lista med passagerare.

        Prints:
        Information om varje passagerare i gruppen.
        """
        print(f"\n{passenger_group_name} Information:")
        for i, passenger in enumerate(passengers, 1):
            print(f"{i}. Namn: {passenger.name}, Ålder: {passenger.age}, Kön: {passenger.gender}")

    def display_passenger_ages(self):
        """
        Visar åldrarna på alla passagerare.
        Prints:
        En lista över åldrarna på alla passagerare.
        """
        print("\nPassagerarnas åldrar: [{}]".format(', '.join(map(str, self.passenger_ages))))

    def display_passengers_within_age_interval(self):
        """
        Visar passagerare inom ett åldersintervall.
        Användaren ombeds ange det lägsta och högsta värdet för åldersintervallet.

        Raises:
        ValueError: Om användaren anger ogiltiga värden.

        Prints:
        Passagerare som ligger inom det angivna åldersintervallet.
        """
        try:
            start_age = int(input("Ange det första och lägsta numret i åldersintervallet: "))
            end_age = int(input("Ange det andra och högsta numret i åldersintervallet: "))

            if not (0 <= start_age <= 100) or not (0 <= end_age <= 100) or start_age > end_age or start_age < 0:
                raise ValueError("Ogiltigt åldersintervall, ange ett numeriskt värde mellan 0 och 100.")

            passengers_within_interval = [passenger for passenger in self.all_passengers if start_age <= passenger.age <= end_age]

            if not passengers_within_interval:
                print(f"Inga passagerare hittades inom åldersintervallet {start_age}-{end_age}.")
            else:
                self.display_passenger_group(f"Passagerare inom [ {start_age}-{end_age}]", passengers_within_interval)

        except ValueError as e:
            print(f"Ogiltig inmatning: {e}")

    def calc_age_average(self):
        """
        Beräknar medelåldern för alla passagerare.

        Raises:
        ValueError: Om inga passagerare hittas.

        Prints:
        Den genomsnittliga åldern för alla passagerare.
        """
        try:
            if not self.all_passengers:
                print("Inga passagerare hittades.")
                return

            total_age = sum(passenger.age for passenger in self.all_passengers)
            average_age = total_age // len(self.all_passengers)

            print(f"\nDen genomsnittliga åldern för alla passagerare är: {average_age} år.")

        except ValueError as e:
            print(f"Fel: {e}")

    def calc_age_total(self):
        """
        Beräknar den totala åldern för alla passagerare.

        Raises:
        ValueError: Om inga passagerare hittas.

        Prints:
        Den totala åldern för alla passagerare.
        """
        try:
            if not self.all_passengers:
                print("Inga passagerare hittades.")
                return

            total_age = sum(passenger.age for passenger in self.all_passengers)

            print(f"\nDen totala åldern för alla passagerare är: {total_age} år.")

        except ValueError as e:
            print(f"Fel: {e}")

    def sort_passengers_by_name(self):
        """
        Sorterar alla passagerare efter namn i stigande ordning.

        Raises:
        ValueError: Om inga passagerare hittas.

        Prints:
        En lista över passagerare sorterade efter namn.
        """
        try:
            if not self.all_passengers:
                print("Inga passagerare hittades.")
                return

            sorted_passengers = sorted(self.all_passengers, key=attrgetter('name'))

            print("\nPassagerare sorterade efter namn:")
            for i, passenger in enumerate(sorted_passengers, 1):
                print(f"{i}. Namn: {passenger.name}, Ålder: {passenger.age}, Kön: {passenger.gender}")

        except Exception as e:
            print(f"Fel: {e}")

    def sort_passengers_by_age(self):
        """
        Sorterar alla passagerare efter ålder i fallande ordning.

        Raises:
        ValueError: Om inga passagerare hittas.

        Prints:
        En lista över passagerare sorterade efter ålder (högst till lägst).
        """
        try:
            if not self.all_passengers:
                print("Inga passagerare hittades.")
                return

            sorted_passengers = sorted(self.all_passengers, key=attrgetter('age'), reverse=True)

            print("\nPassagerare sorterade efter ålder (högst till lägst):")
            for i, passenger in enumerate(sorted_passengers, 1):
                print(f"{i}. Namn: {passenger.name}, Ålder: {passenger.age}, Kön: {passenger.gender}")

        except Exception as e:
            print(f"Fel: {e}")

if __name__ == "__main__":
    # Skapar ett objekt av klassen Bus
    bus_program = Bus()
    # Anropar metoden start_bus_program() som finns i klassen Bus
    bus_program.start_bus_program()
