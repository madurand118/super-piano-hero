mySprite = sprites.create(assets.image("""
    truc
"""), SpriteKind.player)
controller.move_sprite(mySprite)
animation.run_image_animation(mySprite,
    [img("""
    . . . . . . . . b b b b . . . .
    . . . . b b b b 3 3 3 3 b . . .
    . c c b b 1 1 3 3 3 3 3 b b . .
    c c b b 1 1 3 3 3 3 3 1 1 b . .
    c b b b b b 3 3 3 3 3 1 1 b . .
    f b b b b b 3 3 3 3 3 3 3 c . .
    f b b b b b b 3 3 3 3 3 3 b c .
    f b b b b b b b b 3 3 3 b b b c
    . c b b b b b b b b b b b b b c
    . c c b b b b b b 1 1 b b b b f
    . f d c b b b b b 1 1 b b b b f
    . f d d c c b b b b b b b b b f
    . . c d d d c c b b b b b b f f
    . . . c d d d d c c c c f f f .
    . . . f c c c f b b b b . . . .
    . . . f d d d f f . . . . . . .
    """),img(""". . . . . . . . . . . . . . . . 
    . . . . . . . . b b b b . . . .
    . . . . b b b b 3 3 3 3 b . . .
    . c c b 1 1 1 3 3 3 3 1 b b . .
    c b b b 1 1 3 3 3 3 3 1 1 b . .
    c b b b b b 3 3 3 3 3 1 1 b . .
    f b b b b b b 3 3 3 3 3 3 c . .
    f b b b b b b 3 3 3 3 3 b b c .
    f b b b b b b b b 3 3 3 b b b c
    . c b b b b b b b 1 1 b b b b c
    . c c b b b b b b 1 1 b b b b f
    . f d c c b b b b 3 3 b b b b f
    . f d d d c c b b b b b b b c f
    . . c d d d d c c b b b b c f f
    . . . c d d d d c c c c f f f .
    . . . . c c c f b b . . . . . . """),img(""". . . . . . . . . . . . . . . . 
    . . . . . . . . b b b b . . . .
    . . . . b b b b 3 3 3 3 b . . .
    . c c b b 1 1 3 3 3 3 3 b b . .
    c c b b 1 1 3 3 3 3 3 1 1 b . .
    c b b b b b 3 3 3 3 3 1 1 b . .
    f b b b b b 3 3 3 3 3 3 3 c . .
    f b b b b b b 3 3 3 3 3 3 b c .
    f b b b b b b b b 3 3 3 b b b c
    . c b b b b b b b b b b b b b c
    . c c b b b b b b 1 1 b b b b f
    . f d c b b b b b 1 1 b b b b f
    . f d d c c b b b b b b b b b f
    . . c d d d c c b b b b b b f f
    . . f c d d d d c c c c f f f .
    . . f f c c c f b b b f . . . . """),img(""". . . . . . . . b b b b . . . . 
    . . . . b b b b 3 3 3 3 b . . .
    . c c c b 1 1 3 3 3 3 3 b b . .
    c c c b 1 1 1 3 3 3 3 3 1 b . .
    c c b b b b 3 3 3 3 3 1 1 b . .
    f b b b b b 3 3 3 3 3 1 1 c . .
    f b b b b b 3 3 3 3 3 3 3 c c .
    f b b b b b b b 3 3 3 3 3 b c c
    . c b b b b b b b b b b b b b c
    . c b b b b b b b 3 3 b b b b f
    . f c b b b b b b 1 1 b b b b f
    . f d c c b b b b 1 1 b b b b f
    . . c d d c c b b b b b b b f f
    . . f c d d d c c c c c f f f .
    . f f b c c c f c f b b f f . .
    . f d d d b f . . f b b b f . . """)],
    500,
    False)