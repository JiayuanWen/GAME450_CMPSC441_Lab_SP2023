import sys
import pygame
import random
import time
from tempfile import TemporaryFile
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from landscape import get_landscape, get_combat_bg
from pygame_ai_player import PyGameAIPlayer

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from lab3.travel_cost import get_route_cost, route_to_coordinates, generate_terrain
from speech_function.speech import speech

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])

def displayRouteCosts(routes, costs):
    for route in routes:
        text_surface = game_font.render(str(costs.get(route)), True, (0, 0, 0))
        route_coord = ((route[0][0]+route[1][0])/2, (route[0][1]+route[1][1])/2)
        screen.blit(text_surface, route_coord)


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
        costs,
        player_battlestatus,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes
        self.costs = costs
        self.player_battlestatus = player_battlestatus


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = random.randint(0,9)
    sprite_path = "assets/lego.png"
    sprite_speed = 1

    #Ensure player doesnt spawn on destination
    while end_city == start_city:
        end_city = random.randint(0,9)

    screen = setup_window(width, height, "Oillill's Advanture")

    landscape_surface = get_landscape_surface(size)
    combat_surface = get_combat_surface(size)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    cities = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(cities)

    random.shuffle(routes)
    routes = routes[:10]

    route_coordinates = route_to_coordinates(cities, cities, routes)

    game_map = generate_terrain(size)

    costs = {}
    for route, route_coordinate in zip(routes, route_coordinates):
        route_cost = get_route_cost(route_coordinate, game_map)
        print(f'Cost between {route[0]} and {route[1]}: {route_cost}')
        costs[route_coordinate] = route_cost

    player_sprite = Sprite(sprite_path, cities[start_city])

    player = PyGameHumanPlayer("Oillill")

    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""
    #player = PyGameAIPlayer("Oillill")

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=cities,
        routes=routes,
        costs=costs,
        player_battlestatus="Unknown",
    )

    goal_dest = str(f'Goal destination: {city_names[end_city]}')
    print(goal_dest)
    speech(goal_dest)
    while True:
        player_battlestatus="Unknown"
        action = player.selectAction(state)

        # Check if route to player's desired city exist
        target_route = (cities[state.current_city], cities[int(chr(action))])
        target_route_pass2 = (cities[int(chr(action))], cities[state.current_city])

        traveling_ind = "Transcript not avaliable"
        arrival_ind = "Transcript not avaliable"
        if 0 <= int(chr(action)) <= 9:
            if (target_route) in routes:
                if int(chr(action)) != state.current_city and not state.travelling:
                    start = cities[state.current_city]
                    state.destination_city = int(chr(action))
                    destination = cities[state.destination_city]
                    player_sprite.set_location(cities[state.current_city])
                    state.travelling = True
                    traveling_ind = str(f"Travelling from {city_names[state.current_city]} to {city_names[state.destination_city]}")
                    print(traveling_ind)
                    #time.sleep(1)
                    #speech(traveling_ind)
            elif (target_route_pass2) in routes:
                if int(chr(action)) != state.current_city and not state.travelling:
                    start = cities[state.current_city]
                    state.destination_city = int(chr(action))
                    destination = cities[state.destination_city]
                    player_sprite.set_location(cities[state.current_city])
                    state.travelling = True
                    traveling_ind = str(f"Travelling from {city_names[state.current_city]} to {city_names[state.destination_city]}")
                    print(traveling_ind)
                    #time.sleep(1)
                    #speech(traveling_ind)


        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in cities:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayRouteCosts(routes, costs)
        displayCityNames(cities, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                cost = costs.get(route)
                player.money -= cost

                arrival_ind = str(f'Arrived at {city_names[state.destination_city]}. {player.name} currently have {int(player.money)} Rubys left')
                print(arrival_ind)
                  

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            speech(str(f'{player.name} enountered an enemy. Round begin!'))
            run_pygame_combat(combat_surface, screen, player_sprite, state)
            state.encounter_event = False
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.flip()

        if state.player_battlestatus == "Lost":
            break
        
        if state.player_battlestatus == "Won":
            player.money += 150

        if not traveling_ind == "Transcript not avaliable":
            speech(traveling_ind)

        if not arrival_ind == "Transcript not avaliable":
            speech(arrival_ind)

        if player.money < 1:
            print("Ran out of Rubys! Game Over!")
            speech(f'{player.name} have ran out of Rubys. Cannot travel further.') 
            
            break

        if state.current_city == end_city:
            print('Destination reached!')
            print('*** Congratulations! ***')
            speech(f'{player.name} have reached destination! Congratulations!')
            break

        

        


