import os
import random
import cherrypy

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        # This function is called when you register your Battlesnake on play.battlesnake.com
        # It controls your Battlesnake appearance and author permissions.
        # TIP: If you open your Battlesnake URL in browser you should see this data
        return {
            "apiversion": "1",
            "author": "first_snake",  # TODO: Your Battlesnake Username
            "color": "#123456",  # TODO: Personalize
            "head": "default",  # TODO: Personalize
            "tail": "default",  # TODO: Personalize
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        # This function is called everytime your snake is entered into a game.
        # cherrypy.request.json contains information about the game that's about to be played.
        data = cherrypy.request.json

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # This function is called on every turn of a game. It's how your snake decides where to move.
        # Valid moves are "up", "down", "left", or "right".
        # TODO: Use the information in cherrypy.request.json to decide your next move.
        data = cherrypy.request.json
        my_snake = data["you"]
        my_body = data["you"]["body"]
        possible_right = { "x":my_snake["head"]["x"]+1, "y":my_snake["head"]["y"] }
        possible_left = { "x":my_snake["head"]["x"]-1, "y":my_snake["head"]["y"] }
        possible_up = { "x":my_snake["head"]["x"], "y":my_snake["head"]["y"]+1}
        possible_down = { "x":my_snake["head"]["x"], "y":my_snake["head"]["y"]-1}
        if possible_right["x"] > 10:
            possible_right_valid = False
        else:
            possible_right_valid = True

        if possible_left["x"] < 0:
            possible_left_valid = False
        else:
            possible_left_valid = True

        if possible_up["y"] > 10:
            possible_up_valid = False
        else:
            possible_up_valid = True\

        if possible_down["y"] < 0:
            possible_down_valid = False
        else:
            possible_down_valid = True
        is_food_available = False
        counter=0
        while is_food_available == False:
            if data["board"]["food"][counter] not in my_body:
                closest_food = data["board"]["food"][counter]
                is_food_available = True
            counter+=1

    # This section makes sure I stay in bounds
        # If I'm at the bottom left corner and can move up, move up.
        # if my_snake["head"]["y"] == 0 and my_snake["head"]["x"] == 0\
        #     and possible_up not in my_body:
        #     move = "up"
        # # If I'm at the bottom left corner and can move right, move right.
        # elif my_snake["head"]["y"] == 0 and my_snake["head"]["x"] == 0\
        #     and possible_right not in my_body:
        #     move = "right"
        # # If I'm at the bottom right corner and can move up, move up.
        # elif my_snake["head"]["y"] == 0 and my_snake["head"]["x"] == 10\
        #     and possible_up not in my_body:
        #     move = "up"
        # # If I'm at the bottom right corner and can move left, move left.
        # elif my_snake["head"]["y"] == 0 and my_snake["head"]["x"] == 10\
        #     and possible_left not in my_body:
        #     move = "left"
        # # If I'm at the top right corner and can move left, move left.
        # elif my_snake["head"]["y"] == 10 and my_snake["head"]["x"] == 10\
        #     and possible_left not in my_body:
        #     move = "left"
        # # If I'm at the top right corner and can move down, move down.
        # elif my_snake["head"]["y"] == 10 and my_snake["head"]["x"] == 10\
        #     and possible_down not in my_body:
        #     move = "down"
        # # If I'm at the top left corner and can move down, move down.
        # elif my_snake["head"]["y"] == 10 and my_snake["head"]["x"] == 0\
        #     and possible_down not in my_body:
        #     move = "down"
        # # If I'm at the top left corner and can move right, move right.
        # elif my_snake["head"]["y"] == 10 and my_snake["head"]["x"] == 0\
        #     and possible_right not in my_body:
        #     move = "right"
        # elif possible_right in my_body and possible_left in my_body and possible_down in my_body\
        #     and possible_up_valid == True:
        #     move = "up"
        # elif possible_right in my_body and possible_up in my_body and possible_down in my_body\
        #     and possible_left_valid == True:
        #     move = "left"
        # elif possible_left in my_body and possible_up in my_body and possible_down in my_body\
        #     and possible_right_valid == True:
        #     move = "right"
        # elif possible_right in my_body and possible_left in my_body and possible_up in my_body\
        #     and possible_down_valid == True:
        #     move = "down"
        # # If I'm at the top or bottom row and can move right, go right.
        # elif my_snake["head"]["y"] == 0 or my_snake["head"]["y"] == 10\
        #     and possible_right not in my_body:
        #     move = "right"
        # # If I'm at the top or bottom row and can move left, go left.
        # elif my_snake["head"]["y"] == 0 or my_snake["head"]["y"] == 10\
        #     and possible_left not in my_body:
        #     move = "left"
        # # If I'm at the the left or right of map, go up or down
        # elif my_snake["head"]["x"] == 0 or my_snake["head"]["x"] == 10\
        #     and possible_up not in my_body:
        #     move = "up"
        # elif my_snake["head"]["x"] == 0 or my_snake["head"]["x"] == 10\
        #     and possible_down not in my_body:
        #     move = "down"
    # This section searches for food

        # If I'm to the left of the food and the square to my right is open, go right
        if my_snake["head"]["x"] < closest_food["x"]\
            and possible_right not in my_body\
            and possible_right_valid == True:
            move = "right"
        # If I'm to the right of the food and the square to my left is open, go left
        elif my_snake["head"]["x"] > closest_food["x"]\
            and possible_left not in my_body\
            and possible_left_valid == True:
            move = "left"
        elif my_snake["head"]["y"] < closest_food["y"]\
            and possible_up not in my_body\
            and possible_up_valid == True:
            move = "up"
        elif my_snake["head"]["y"] < closest_food["y"]\
            and possible_down not in my_body\
            and possible_down_valid == True:
            move = "down"
        elif possible_left not in my_body\
            and possible_left_valid == True:
            move = "left"
        elif possible_up not in my_body\
            and possible_up_valid == True:
            move = "up"
        elif possible_right not in my_body\
            and possible_right_valid == True:
            move = "right"
        elif possible_down not in my_body\
            and possible_down_valid == True:
            move = "down"
        else:
            move = "down"

        # if my_snake["head"]["x"] < data["board"]["food"][0]["x"]\
        #     and my_snake["body"][1]["x"] != my_snake["head"]["x"] +1\
        #     move = "right"
        # elif my_snake["head"]["x"] > data["board"]["food"][0]["x"] and my_snake["body"][1]["x"] != my_snake["head"]["x"] -1:
        #     move = "left"
        # elif my_snake["head"]["y"] < data["board"]["food"][0]["y"] and my_snake["body"][1]["y"] != my_snake["head"]["y"] +1:
        #     move = "up"
        # else:
        #     move = "down"


        # Below code is to spin in a circle
        # if my_snake["head"]["x"] > 0 and my_snake["body"][1]["x"] != my_snake["head"]["x"] -1:
        #   move = "left"
        # elif my_snake["head"]["y"] > 0:
        #   move = "down"
        # elif my_snake["head"]["x"] < 6 and my_snake["body"][1]["x"] != my_snake["head"]["x"] +1:
        #   move = "right"
        # else:
        #   move = "up"

        # Choose a random direction to move in
        #possible_moves = ["up", "down", "left", "right"]
        #move = random.choice(possible_moves)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        # This function is called when a game your snake was in ends.
        # It's purely for informational purposes, you don't have to make any decisions here.
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
