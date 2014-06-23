#!/usr/bin/python

# This version has a reference array and a buffer array
# Every cycle the buffer array is filed following the game rules and replaces the ref array at the end of the cycle
# Starts with a array full of zeros and goes through once to fill it based on rand % 2
# Border are in cycle mode example top neighboor of cell (0,0) is (0,height) , bottom border of (height, 0) is (0.0)
# stable represents the number of live neighbours for stable life
# repro represents the number of neighbours for reproduction
# dead is the char to display on dead cells
# live is the char to display on live cells
# try and keep these string the same size as to not fuck up the output
# Rules are :
# Live cell with < stable live neighbours dies
# Live cell with stable || repro live neighbours lives
# Live cell with > repro live neighbours dies
# Dead cell with = repro live neighbours comes to life
# Directions are in cardinal mode East West South North SE SW NE NW
# anything with y represents vertical position, anything with x represent horizontal position

import os
from random import randint
from time import sleep
import sys
#import traceback

turn = 0
stable = 2
repro = 3
dead = '-'
live = 'O'
width = 315
height = 74

ref = [[ 0 for x in xrange(width)] for x in xrange(height)]
buf = [[ 0 for x in xrange(width)] for x in xrange(height)]



def getEstatus(x, y) :
    rx = x + 1
    ry = y
    if rx > (width - 1) :
        rx -= width
    return ref[ry][rx]

def getWstatus(x, y) :
    rx = x - 1
    ry = y
    if rx < 0 :
        rx += width
    return ref[ry][rx]

def getSstatus(x, y) :
    rx = x
    ry = y + 1
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]

def getNstatus(x, y) :
    rx = x
    ry = y - 1
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getNEstatus(x, y) :
    rx = x + 1
    ry = y - 1

    if rx > (width - 1) :
        rx -= width
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getNWstatus(x, y) :
    rx = x - 1
    ry = y - 1
    if rx < 0 :
        rx += width
    if ry < 0 :
        ry += height
    return ref[ry][rx]

def getSEstatus(x, y) :
    rx = x + 1
    ry = y + 1
    if rx > (width - 1) :
        rx -= width
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]

def getSWstatus(x, y) :
    rx = x - 1
    ry = y + 1
    if rx < 0 :
        rx += width
    if ry > (height - 1) :
        ry -= height
    return ref[ry][rx]

def updateCellStatus(x, y) :
        nbLiveNeighbours = getEstatus(x, y) + getWstatus(x, y) + getNstatus(x, y) + getSstatus(x, y) + getNEstatus(x, y) + getNWstatus(x, y) + getSEstatus(x, y) + getSWstatus(x, y)

        if ref[y][x] == 1 :
            if nbLiveNeighbours < stable :
                buf[y][x] = 0
            elif nbLiveNeighbours == stable or nbLiveNeighbours == repro :
                buf[y][x] = 1
            elif nbLiveNeighbours > repro :
                buf[y][x] = 0
            else :
                buf[y][x] = 0
        if ref[y][x] == 0 :
            if nbLiveNeighbours == repro :
                buf[y][x] = 1
            else :
                buf[y][x] = 0

def cycle() :
    for y in range(height) :
        for x in range(width) :
            updateCellStatus(x, y)

def draw() :
    os.system('cls' if os.name == 'nt' else 'clear')
    print turn
    for y in ref :
        for x in y :
            sys.stdout.write(live if x == 1 else dead)
        print ''

def init() :
    for y in range(height - 1) :
        for x in range(width - 1) :
            ref[y][x] = randint(0, 1)

init()
draw()
sleep(0.1)

while True :
    turn += 1
    cycle()
    ref, buf = buf, ref
    draw()
    sleep(0.1)
