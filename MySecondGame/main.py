from map import Map
from pynput import keyboard
import time
import os
from helicopter import Helicopter as Helico
from clouds import Clouds
import json

# 🌲 🌊 🚁🟩 🔥 🏥 💛 💵 ⬛ 🚰 🏆 ☁️ 🌩️ 🔲

TICK_SLEEP = 0.5
TREE_UPDATE = 50
FIRE_UPDATE = 20
CLOUDS_UPDATE = 30
MAP_W, MAP_H = 10, 5

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helico(MAP_W, MAP_H)

tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}

def proccessHelico_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)

    if c == 'f':
        data = {'helicopter': helico.exportData(),
                'clouds': clouds.exportData(),
                'field': field.exportData(),
                'tick': tick}
        with open('Level.json', 'w') as lvl:
            json.dump(data, lvl)


    if c == 'g':
        with open('Level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.importData(data['helicopter'])
            field.importData(data['field'])
            clouds.importData(data['clouds'])

listner = keyboard.Listener(
    on_press=None,
    on_release=proccessHelico_key)
listner.start()


while True:
    os.system('clear')

    field.proccessHelico(helico, clouds)
    helico.printStats()
    field.print_map(helico, clouds)
    print('Tick: ', tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fire()
    if(tick % CLOUDS_UPDATE == 0):
        clouds.upgeteClouds()


