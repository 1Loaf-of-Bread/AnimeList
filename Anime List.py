from this import s
from colorama import Fore, init 
from time import sleep 
import json
import os
init(autoreset=True)

cls = 'cls'
cwd = os.getcwd()
ratingScale = ["U", "SSS", "SS", "S", "A", "B", "C", "D", "F"]


def checkAnimeListExist():
    if not os.path.isfile(f"{cwd}\\Anime List.json"):

        print(f"{Fore.CYAN}Creating Your Anime List...")

        with open(f"{cwd}\\Anime List.json", 'w') as file:
            file.close()
        
        print(f"{Fore.GREEN}Created Your Anime List!")
        
        sleep(1)
        
        os.system(cls)
        return 

    os.system(cls)
    return


def mainMenu():
    while True:
        os.system(cls)

        print("######### Main Menu #########")
        print("#                           #")
        print("#  1. Add Anime             #")
        print("#  2. Remove Anime          #")
        print("#  3. Change Anime Rating   #")
        print("#  4. View Anime List       #")
        print("#  5. Anime List Stats      #")
        print("#  6. Exit                  #")
        print("#                           #")
        print("#############################")
        print()

        uI = input("--> ")

        if uI == "1":
            AddAnime.addAnimePart1()
        elif uI == "2":
            RemoveAnime.removeAnimePart1()
        elif uI == "3":
            ChangeAnimeRating.changeAnimeRatingPart1()
        elif uI == "4":
            viewAnimeList()
        elif uI == "5":
            getAnimeListStats()
        elif uI == "6":
            exit()
        else:
            print()
            print(f"{Fore.RED}ERROR!: {Fore.WHITE}Please enter a numerical value from the choices provided in the menu list.")


class AddAnime():
    def addAnimePart1():
        os.system(cls)
        
        print("###### Add Anime ######")
        print()
        animeName = input("Enter Anime Name: ")

        animeListFile = loadFile()

        for key in animeListFile:
            if str(key) == animeName:
                print(f"{Fore.RED}ERROR!: {Fore.WHITE}This anime already exists in your anime list")
                sleep(1)

                return
        
        AddAnime.addAnimePart2(animeName)
        
        return


    def addAnimePart2(animeName):
        while True:
            os.system(cls)

            print("~~~~~~ Add Anime ~~~~~~")
            print()
            
            uI = input("Have you watched this anime? (y/n): ")

            if uI.lower() == "y":
                AddAnime.addAnimePart3(animeName)
                return
            elif uI.lower() == "n":
                AddAnime.addAnimeToFile(animeName, "", False)
                return


    def addAnimePart3(animeName):
        while True:
            os.system(cls)

            print("~~~~~~ Add Anime ~~~~~~")
            print()
            print("Type 'rs' to list the anime rating scale.")
            print()

            animeRating = input("What would you rate this anime?: ")

            if animeRating.lower() == "rs":
                listAnimeRatings()
            elif animeRating.upper() not in ratingScale:
                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Please enter a proper rating from the rating scale.")
            else:
                AddAnime.addAnimeToFile(animeName, animeRating, True)
                return

            
    def addAnimeToFile(animeName, animeRating, watched):
        animeListFile = loadFile()
        
        animeListFile.update({
            f"{animeName}": {
                "watched": watched,
                "rating": str(animeRating).upper()
            }
        })

        with open(f"{cwd}\\Anime List.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(animeListFile, indent=4, sort_keys=True))
            file.close()

        print()
        print(f"{Fore.CYAN}Added Anime '{animeName}' to Anime List.")
        sleep(1)

        return 


class RemoveAnime():
    def removeAnimePart1():
        os.system(cls)

        animeListFile = loadFile()

        while True:
            os.system(cls)

            print("~~~~~ Remove Anime ~~~~~")
            print()
            print("Type 'al' to view your anime list.")
            print()

            animeName = input("Which anime would you like to remove?: ")

            if animeName.lower() == "al":
                viewAnimeList()
            else:
                for key in animeListFile:
                    if animeName == str(key):
                        del animeListFile[key]
                        RemoveAnime.removeAnimePart2(animeListFile, animeName)
                        return

                print()
                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Unable to find anime in anime list.")
                sleep(1)


    def removeAnimePart2(animeListFile, animeName):
        with open(f"{cwd}\\Anime List.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(animeListFile, indent=4, sort_keys=True))
            file.close()

        print()
        print(f"{Fore.CYAN}Removed Anime: {animeName}")
        sleep(1)

        return 


class ChangeAnimeRating():
    def changeAnimeRatingPart1():
        animeListFile = loadFile()

        while True:
            os.system(cls)

            print("~~~~~ Change Anime Rating ~~~~~")
            print()
            print("Type 'al' to view your anime list.")
            print()

            animeName = input("Which anime rating would you like to change?: ")

            if animeName.lower() == "al":
                viewAnimeList()
            else:
                for key in animeListFile:
                    if animeName == str(key):
                        while True:
                            os.system(cls)

                            print("~~~~~ Change Anime Rating ~~~~~")
                            print()
                            
                            animeRating = input("What would you lke to change the rating to?: ")
                            animeRating = animeRating.upper()

                            if animeRating in ratingScale:
                                ChangeAnimeRating.changeAnimeRatingPart2(animeName, animeRating)
                                return
                            else:
                                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Please enter a proper rating from the rating scale.")

                print()
                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Unable to find anime in anime list.")
                sleep(1)

    
    def changeAnimeRatingPart2(animeName, animeRating):
        animeListFile = loadFile()

        for key in animeListFile:
            if str(key) == animeName:
                prevRating = animeListFile[key]['rating']
                animeListFile[key]['rating'] = animeRating

        with open(f"{cwd}\\Anime List.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(animeListFile, indent=4, sort_keys=True))
            file.close()

        print()
        print(f"{Fore.CYAN}Changed anime rating from '{prevRating}' to '{animeRating}'.")
        sleep(1)

        return 


def viewAnimeList():
    os.system(cls)
    
    animeListFile = loadFile()

    for key in animeListFile:
        print(f"Anime: {key}")
        print(f"Rating: {animeListFile[key]['rating']}")
        print(f"Watched: {animeListFile[key]['watched']}")
        print("~"*25)
        print()

    print()
    input("Press ENTER to Return...")

    return


def getAnimeListStats():
    os.system(cls)

    animeListFile = loadFile()

    watchCount = 0
    unwatchedCount = 0
    for key in animeListFile:
        if animeListFile[key]['watched'] == True:
            watchCount += 1
        else:
            unwatchedCount += 1

    divideCount = 0
    averageRatingCount = 0
    for key in animeListFile:
        if animeListFile[key]['rating'] != "":
            averageRatingCount += ratingScale.index(str(animeListFile[key]['rating']))
            divideCount += 1

    averageRatingCount = averageRatingCount / divideCount
    averageRatingCount = int(averageRatingCount)

    print("~~~~~~ Anime List Statistics ~~~~~~")
    print()
    print(f"Animes Watched: {watchCount}")
    print(f"Animes Unwatched: {unwatchedCount}")
    print()
    print(f"Average Anime Rating: {ratingScale[averageRatingCount]}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press ENTER Key to Return...")

    return


def listAnimeRatings():
    os.system(cls)

    print("~~~~~~ Anime Rating Scale ~~~~~~")
    print()
    print("From top to bottom: highest rating to lowest rating.")
    print()

    for rating in ratingScale:
        print(rating)
    
    print()
    input("Press ENTER Key to Return...")

    return


def loadFile():
    with open(f"{cwd}\\Anime List.json", "r") as file:
        animeList = json.load(file)

    return animeList




if __name__ == "__main__":
    checkAnimeListExist()
    mainMenu()