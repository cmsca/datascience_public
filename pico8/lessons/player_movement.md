# Player Movement

## Desired outcomes from this lesson

The purpose of ths lesson is to ensure each participant has a basic understanding of how to draw and move a player. 

## Drawing Sprite 1

(This will be our player)

## Start with the game loop structure

```lua
-- player movement
-- by ben

function _init()
    -- add initial variables here
end

function _update()
    -- add update logic here
end

function _draw()
    -- add drawing logic here
end
```

## Add our player variables

Note: this is a table!

```lua
function _init()

    player={
        sp=1,
        x=59,
        y=59,
        w=8,
        h=8,
        flp=false,
        dx=1,
        dy=1
    }

end
```

## Add our gravity variables

```lua
function _init()

    player={
        sp=1,
        x=59,
        y=59,
        w=8,
        h=8,
        flp=false,
        acc=1
    }

    gravity=0.3

end
```

## Draw our player

```lua
function _draw()

    cls()

    map(0,0)
    
    spr(player.sp,player.x,player.y,1,1,player.flp)

end
```

## Make a player update function

```lua
function player_update()

    -- physics
    player.y+=gravity

    -- move left
    if btn(0) then
        player.x-=player.acc
        player.flp=true
    end

    -- move right
    if btn(1) then
        player.x+=player.acc
        player.flp=false
    end
    
    --jump
    if btn(2) then
        player.y-=player.acc
    end

    --limit player to map

end
```

## Update with player update function

```lua
function _update()

    player_update()

end
```

## Update player by keeping them on screen

```lua
function keep_plr_on_screen()

    -- stop at bottom of screen
    if player.y >= 111 then
        player.y = 111
    end

    -- stop at top of screen
    if player.y <= 0 then
        player.y = 0
    end

    -- reset on right of screen
    if player.x > 127 then
        player.x = 0
    end

    -- reset on left of screen
    if player.x <= -8 then
        player.x = 127
    end

end
```

## Update with player on screen function

```lua
function _update()

    player_update()

    keep_plr_on_screen()

end
```

## Draw sprite 16: floor

(This will be the bottom of the screen)

## Draw sprite 17: bush

(This is a 2x2 sprite)

## Draw sprite 19: cloud

(This is a 2x2 sprite)

## Update background color

```lua
function _draw()

    cls(12)

    map(0,0)
    
    spr(player.sp,player.x,player.y,1,1,player.flp)

end
```