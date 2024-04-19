import pandas as pd
import region_performance

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
    TOP_REGIONAL_GAMES_CHOICE = 2
    GAMES_OLD_RELEASES_CHOICE = 3
    GAMING_GENRES_CHOICE = 4
    PUBLISHER_IMPACT_CHOICE = 5
    GLOBAL_AVERAGE_CHOICE = 6

    CHOICE_MINIMUM = 0
    CHOICE_MAXIMUM = 8
    choices = tuple(range(CHOICE_MINIMUM, CHOICE_MAXIMUM))
    print(choices)

    while (1):
        print("1. Visualise region performance")
        print("2. Visualise top gaming consoles")
        print("3. Visualise top global games")
        print("4. Visualise top regional games")
        print("5. Visualise top old releases")
        print("6. Visualise top gaming genres")
        print("7. Visualise publisher impact on regions")
        print("8. Visualise global averages")
        print()
        user_choice = input("Which choice do you want to pick? ")
        try:
            user_choice = int(user_choice) - 1
        except:
            print("User choice needs to be a valid integer!")
        else:
            if user_choice not in choices:
                print("Invalid choice! Please pick from the selection...")
            else:
                break
    
    if user_choice == REGION_PERFORMANCE_CHOICE:
        region_performance.visualise_region_performance(df)
    elif user_choice == TOP_GAMING_CONSOLES_CHOICE:
        visualise_top_gaming_consoles()
    elif user_choice == TOP_GLOBAL_GAMES_CHOICE:
        visualise_top_global_games()
    elif user_choice == TOP_REGIONAL_GAMES_CHOICE:
        visualise_top_regional_games()
    elif user_choice == GAMES_OLD_RELEASES_CHOICE:
        visualise_games_old_releases()
    elif user_choice == GAMING_GENRES_CHOICE:
        visualise_gaming_genres()
    elif user_choice == PUBLISHER_IMPACT_CHOICE:
        visualise_publisher_impact_on_regions()
    elif user_choice == GLOBAL_AVERAGE_CHOICE:
        visualise_global_average()

# Naming convention: Use "visualise" at the start of every
# function name that performs data visualisation.
def visualise_top_gaming_consoles():
    pass

def visualise_top_global_games():
    pass

def visualise_top_regional_games():
    pass

def visualise_games_old_releases():
    pass

def visualise_gaming_genres():
    pass

def visualise_publisher_impact_on_regions():
    pass

def visualise_global_average():
    pass

main_menu()