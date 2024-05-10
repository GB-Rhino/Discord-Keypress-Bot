# Overview
This project was designed to emulate Twitch-Plays-Pokemon but with friends over discord, allowing them to control keypresses.

## How it works
This bot will essentially listen to any inputs sent in any text channel on the server (RECOMMENDED YOU KEEP IT TO ONE TEXT CHANNEL) using the prefix !cmd.
the game set up in the example is Elden Ring with default keybinds.

For convenience sake, I have added functionality so that only when you are focused on the specified window does it allow inputs, preventing people from messing with your computer.

## DISCLAIMER: THIS WILL NOT RUN ON ITS OWN
You will need to supply your own bot token and install Python, as well as the prerequisites that are imported - to get the token, create a bot using the Discord developer Portal and go from there.

## Amending for other games
I have added a JSON file which allows you to input new games into the list - ELDEN RING is the only game I have verified that works. In theory, this could support any game with mappable keyboard inputs, as long as you have the process name in question, and as long as the game allows multiple inputs from different devices - An example where this probably wouldn't work would be Xenia that only seems to read from one input device.

In theory, this can work for any game played on a keyboard and mouse.

## DISCLAIMER
I AM NOT SURE HOW THIS WOULD AFFECT ONLINE GAMES/ANTICHEAT. If you were to run this for a multiplayer game, I don't know whether using pydirectinput will be picked up as you cheating, as it can allow for some weird behaviour and interaction between inputs, as well as come across strange if your inputs are being read.

I have also tried to idiot proof it as much as possible to ensure that your computer is safe, but there is no thing such as entire safety. I haven't tested what happens in the event a command is done at the same time as the window being unfocused, so commands may be able to slip through, potentially in the even of rate limiting also





