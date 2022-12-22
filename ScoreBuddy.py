import ursina
from ursina import *
import nba_api
from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.endpoints import boxscore
from datetime import datetime,timezone
from dateutil import parser
import random
from nba_api.stats.static import players

f = "{gameId}"

id_list = []

gameon = False

scoreapp = Ursina(vynsce=True)
scorebuddy_text = Text(text="Score Buddy",color = color.gold,x=-0.3,y=0.44,scale=(3,3))
board = scoreboard.ScoreBoard()
print("ScoreBoardDate: " + board.score_board_date)
games = board.games.get_dict()
print(games)
for game in games:
    id_data = game.get('gameId')
    id_list.append(id_data)
random_game = random.choice(id_list)
box = boxscore.BoxScore(f'{random_game}')
boxgame = box.game.get_dict()
box_home = box.home_team.get_dict()
box_away = box.away_team.get_dict()
home_code = box_home.get('teamTricode')
away_code = box_away.get('teamTricode')
home_score = box_home.get('score')
away_score = box_away.get('score')
box_period = boxgame.get('period')
line = "{period}:{clock}  {player_id} ({action_type})"




def update():
    if boxgame.get('gameStatusText') != 'final':
        hometext = Text(text=f"{home_code}",scale=(5,5),color = color.gold,x=-0.6,y=0.2)
        awaytext = Text(text=f"{away_code}",scale=(5,5),color = color.gold,x=0.2,y=0.2)
        hscoretext = Text(text=f"{home_score}",scale=(5,5),color = color.gold,x=-0.5,y=0.05)
        ascoretext = Text(text=f"{away_score}",scale=(5,5),color = color.gold,x=0.3,y=0.05)
        periodtext1 = Text(text="Period",scale=(3,3),color = color.gold,x=-0.2,y=0.2)
        periodtext = Text(text=f"{box_period}",scale=(3,3),color = color.gold,x=-0.015,y=0.04)
    else:
        print("No game occuring right now")

scoreapp.run()


