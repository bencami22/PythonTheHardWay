from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("SUbclass it and implement enter()")
        exit(0)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        #be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    quips=[
        "You died",
        "You're not very good at this are you?"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorrider(Scene):
    def enter(self):
        print(dedent("""
        Aliens have invaded the ship
        You're running down central corrider to the weapons Armoury
        when an alien jumps in front of you and about to pull out his weapon
        What do you do?
        """))
        action = input(">")

        if action == "shoot":
            print(dedent(
            """
            You miss and he shoots you.
            """
            ))

            return 'death'
        elif action == 'dodge':
            print(dedent(
            """
                Nice try, but the alien still gets you
            """
            ))
            return 'death'
        elif action == 'tell a joke':
            print(dedent("""
                You have got the alien laughing and you pass him
                into the weapon armoury room.
            """))
            return 'laser_weapon_armory'
        else:
            print(dedent("""
            DOES NOT COMPUTE
            """))
            return 'central_corrider'


class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You find a bomb with a keypad on it.
        If you get the code wrong 10 times, you die.
        The code is 3 digits long.
        """))
        code = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        #print(code)
        guess = None
        guesses = 0

        while guesses < 10:
            guess = input(">")
            if guess == code:
                print("Well done! You now proceed to the bridge")
                return 'the_bridge'
            else:
                print("BZZZT Wrong!")
                guesses = guesses + 1
        return 'death'


class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You have a bomb in your hand running across the bridge.
        5 aliens pop out of no where.
        They don't attack because you have the bomb.
        """))
        action = input(">")

        if action == "throw the bomb":
            print("The bomb blows on impact. You die")
            return 'death'
        elif action == "slowly place the bomb":
            print("You point your gun to the bomb threatening the aliens and run to the escape pod")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print("There are 5 pods, which one do you take")
        correct_pod = randint(0,5)
        guess = input(">")
        if correct_pod == int(guess):
            print("The pod starts and you get going")
            return 'finished'
        else:
            print("The pod is damaged and the aliens are behing you as you leave it. You die")
            return 'death'

class Finished(Scene):
    def enter(self):
        print("You won!")
        exit(0)


class Map(object):
    scenes={
        'central_corrider' : CentralCorrider(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corrider')
a_game = Engine(a_map)
a_game.play()
