from django.shortcuts import render
from django.conf import settings
from game.data_mgmt import Data_mgmt
from random import randint

def title_screen(request):
    context = {"controls": {"a": {"action": "worldmap", "value": "default_settings"}, "b": {"action": "options/load_game", "value": "load"} } }
    dat = Data_mgmt()
    dat.load_default_settings()
    return render(request, "game/title_screen.html", context)

def worldmap(request):
    data_mgmt = Data_mgmt()
    data = data_mgmt.dump()
    chance = randint(0,3)
    board_size = { "width": range(settings.BOARD_SIZE["width"]), "height": range(settings.BOARD_SIZE["height"]) }
    if request.method == 'POST' and request._get_post()['clicked']:
        val = request._get_post()['val']
        if chance == 1:
            data["nbr_balls"] += 1
        if val == "left":
            data['position']['x'] = data['position']['x'] - 1
        if val == "up":
            data['position']['y'] = data['position']['y'] - 1
        if val == "right":
            data['position']['x'] = data['position']['x'] + 1
        if val == "down":
            data['position']['y'] = data['position']['y'] + 1
        if val == "default_settings":
            data_mgmt.load_default_settings()

        data_mgmt.load(data["position"], data["nbr_balls"], data["Moviedex"])
    def attack_link():
        if chance == 2:
            return "battle/tt0111161"
        else:
            return ""
    position = data["position"]
    if position["x"] != 0:
        left = {"action": "worldmap", "value": "left"}
    else:
        left = {"action": "", "value": ""}
    if position["y"] != 0:
        up = {"action": "worldmap", "value": "up"}
    else:
        up = {"action": "", "value": ""}
    if position["x"] != int(settings.BOARD_SIZE["height"]) - 1:
        right = {"action": "worldmap", "value": "right"}
    else:
        right = {"action": "", "value": ""}
    if position["y"] != int(settings.BOARD_SIZE["height"]) - 1:
        down = {"action": "worldmap", "value": "down"}
    else:
        down = {"action": "", "value": ""}
    controls = {
            "left": left,
            "up": up,
            "right": right,
            "down": down,
            "a": {"action": attack_link(), "value": attack_link()},
            "start": {"action": "/options", "value": "options"},
            "select": {"action": "/moviedex", "value": "moviedex"},
            }
    context = { "board_size": board_size, "controls": controls, "position": position }
    return render(request, "game/worldmap.html", context)

def battle(request):
    context = {}
    return render(request, "game/battle.html", context)

def battle_moviemon(request, moviemon_id):
    dat = Data_mgmt()
    dump = dat.dump()
    if request.method == 'POST' and request._get_post()['clicked']:
        val = request._get_post()['val']
        if val == "throw":
            dump['nbr_balls'] = dump['nbr_balls'] - 1
            dat.load(dump["position"], dump["nbr_balls"], dump["Moviedex"])
    mov = {}
    balls = dump["nbr_balls"]
    sgt = dat.get_strength()
    for item in dump['Movies']:
        if item['imdbID'] == moviemon_id:
            mov = item
    taux = 50 - (int(mov['imdbRating'][0:1]) * 10) + (sgt * 5)
    taux = 1 <= taux <= 90
    taux = 60
    if int(balls) > 0:
        launch = {"action": "/battle/"+moviemon_id, "value":"throw"}
    else:
        launch = {"action": "", "value": ""}
    controls = {
            "left": {"action": "", "value": ""},
            "up": {"action": "", "value": ""},
            "right": {"action": "", "value": ""},
            "down": {"action": "", "value": ""},
            "a": launch,
            "b": {"action": "/worldmap", "value": "worldmap"},
            "start": {"action": "", "value": ""},
            "select": {"action": "/moviedex", "value": "moviedex"},
            }
    context = {"moviemon": mov, "nbr_balls" : balls, "strength" : sgt, "taux" : taux, "controls": controls}
    return render(request, "game/battle_moviemon.html", context)

def moviedex(request):
    datamg = Data_mgmt()
    # datamg.load_default_settings()
    data = datamg.dump()
    movies = data['Movies']
    print (type(movies))
    controls = {
            "left": {"action": "moviedex", "value": "prev"},
            "right": {"action": "moviedex", "value": "next"},
            "a": {"action": "moviedex_moviemon", "value": "detail"},
            "select": {"action": "worldmap", "value": "back"},
            }
    context = {"movies":movies, "controls":controls}
    return render(request, "game/moviedex.html", context)

def moviedex_moviemon(request, moviemon_id):
    datamg = Data_mgmt()
    data = datamg.dump()
    movies = data['Movies']
    for elem in movies:
        if elem['imdbID'] == moviemon_id:
            movie = elem
    controls = {
            "b": {"action": "/moviedex", "value": "back"},
            }
    context = {"movie": movie, "controls":controls}
    return render(request, "game/moviedex_moviemon.html", context)

def options(request):
    context = {}
    return render(request, "game/options.html", context)

def options_save_game(request):
    context = {}
    return render(request, "game/options_save_game.html", context)

def options_load_game(request):
    context = {}
    return render(request, "game/options_load_game.html", context)

