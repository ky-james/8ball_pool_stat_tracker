# 8ball_pool_stat_tracker

## Description
The goal of this project was to create a GUI application which allows players to easily track 8 ball pool games and statistics as players play. To start recording a game, simply select the breaking and incoming players from drop down menus containing all the player names in the database. After a player finishes their turn, the GUI is used to input all relevant information of their completed turn. To record sinking a ball, a player will click the potted ball, and the pocket where it was potted. Once a player's turn ends, clicking the "End Turn" button will end the players turn and update the app with that turn. Once the 8 ball is sunk, the app's embedded logic will determine that the game is over and move to a game recap screen. Inspired by NHL games I used to play on xbox, a table of the completed game's statistics will be displayed.

## Origin Story & Motivation
My friends and I are BIG fans of pool. When your friend group has a pool table at your usual hangout spot, it's really hard not to be. At the end of summer 22' we had the idea of recording each shot we took, made, and missed, so we could then analyze the data to see who has the best shooting percentage, win percentage, and other interesting stats. The project was originally created in excel with a very basic spreadsheet. I quickly noticed that while effective, this method of data collection was very slow. I then had the idea to create a GUI application which would follow your games as you play, making data collection very easy.

## Design & Technical Description
This GUI contains multiple layered windows which guide the user through the app, creating an easy and intuitive experience. A flow chart of the app's windows can be found [here](https://lucid.app/lucidchart/c6d29fa4-9ebd-4090-a61a-362e1455ca3f/edit?viewport_loc=-125%2C-132%2C2219%2C1151%2C0_0&invitationId=inv_7f021f67-326a-43f9-9a70-114b37afd814#). The entirety of this project was written in python, with the help of the PyQt5 package. PyQt5 was the chosen library as it contains a wide array of GUI features, useful documentation, and ample resources available online.

## Future Work
The next feature which I would like to add is an area to view the recorded statistics. I’ve brainstormed an initial flowchart for these windows, which is visible in the hyperlink in the Design & Technical Description section. In this feature, I’d like the user to be able to see each individual player’s statistics, game’s statistics, and a leaderboard inspired by Xbox games showing the top and bottom 3 players for any selected stat.


