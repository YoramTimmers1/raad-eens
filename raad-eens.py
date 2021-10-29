from math import radians
import random
Poging = None  #de variable bestaand zonder waarde
Raadhetgetal = None #de variable bestaand zonder waarde

for ronde in range(20): #Dit zorgt ervoor als ik het random getal raad start een nieuwe ronde
    RandomAntwoord = random.randint(1,1000) #Dit zorgt ervoor dat ik een random getal krijg 1 tot 1000
    print(RandomAntwoord) # verwijder als het af is
    Poging = 0

    while Poging < 10: #je kan het 10 keer proberen anders ga je game over
        Raadhetgetal = input("Raad het getal : ")
        
        
        if Raadhetgetal == "quit":
            print(f"JE SCORE IS:  {ronde}") #F zorgt er voor dat je je variable omzet in het gene wat hij nodig heeft zoals een string of een int
            exit()
        Raadhetgetal = int(Raadhetgetal)                  # anders raad het progamma niet goed
        Poging = Poging + 1
        print(f"Dit was poging {Poging}")
    
        if Raadhetgetal in range(RandomAntwoord - 20, RandomAntwoord + 20): #Als het getal in de range is laat het weten of het heel warm is
            print("HEEL WARM!")
        
        elif Raadhetgetal in range(RandomAntwoord - 50, RandomAntwoord + 50): #Als het getal in de range is laat het weten of het warm is
            print("Warm!")

        if Raadhetgetal > RandomAntwoord:
            print("Lager")
        if Raadhetgetal < RandomAntwoord:
            print("Hoger")    

        if Raadhetgetal == RandomAntwoord:
            print("Je hebt het getal geraden GJ!")
            NogEenKeer = input("Wil je nog een keer? j/n :") 
            if NogEenKeer == "j":
                break                            #het haalt je uit de huidige loop
            elif NogEenKeer == "n":
                print("JE SCORE IS: " + ronde)
                exit()                          #het sluit het progamma af
    print("GAME OVER!")
    print("JE SCORE IS: " + ronde)
    exit()
