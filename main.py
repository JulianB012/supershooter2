def on_button_pressed_a():
    ship.move(1)
    ship.if_on_edge_bounce()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bullet
    bullet = game.create_sprite(ship.get(LedSpriteProperty.X), 3)
    bullet.turn(Direction.LEFT, 90)
    while not (bullet.get(LedSpriteProperty.Y) == 0):
        bullet.move(1)
        if bullet.is_touching(enemy):
            game.add_score(1)
            enemy.set(LedSpriteProperty.BLINK, 1)
            basic.pause(100)
            enemy.set(LedSpriteProperty.BLINK, 0)
        basic.pause(100)
    basic.pause(100)
    bullet.delete()
input.on_button_pressed(Button.B, on_button_pressed_b)

enemybullet: game.LedSprite = None
bullet: game.LedSprite = None
enemy: game.LedSprite = None
ship: game.LedSprite = None
ship = game.create_sprite(2, 4)
enemy = game.create_sprite(0, 0)
game.set_score(0)
game.set_life(5)

def on_forever():
    global enemybullet
    basic.pause(200)
    enemy.move(1)
    basic.pause(100)
    enemy.move(randint(1, -1))
    enemy.if_on_edge_bounce()
    if randint(0, 4) == 0:
        enemybullet = game.create_sprite(enemy.get(LedSpriteProperty.X), 0)
        enemybullet.turn(Direction.LEFT, 270)
        while not (enemybullet.get(LedSpriteProperty.Y) == 4):
            enemybullet.move(1)
            if enemybullet.is_touching(ship):
                game.remove_life(1)
                basic.pause(1000)
            basic.pause(100)
        basic.pause(100)
        enemybullet.delete()
basic.forever(on_forever)
