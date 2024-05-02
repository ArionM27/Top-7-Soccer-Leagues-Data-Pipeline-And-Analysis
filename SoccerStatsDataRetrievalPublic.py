#Soccer Stats Pipeline, Scrapes from Fotmob API of Europes Top 7 Leagues
#Made by Arkadiuz A. Mercado
#Will scrape data, updating after every gameweek, to then translate into a SQL Database
#Planned to be worked on and updated with new features overtime

import time
import numpy as pd
import pandas as pd
import requests
import time
from sqlalchemy import create_engine

#Connecting to SQL (PostgreSQL) Database
engine = create_engine("   Add In Your Own Database Here       ")  #Hidden for Security Purposes


#Creating a List for All Players
current_leagues = [{'Name': 'Premier League', 'Country': 'England', 'NameLink': 'premier-league', 'id': '47'}, 
                   {'Name': 'La Liga', 'Country': 'Spain', 'NameLink': 'laliga', 'id': '87'}, 
                   {'Name': 'Serie A', 'Country': 'Italy', 'NameLink': 'serie', 'id': '55'}, 
                   {'Name': 'Bundesliga', 'Country': 'Germany', 'NameLink': 'bundesliga', 'id': '54'}, 
                   {'Name': 'Ligue 1', 'Country': 'France', 'NameLink': 'ligue-1', 'id': '53'}, 
                   {'Name': 'Eredivisie', 'Country': 'Netherlands', 'NameLink': 'eredivisie', 'id': '57'}, 
                   {'Name': 'Liga Portugal', 'Country': 'Portugal', 'NameLink': 'liga-portugal', 'id': '61'}]

player_stats = []

#Calling all function that will be used

    #Retrieving all players in a team and their info for future sorting, filtering, and to connect them to respective stats
def eachTeam(team):
    teamName = team['name']
    teamID = team['id']
    teamAPI = "https://www.fotmob.com/api/" + 'teams?id=' + str(teamID)
    response = requests.get(teamAPI)
    squad = response.json()['squad']

    #Obtaining the player info using the teams API
    for player in squad:
        if(player['title'] != 'coach'):
            for info in player['members']:
                player_info = {
                    'Name': info['name'],
                    'League': eachLeague['Name'],
                    'Team': teamName,
                    'Nationality': info['cname'],
                    'Position': info['role']['fallback']
                }
                player_stats.append(player_info)

    #Retrieving all player stats in a specific league and matches them to its respective player
def eachPlayerStat(stat):
    statLink = stat['fetchAllUrl']
    statName = stat['header']
    specificStat = requests.get(statLink)
    eachPlayerSpecificStat = specificStat.json()['TopLists'][0]['StatList']

    if(statName == "Top scorer"):
        statName = "Goals"
        
    #For Loop for Specific Stat
    for player in eachPlayerSpecificStat:
        for playerFurther in player_stats:
                if(playerFurther['Name'] == player['ParticipantName']):
                        playerFurther[statName] = player['StatValue']
                        break
            
try:
    #Retrieving for each league of the top 7 UEFA ranked
    for eachLeague in current_leagues:
      #Retrieving teams using API
        leagueAPI = "https://www.fotmob.com/api/leagues?id=" + eachLeague['id']
        response = requests.get(leagueAPI)
        extractTeams = response.json()['table'][0]['data']['table']['all']
        #Using eachTeam function
        for team in extractTeams:
            eachTeam(team)

        response = requests.get(leagueAPI)
        extractStats = response.json()['stats']['players']

        #Using eachPlayerStat functiion
        for stat in extractStats:
            eachPlayerStat(stat)
        
    
except Exception as e:
      print("Error in Webscraping the Data! Check Response Status Code")
      response = requests.get('https://www.fotmob.com/leagues')
      response.status_code()

df = pd.DataFrame(player_stats)
#Using Pandas to clean DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame(player_stats, columns=['Name', 'League', 'Team','Nationality', 'Position', 'Goals', 'Assists', 'Goals + Assists', 'Goals per 90', 'Expected goals (xG)', 
                                         'Expected goals (xG) per 90', 'Expected goals on target (xGOT)', 'Shots on target per 90', 'Shots per 90',
                                         'Accurate passes per 90', 'Big chances created', 'Chances created', 'Accurate long balls per 90', 'Expected assist (xA)',
                                         'Expected assist (xA) per 90', 'xG + xA per 90', 'Big chances missed','Penalties won', 'Successful tackles per 90',
                                         'Interceptions per 90', 'Clearances per 90', 'Blocks per 90', 'Possession won final 3rd per 90', 'Penalties conceded', 
                                         'Clean sheets', 'Save percentage', 'Saves per 90', 'Goals prevented', 'Goals conceded per 90', 'Fouls committed per 90',
                                         'Yellow cards', 'Red cards']).fillna(0)

df = df.astype({'Goals': int, 'Assists': int, 'Goals + Assists': int, 'Big chances created': int, 'Chances created': int, 'Big chances missed': int, 'Penalties won': int,
                'Penalties conceded': int, 'Clean sheets': int, 'Yellow cards': int, 'Red cards': int})

#Inputting the Dataframe into the Database
try:
    df.to_sql('player_stats', con=engine, if_exists='replace', index_label = 'id')
except:
    print("Error, unable to add table to Database")

#Ending engine
engine.dispose()

print("Updated")