import pandas as pd
import region_performance
import top_gaming_consoles
import top_global_games
import top_regional_games
import old_game_release
import gaming_genre
import publisher_impact_on_regions
import global_average

def main_menu():
    # Preload dataset
    df=pd.read_csv("content/vgsales.csv")
    df.head()

    # Named constants for readability
    # Capital case for constants according to variable naming conventions
    # "CHOICE" written at the end of each constant name as a naming convention
    REGION_PERFORMANCE_CHOICE = 0
    TOP_GAMING_CONSOLES_CHOICE = 1
    TOP_GLOBAL_GAMES_CHOICE = 2
    TOP_REGIONAL_GAMES_CHOICE = 3
    GAMES_OLD_RELEASES_CHOICE = 4
    GAMING_GENRES_CHOICE = 5
    PUBLISHER_IMPACT_CHOICE = 6
    GLOBAL_AVERAGE_CHOICE = 7
    EXIT_CHOICE = 8

    CHOICE_MINIMUM = 0
    CHOICE_MAXIMUM = 9
    choices = tuple(range(CHOICE_MINIMUM, CHOICE_MAXIMUM))

    while (1):
        print("1. Visualise region performance")
        print("2. Visualise top gaming consoles")
        print("3. Visualise top global games")
        print("4. Visualise top regional games")
        print("5. Visualise top old releases")
        print("6. Visualise top gaming genres")
        print("7. Visualise publisher impact on regions")
        print("8. Visualise global averages")
        print("9. Exit program")
        print()
        user_choice = input("Which choice do you want to pick? ")
        try:
            user_choice = int(user_choice) - 1
        except:
            print("User choice needs to be a valid integer!")
        else:
            if user_choice not in choices:
                print("Invalid choice! Please pick from the selection...")
                continue

        if user_choice == REGION_PERFORMANCE_CHOICE:
            region_performance.visualise_region_performance(df)
        elif user_choice == TOP_GAMING_CONSOLES_CHOICE:
            top_gaming_consoles.visualise_top_gaming_consoles(df)
        elif user_choice == TOP_GLOBAL_GAMES_CHOICE:
            top_global_games.visualise_top_global_games(df)
        elif user_choice == TOP_REGIONAL_GAMES_CHOICE:
            top_regional_games.visualise_top_regional_games(df)
        elif user_choice == GAMES_OLD_RELEASES_CHOICE:
            old_game_release.visualise_games_old_releases(df)
        elif user_choice == GAMING_GENRES_CHOICE:
            gaming_genre.visualise_gaming_genres(df)
        elif user_choice == PUBLISHER_IMPACT_CHOICE:
            publisher_impact_on_regions.visualise_publisher_impact_on_regions(df)
        elif user_choice == GLOBAL_AVERAGE_CHOICE:
            global_average.visualise_global_average(df)
        elif user_choice == EXIT_CHOICE:
            print("Exiting program...")
            exit()

# Naming convention: Use "visualise" at the start of every
# function name that performs data visualisation.





main_menu()