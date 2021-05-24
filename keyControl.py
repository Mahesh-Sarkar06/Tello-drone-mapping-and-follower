import pygame
import time


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")
        time.sleep(0.5)
    if getKey("RIGHT"):
        print("Right key pressed")
        time.sleep(0.5)
    if getKey("UP"):
        print("Up key pressed")
        time.sleep(0.5)
    if getKey("DOWN"):
        print("Down key pressed")
        time.sleep(0.5)
    if getKey("a"):
        print("A key pressed")
        time.sleep(0.5)
    if getKey("d"):
        print("D key pressed")
        time.sleep(0.5)
    if getKey("w"):
        print("W key pressed")
        time.sleep(0.5)
    if getKey("s"):
        print("S key pressed")
        time.sleep(0.5)


if __name__ == '__main__':
    init()
    while True:
        main()
