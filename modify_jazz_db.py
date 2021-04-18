# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 19:43:12 2021

@author: Alice
"""

import pandas as pd
import sqlite3

'''
The purpose of this code is to modify the Weimar Jazz Database
(https://jazzomat.hfm-weimar.de/download/downloads/wjazzd.db)
to include the average Metrical Event Density (notes per bar) - this is going 
in the solo_info table. This number isn't quite exact, because of measures that
are entirely rests, and this fits our use case well.
'''
            
con = sqlite3.connect("wjazzd.db")

# Load the melody data into a DataFrame
melody_df = pd.read_sql_query("SELECT * from melody", con)
# calculate number of events in bar
events_per_melody = melody_df.groupby(['melid', 'bar'], dropna=False)\
                             .count()['eventid']
# calculate average number of events per bar in melody
avg_events_per_bar = events_per_melody.groupby(['melid']).mean()

# modify solo info df - add new column
solo_info_df = pd.read_sql_query("SELECT * from solo_info", con)
solo_info_df['avg_events_per_bar'] = avg_events_per_bar.reset_index()['eventid']

# write to new table
solo_info_df.to_sql('solo_info2', con)

con.close()

'''
For the ESAC Folksong database, which is easier:
'''
con = sqlite3.connect("esac.db")

# Load the melody data into a DataFrame
melody_df = pd.read_sql_query("SELECT * from melody", con)
# calculate number of events in bar
events_per_melody = melody_df.groupby(['melid', 'bar'], dropna=False)\
                             .count()['eventid']
# calculate average number of events per bar in melody
avg_events_per_bar = events_per_melody.groupby(['melid']).mean()

# modify solo info df - add new column
solo_info_df = pd.read_sql_query("SELECT * from esac_info", con)
solo_info_df['avg_events_per_bar'] = avg_events_per_bar.reset_index()['eventid']

# write to new table
solo_info_df.to_sql('esac_info2', con)

con.close()