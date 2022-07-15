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
        
        print()
        print(f"{Fore.GREEN}Created Your Anime List!")
        
        sleep(1)
        
        return 

    return


def mainMenu():
    while True:
        os.system(cls)

        print("######### Main Menu #########")
        print("#                           #")
        print("#  1. Add Anime             #")
        print("#  2. Remove Anime          #")
        print("#  3. Change Anime Rating   #")
        print("#  4. Finished an Anime     #")
        print("#  5. View Anime List       #")
        print("#  6. Anime List Stats      #")
        print("#  7. Unwatched Animes      #")
        print("#  8. Exit                  #")
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
            FinishedAnAnime.finishedAnAnimePart1()
        elif uI == "5":
            viewAnimeList()
        elif uI == "6":
            getAnimeListStats()
        elif uI == "7":
            listUnwatchedAnimes()
        elif uI == "8":
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

        for anime in animeListFile:
            if str(anime) == animeName:
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
                for anime in animeListFile:
                    if animeName == str(anime):
                        del animeListFile[anime]
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
                for anime in animeListFile:
                    if animeName == str(anime):
                        while True:
                            os.system(cls)

                            print("~~~~~ Change Anime Rating ~~~~~")
                            print()
                            print("Type 'rs' to view the anime rating scale.")
                            print()
                            animeRating = input("What would you lke to change the rating to?: ")

                            if animeRating.lower() == "rs":
                                listAnimeRatings()
                            elif animeRating.upper() in ratingScale:
                                ChangeAnimeRating.changeAnimeRatingPart2(animeName, animeRating)
                                return
                            else:
                                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Please enter a proper rating from the rating scale.")

                print()
                print(f"{Fore.RED}ERROR!: {Fore.WHITE}Unable to find anime in anime list.")
                sleep(1)

    
    def changeAnimeRatingPart2(animeName, animeRating):
        animeListFile = loadFile()

        for anime in animeListFile:
            if str(anime) == animeName:
                prevRating = animeListFile[anime]['rating']
                animeListFile[anime]['rating'] = animeRating

        with open(f"{cwd}\\Anime List.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(animeListFile, indent=4, sort_keys=True))
            file.close()

        print()
        print(f"{Fore.CYAN}Changed anime rating from '{prevRating}' to '{animeRating}'.")
        sleep(1)

        return 


class FinishedAnAnime():
    def finishedAnAnimePart1():
        os.system(cls)

        animeListFile = loadFile()

        for anime in animeListFile:
            if animeListFile[anime]['watched'] == False:

                print(f"Anime: {anime}")
                print("~"*15)

        print()

        animeInList = False
        while True:
            animeName = input("Which anime have you watched?: ")

            for anime in animeListFile:
                if animeName == str(anime):
                    animeInList = True 

            if animeInList == True:
                break

            print(f"{Fore.RED}ERROR!: {Fore.WHITE}Anime not found in anime list.")

        FinishedAnAnime.finishedAnAnimePart2(animeName)

        return


    def finishedAnAnimePart2(animeName):
        animeListFile = loadFile()

        while True:
            os.system(cls)

            print(f"~~~~~~ Rating Anime: {animeName} ~~~~~~")
            print()
            print("Type 'rs' to view the anime rating scale.")
            print()

            animeRating = input("What would you like to rate this anime?: ")

            if animeRating.lower() == "rs":
                listAnimeRatings()
            elif animeRating.upper() in ratingScale:
                break

        for anime in animeListFile:
            if str(anime) == animeName:
                animeListFile[animeName]['rating'] = animeRating
                animeListFile[animeName]['watched'] = True
                
                break

        with open(f"{cwd}\\Anime List.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(animeListFile, indent=4, sort_keys=True))
            file.close()

        print()
        print(f"{Fore.CYAN}Congrats on Finishing '{animeName}'!")
        print(f"{Fore.CYAN}Anime Rating: {getRatingColor(animeRating)}{animeRating}")
        sleep(1)

        return 


def viewAnimeList():
    os.system(cls)
    
    animeListFile = loadFile()

    for anime in animeListFile:
        ratingColor = getRatingColor(str(animeListFile[anime]['rating']))

        print(f"Anime: {anime}")

        if animeListFile[anime]['watched'] != False:
            print(f"Rating: {ratingColor}{animeListFile[anime]['rating']}")
        
        print(f"Watched: {animeListFile[anime]['watched']}")
        print("~"*25)

    print()
    input("Press ENTER to Return...")

    return


def listUnwatchedAnimes():
    os.system(cls)
    
    animeListFile = loadFile()

    for anime in animeListFile:
        if animeListFile[anime]['watched'] == False:

            print(f"Anime: {anime}")
            print("~"*15)

    print()
    input("Press ENTER to Return...")

    return


def getAnimeListStats():
    os.system(cls)

    animeListFile = loadFile()

    watchCount = 0
    unwatchedCount = 0
    for anime in animeListFile:
        if animeListFile[anime]['watched'] == True:
            watchCount += 1
        else:
            unwatchedCount += 1

    divideCount = 0
    averageRatingCount = 0
    for anime in animeListFile:
        if animeListFile[anime]['rating'] != "":
            averageRatingCount += ratingScale.index(str(animeListFile[anime]['rating']))
            divideCount += 1

    averageRatingCount = averageRatingCount / divideCount
    averageRatingCount = int(averageRatingCount)
    averageRatingCount = ratingScale[averageRatingCount]

    ratingColor = getRatingColor(averageRatingCount)

    print("~~~~~~ Anime List Statistics ~~~~~~")
    print()
    print(f"Animes Watched: {watchCount}")
    print(f"Animes Unwatched: {unwatchedCount}")
    print()
    print(f"Average Anime Rating: {ratingColor}{averageRatingCount}")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    input("Press ENTER Key to Return...")

    return

# ["U", "SSS", "SS", "S", "A", "B", "C", "D", "F"]
def getRatingColor(rating):
    if rating == "":
        return Fore.RED
    elif ratingScale.index(rating) == 0:
        return Fore.MAGENTA
    elif ratingScale.index(rating) >= 1 and ratingScale.index(rating) <= 2:
        return Fore.CYAN
    elif ratingScale.index(rating) >= 3 and ratingScale.index(rating) <= 4:
        return Fore.GREEN
    elif ratingScale.index(rating) >= 5 and ratingScale.index(rating) <= 6:
        return Fore.YELLOW
    elif ratingScale.index(rating) >= 7 and ratingScale.index(rating) <= 8:
        return Fore.RED


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
