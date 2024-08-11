# Baduk Game
Go board game made in python and visualized using pygame, following japanese Go rules regarding Ko

## Rules of Go

Go isn't too hard of a game once you have played it, so for the rules I would recommmend:
1. Reading https://en.wikipedia.org/wiki/Go_(game)

or

2. Learning to play at https://online-go.com/ (I personally use this to play with friends)

## Description

This is a game of Go made with pygame. The game is played on the same board by two people, with alternating picks for moves. The engine is quite simple but follows all the rules of the game, including blocking a ko fight from occuring and blocking suicide.

##:w Recognition

A lot of the base logic, capture, floodfill and the structure of the board, came from this series by Chess Programming: [link](https://www.youtube.com/watch?v=dHlan0bgr5U&list=PLmN0neTso3JzVlIQC3fwnP1qgIKp1x97X)
The logic use to determine if a move is legal or not was thought up and written by me.

## Requirements
Pygame and Numpy are the only two requirements:
~~~
pip install pygame
pip istall numpy
~~~

## (Probable) Future Development

- Ability to change the size
- Turn Indicator
- Score Estimation
- (Simple) Robot
