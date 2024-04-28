import pygame
import math
from queue import PriorityQueue

WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Algoritmo A Estrella")

ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 255, 0)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MORADO = (128, 0, 128)
NARANJA = (255, 165, 0)
GRIS = (128, 128, 128)
TURQUESA = (64, 254, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLANCO
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == ROJO

    def is_open(self):
        return self.color == VERDE

    def is_barrier(self):
        return self.color == NEGRO

    def is_start(self):
        return self.color == NARANJA
    
    def make_open(self):
        self.color = VERDE  
    
    def make_barrier(self):
        self.color = NEGRO 
    
    def make_end(self):
        self.color = TURQUESA  

    def make_path(self):
        self.color = MORADO  
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        
    def update_neighbors(self, grid):
        self.update_neighbors = []  

def draw(win, grid, rows, width):
    win.fill(BLANCO)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRIS, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRIS, (j * gap, 0), (j * gap, width))

def main():
    rows = 50
    grid = [[Spot(row, col, WIDTH // rows, rows) for col in range(rows)] for row in range(rows)]

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(WIN, grid, rows, WIDTH)

    pygame.quit()

if __name__ == "__main__":
    main()

