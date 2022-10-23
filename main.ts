input.onButtonPressed(Button.A, function () {
    ship.move(1)
    ship.ifOnEdgeBounce()
})
input.onButtonPressed(Button.B, function () {
    bullet = game.createSprite(ship.get(LedSpriteProperty.X), 3)
    bullet.turn(Direction.Left, 90)
    while (!(bullet.get(LedSpriteProperty.Y) == 0)) {
        bullet.move(1)
        if (bullet.isTouching(enemy)) {
            game.addScore(1)
            enemy.set(LedSpriteProperty.Blink, 1)
            basic.pause(100)
            enemy.set(LedSpriteProperty.Blink, 0)
        }
        basic.pause(100)
    }
    basic.pause(100)
    bullet.delete()
})
let enemybullet: game.LedSprite = null
let bullet: game.LedSprite = null
let enemy: game.LedSprite = null
let ship: game.LedSprite = null
ship = game.createSprite(2, 4)
enemy = game.createSprite(0, 0)
game.setScore(0)
game.setLife(5)
basic.forever(function () {
    basic.pause(200)
    enemy.move(1)
    basic.pause(100)
    enemy.move(randint(1, -1))
    enemy.ifOnEdgeBounce()
    if (randint(0, 4) == 0) {
        enemybullet = game.createSprite(enemy.get(LedSpriteProperty.X), 0)
        enemybullet.turn(Direction.Left, 270)
        while (!(enemybullet.get(LedSpriteProperty.Y) == 4)) {
            enemybullet.move(1)
            if (enemybullet.isTouching(ship)) {
                game.removeLife(1)
                basic.pause(1000)
            }
            basic.pause(100)
        }
        basic.pause(100)
        enemybullet.delete()
    }
})
