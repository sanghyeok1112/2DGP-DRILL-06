from pico2d import *
import random

# Game object class here

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.frame = random.randint(100, 700)
        self.image = load_image('run_animation.png')

    def update(self):
        self.x += 5
        if self.x > 800:
            self.x = 0
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90)

class Grass:
    def __init__(self):
        self.x = 400
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, 30)

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width // 2, frame_height // 2)


class Ball:
    pass






    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    running = True
    global world
    world = []
    grass = Grass()
    world.append(grass)
    global team
    team = [Boy() for _ in range(11)]
    world += team
    zombie = Zombie()
    world.append(zombie)

def update_world():
    for game_object in world:
        game_object.update()

def render_world():
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

reset_world()
while running:
    handle_events() # 사용자 입력을 받는다
    update_world() # 객체의 상호작용을 계산
    render_world() # 객체의 모습을 그린다
    delay(0.05)

close_canvas()
