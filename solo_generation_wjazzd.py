# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:38:57 2021

@author: Alice
"""

import pandas as pd
import sqlite3
from music21 import *
from music21.converter.subConverters import ConverterMidi, ConverterMusicXML
import random

# use phrases to determine length

DIFFICULTY = 5.5
print(DIFFICULTY)

def get_solo_melody(difficulty, jazz=True):
    if jazz:
        con = sqlite3.connect("wjazzd.db")
        solo_info = "solo_info2"
    else:
        con = sqlite3.connect("esac.db")
        solo_info = "esac_info2"
    
    # Load the solo data into a DataFrame
    solo_info_df = pd.read_sql_query(f"SELECT * from {solo_info}", con)
    # Get random solo with appropriate difficulty
    solo = solo_info_df[abs(solo_info_df['avg_events_per_bar'] - DIFFICULTY) < 0.5].sample(1)
    #solo = solo_info_df.loc[315, :] #marseillaise, esac
    solo_num = int(solo['melid'])
    
    # Get phrase data
    phrase_df = pd.read_sql_query(f"SELECT * from sections "\
                                  f"WHERE melid = {solo_num} AND type = 'PHRASE'", con)
    # find a natural phrase end closest to desired end
    result_index = phrase_df['end'].sub(20).abs().idxmin()
    notes_end_index = phrase_df.loc[result_index, 'end']
    
    # Load corresponding melody into a Dataframe
    melody_df = pd.read_sql_query(f"SELECT * from melody WHERE melid = {solo_num}", con)
    melody_df = melody_df[0:notes_end_index+1]
    period = melody_df.loc[0, 'period']
    
    bars = int(melody_df['bar'].tail(1))
    onset = float(melody_df['onset'].head(1))
    
    midi = pd.read_sql_query(f"SELECT * from transcription_info WHERE melid = {solo_num}", con)
    midi_file = midi.loc[0, 'filename_sv'].replace('.sv', '.mid')
    midi_url = f"https://jazzomat.hfm-weimar.de/dbformat/synopsis/midi/{midi_file}"
    return midi_url, bars, onset, period


#melody_df = get_solo_melody(difficulty=4)

midi_url, bars, onset, timesig = get_solo_melody(DIFFICULTY)
onset = round(onset)
#score = converter.parse("france01.mid")
score = converter.parse(midi_url)
#score.quantize([8], processOffsets=True, processDurations=True, inPlace=True)
part = score.elements[0]

#part.insert(0, note.Rest(quarterLength=OFFSET))
    
score = stream.Score()
score.append(part)
score = score.makeMeasures(meter.TimeSignature(f'{timesig}/4'))
score = score.makeNotation()

# adjust rest mess

score.elements[0].remove(score.elements[0].elements[-1])
for num in range(1, onset):
    print("removing " + str(score.elements[1]))
    score.remove(score.elements[1])
for thisElement in score:
    if thisElement.offset > 0:
        thisElement.offset -= onset
score = score[0:4]

us = environment.UserSettings()
us['autoDownload'] = 'allow'
us['lilypondPath'] = 'C:/Program Files (x86)/LilyPond/usr/bin/lilypond.exe'
us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'
us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'

filepath = r'C:\Users\Alice\Documents\GitHub\battlenotes\hi'

conv_musicxml = ConverterMusicXML()
scorename = 'Blues_For_Alice.xml'
out_filepath = conv_musicxml.write(score, 'musicxml', fp=filepath, subformats=['png'])

# importing PIL
from PIL import Image
img = Image.open(filepath + '-1.png')
img.show()
