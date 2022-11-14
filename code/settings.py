from pygame.math import Vector2

#Screen Resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TILE_SIZE = 64  

#Overlay Positions

OVERLAY_POSITIONS = {
    'tool' : (40, SCREEN_HEIGHT - 15),
    'seed' : (70, SCREEN_WIDTH - 5)}

PLAYER_TOOL_OFFSET = {
    'left': Vector2(-50, 40),
    'right': Vector2(50, 40),
    'up': Vector2(0, -10),
    'down': Vector2(0, 40)
}


