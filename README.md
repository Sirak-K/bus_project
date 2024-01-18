
  

# Buss Simulation

  

# Innehållsförteckning

  

-  [Projektbeskrivning](#projektbeskrivning)

-  [Funktioner](#funktioner)

-  [Hur man installerar](#how-to-install)

-  [Hur man använder](#how-to-use)

-  [Hur man testar](#how-to-test)

-  [Teknologi som använts](#technologies-used)

-  [Licens](#license)

-  [Kontakt](#kontakt)

  

## Projektbeskrivning

#### Projektet handlar om att simulera busspassagerare med syftet att undersöka passagerarnas personliga egenskaper som t ex den genomsnittliga åldern.

#### Detta program kan användas av företag som vill använda sig av digitala simuleringar för att förbättra deras produkt.

  

## Funktionalitet

#### 1) Lägga till passagerare

- Namn

- Ålder

- Kön

#### 2) Ta bort passagerare

#### 3) Visa passagerarinformation

- Visa alla passagerare
- Visa alla manliga passagerare
- Visa alla kvinnliga passagerare
- Visa alla passageraråldrar
- Visa passageraråldrar baserat på ett användargivet åldersintervall

- Sortera passagerarinformation efter namn
- Sortera passagerarinformation efter ålder

#### 4) Beräkna den genomsnittliga åldern

#### 5) Beräkna den sammanlagda åldern

#### 6) Avsluta programmet

## Hur man installerar

1. Se till att du har Python 3.x installerat på din dator.

2. Klona det här förrådet till din lokala dator med följande kommando:

```git clone https://github.com/Sirak-K/bus_project.git```

  

- Om du föredrar det kan du också ladda ner ZIP-filen för förvaret genom att klicka på knappen "Code" på den här sidan och sedan välja "Ladda ner ZIP."

  

## Hur man använder

1. För att köra busssimuleringsmjukvaran i en terminal, skriv "python Project_Buss.py" och tryck på Enter.

2. Välj ett alternativ från menyn.

3. För att avsluta programmet, välj menyalternativ #7 i huvudmenyn.

  

## Pseudokod

  

**Pseudokod för att Sortera Passagerare baserat på Namn:**

    Funktion sort_passengers_by_name():
    
    Om antalet passagerare är noll:
    
    Skriv ut "Inga passagerare hittades."

    Annars:

    Skapa en sorterad lista av passagerare med hjälp av attrgetter för namn

    Skriv ut "Passagerare sorterade efter namn:"
    
    För varje index, passagerare i den sorterade listan:
    
    Skriv ut "Namn:", "Ålder:","Kön:"

  

**Pseudokod för att Skriva ut Alla Åldrar:**

    Funktion display_passenger_ages():
    
    Om antalet passagerare är noll:
    
    Skriv ut "Inga passagerare hittades."
    
    Annars:
    
    Skriv ut "Passageraråldrar:"
    
    För varje passagerare i alla_passagerare:
    
    Skriv ut passagerarens ålder

  

**Pseudokod för att Sortera Passagerare baserat på Ålder:**

    Funktion sort_passengers_by_age():
    
    Om antalet passagerare är noll:
    
    Skriv ut "Inga passagerare hittades."
    
    Annars:
   
    Sortera alla_passagerare efter ålder i fallande ordning
    
    Skriv ut "Passagerare sorterade efter ålder (högsta till lägsta):"
    
    För varje index, passagerare i den sorterade listan:
    
    Skriv ut "Namn:", "Ålder:","Kön:"


## Aktivitetsdiagram

  1.  **Huvudaktiviteter:**
    -   Starta bussprogrammet
    -   Lägg till passagerare
    -   Ta bort passagerare
    -   Visa & sortera passagerarinformation
    -   Beräkna medelåldern
    -   Beräkna total ålder
    
2.  **Sekvenser:**
    -   Starta bussprogrammet -> Välj alternativ (loop)
    -   Lägg till passagerare -> Inmatningshantering för passagerarinformation -> Lägg till passagerare i listan
    -   Ta bort passagerare -> Välj passagerare att ta bort -> Ta bort passagerare från listan
    -   Visa passagerarinformation -> Välj visningsalternativ -> Visa information baserat på val
    -   Beräkna medelåldern -> Samla in åldrar -> Beräkna och visa genomsnittet
    -   Beräkna total ålder -> Samla in åldrar -> Beräkna och visa total ålder
    -   Sortera passagerare -> Välj sorteringsalternativ -> Sortera och visa passagerare
  
![Diagram_2](https://github.com/Sirak-K/bus_project/assets/122515678/4d98f8e1-d935-4b94-b030-26f464002a42)



## Kodkomponenter
![Projekt_Buss_Kodkomponenter](https://github.com/Sirak-K/bus_project/assets/122515678/43952297-4934-4c82-ab44-c6b37b5c596f)


## Testning
![Projekt_Buss_Testning](https://github.com/Sirak-K/bus_project/assets/122515678/ff7243e0-000c-426e-9595-50bf4614873e)


## Teknik som använts

- Programmeringsspråk: Python

- Python-modul för att sortera passagerare: `from operator import attrgetter`

  

## Licens

Detta projekt är licensierat under MIT-licensen.

  

## Kontakt

För frågor eller feedback, vänligen kontakta [sirak.dev@gmail.com](mailto:sirak.dev@gmail.com).
