import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games[games['type'] == 'play']
strike_outs = plays[plays['event'].str.contains('K')]
strike_outs = strike_outs.groupby(['year', 'game_id']).size()
strike_outs = reset_index(name='strike_outs')
