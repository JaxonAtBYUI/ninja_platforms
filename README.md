# Overview

This is a proof of concept platformer game. 

Controls:
* A - Move Left
* D - Move Right
* W or SPACE - Jump

Abilities:
 - Wall clinging: The ability to slide down a wall slowly. This is done by touching a wall while in the air. This allows you to wall jump as well.
 - Wall jumping: While wall clinging you are able to throw yourself up and away from the wall. This is done by jumping while against a wall.
 - Double jumping: You are able to jump once while in the air. Simply press the jump key while in the air to double jump.

This is a simple platforming game written in python using the pygame library. I created this to explore object oriented programmig, as well as increase my knowledge of game physics and collisions. I focused heavily on encapsulation. I also focused on clarity. I broke the code out into many simple functions. I did this to make the code clear enough that minimal comments were necessary to explain what was happening when looking at a function. I also experimented with extreme modularity, allowing everything from solids, to new levels to be added easily. Levels are created by drawing an image of the level in an image editor and then having the code read the image to generate the level. In this way I sought to increase the speed at which you would be able to expand the game.

[Demo Video](https://youtu.be/xkPZQuC9az4)

# Development Environment

This was made in VScode. The images were created in MS Paint and Gimp. The files are hosted on Github.

The language used was Python, and the library used to create the game was pygame.

# Useful Websites

* [Pygame Documentation](https://www.pygame.org/docs/)

# Future Work

* Animations to be added to the player as well as any other objects that would necessitate animation.
* More tiles as there are only six in the game currently.
* Moveable boxes which would have an physics based interaction with the player as well as being destructable.
* Enemies and other obstacles as to make the game more challenging.
* A grappling ability to swing around and pull the player towards positions on the screen.