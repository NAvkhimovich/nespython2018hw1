#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:01:20 2018

@author: nik_avkhimovich
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline

%cd ~/Desktop/NES_MAEE2020/Modul 1/Data Analysis in Python/Home Assignment/Data

season1718 = pd.read_csv('season1718.csv')

# Matches, where Manchester United won with 3 goals difference and both teams earned few yellow cards
season1718[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'HY', 'AY']][((season1718.HomeTeam == 'Man United')&(season1718.FTHG - season1718.FTAG > 2)|(season1718.AwayTeam == 'Man United')&(season1718.FTAG - season1718.FTHG > 2))&(season1718.HY + season1718.AY < 3)]

# Probability, that there would be a red card in a match with Mike Dean as a referee
q1 = season1718[(season1718.Referee == 'M Dean')&(season1718.HR + season1718.AR > 0)].HomeTeam.count()
q2 = season1718[(season1718.Referee == 'M Dean')].HomeTeam.count()
print('Probability, that there would be a red card in a match with Mike Dean as a referee = ', q1 / q2)

# Games, when bookmakers evaluated two teams as nearly equal (were unsure, who would win - odds for both teams are higher that 2,7)
season1718[['HomeTeam', 'AwayTeam', 'B365H', 'B365D', 'B365A']][(season1718.B365H>2.7)&(season1718.B365A>2.7)]

# Top 3 Home Teams by share of shots, which were on target, and by probability of a goal after a shot on target
GoalsShots = grouped[['FTHG','HS','HST']].sum()
ProbOnTarget = GoalsShots.HST / GoalsShots.HS
ProbGoal = GoalsShots.FTHG / GoalsShots.HST
print('Top 3 Home Teams by share of shots, which were on target')
print(ProbOnTarget.sort_values(ascending=False)[:3])
print('')
print('Top 3 Home Teams by probability of a goal after a shot on target')
print(ProbGoal.sort_values(ascending=False)[:3])

# Number of cases of possible arbitrage across 7 bookmakers
season1718['maxH'] = season1718[['B365H','BWH','IWH','LBH','PSH','WHH','VCH']].max(axis=1)
season1718['maxD'] = season1718[['B365D','BWD','IWD','LBD','PSD','WHD','VCD']].max(axis=1)
season1718['maxA'] = season1718[['B365A','BWA','IWA','LBA','PSA','WHA','VCA']].max(axis=1)
print('During the season there were', season1718[(1/season1718.maxH + 1/season1718.maxD + 1/season1718.maxA > 1)].HomeTeam.count(), 'cases of possible arbitrage out of', season1718.HomeTeam.count(), 'matches')
