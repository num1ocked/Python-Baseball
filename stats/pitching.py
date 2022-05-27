import pandas as pd
import matplotlib.pyplot as plt

from data import games

plays = games[games['type'] == 'play']
plays[plays['event'].str.contains('K')]
