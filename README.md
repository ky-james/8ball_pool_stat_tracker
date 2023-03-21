# 8ball_pool_stat_tracker

## Description
The 8-Ball Pool Stat Tracker is an application consisting of a graphical user interface designed to simplify the process of recording and analyzing data during a game of pool. With easy-to-use features, such as player selection, shot outcome recording, and automatic game-ending detection, players can focus on playing their game while effortlessly keeping track of their progress. By providing detailed summaries of each player's game, the application enables players to identify their strengths and weaknesses, ultimately leading to improved gameplay. Whether you're a casual player or a seasoned pro, the Pool Tracker application is a powerful tool for enhancing your game.

## Origin Story & Motivation
Pool has always been a favorite pastime among my group of friends, and we love nothing more than spending our evenings playing a few rounds. As summer 2022 drew to a close, we decided to take our game to the next level by recording each shot we took, missed, and made, in order to analyze the data and see who had the best win percentage and shooting accuracy. As a computer science student, I knew there had to be a better way to track our games than using a basic Excel spreadsheet. So, I set out to create a graphical user interface that would streamline the process, allowing us to effortlessly track our games and gather valuable insights about our gameplay. And so, the 8-Ball Pool Stat Tracker was born.

## Design & Technical Description
The 8-ball stat tracker is a Python-based application that utilizes PyQt5 to create a user-friendly graphical user interface. The interface is made up of several windows, each designed to guide the user through the process of creating and recording stats for a new game, which can be found [here](https://lucid.app/lucidchart/c6d29fa4-9ebd-4090-a61a-362e1455ca3f/edit?viewport_loc=-125%2C-132%2C2219%2C1151%2C0_0&invitationId=inv_7f021f67-326a-43f9-9a70-114b37afd814#). The application stores CSV files in the [stat_sheets folder](./stat_sheets/), and these files are updated after every game to ensure that the latest data is always available. Thanks to its simple yet intuitive design and advanced functionality, the 8-ball stat tracker is a powerful tool for any pool player looking to track and analyze their gameplay data.

## Future Work
The next feature which I would like to add is an area to view the recorded statistics. I’ve brainstormed an initial flowchart for these windows, which is visible in the hyperlink in the Design & Technical Description section. In this feature, I’d like the user to be able to see each individual player’s statistics, game’s statistics, and a leaderboard inspired by Xbox games showing the top and bottom 3 players for any selected stat.


