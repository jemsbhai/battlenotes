# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:10:55 2021

@author: Alice
"""

import pandas as pd
import sqlite3
from music21 import *
from music21.converter.subConverters import ConverterMidi, ConverterMusicXML
import random
import os
import re

def get_solo_melody(difficulty):

    con = sqlite3.connect("esac.db")
    solo_info = "esac_info2"
    
    # Load the solo data into a DataFrame
    solo_info_df = pd.read_sql_query(f"SELECT * from {solo_info}", con)
    # Get random solo with appropriate difficulty
    solo = solo_info_df[abs(solo_info_df['avg_events_per_bar'] - difficulty) < 1].sample(1)
    #solo_id = 'A0128A'
    solo_id = solo.iloc[0]['esacid']
    mel_id = solo.iloc[0]['melid']
    print(solo_id)
    return solo_id, mel_id

def get_abc_file(esacid):
    user_input = 'esac'
    directory = os.listdir(user_input)
    
    searchstring = f'N: {esacid}\n'
    file = ''
    for fname in directory:
        if os.path.isfile(user_input + os.sep + fname):
            # Full path
            f = open(user_input + os.sep + fname, 'r', errors='ignore')
            if searchstring in f.read():
                file = fname
                
                print(file)
                f.close()
                break
            f.close()

    nextbreak = 0
    # find line number of esacid
    with open(user_input + os.sep + file, 'r', errors='ignore') as myFile:
        for num, line in enumerate(myFile, 1):
            if searchstring in line and nextbreak==0:
                print('found at line:', num)
                linenum = num
                nextbreak = 1
            elif '\n' == line and nextbreak == 1:
                nextbreak = num
                print('next break:', nextbreak)
            
                
    with open(user_input + os.sep + file, 'r', errors='ignore') as myFile:
        opusnum = myFile.readlines()[linenum-3][2:-1]
        print('opus', opusnum)
    with open(user_input + os.sep + file, 'r', errors='ignore') as myFile:
        musictext = myFile.readlines()[linenum+6:nextbreak-1]
        print('music text', musictext)
    
    return file, opusnum

def display_music(file, opusnum):
    s = converter.parse(f'esac/{file}', number=opusnum)
    s.metadata.title = ''
    us = environment.UserSettings()
    us['autoDownload'] = 'allow'
    us['lilypondPath'] = 'C:/Program Files (x86)/LilyPond/usr/bin/lilypond.exe'
    us['musescoreDirectPNGPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'
    us['musicxmlPath'] = 'C:/Program Files/MuseScore 3/bin/MuseScore3.exe'
    
    filepath = r'output'
    
    conv_musicxml = ConverterMusicXML()
    out_filepath = conv_musicxml.write(s, 'musicxml', fp=filepath, subformats=['png'])

    # importing PIL
    from PIL import Image
    img = Image.open(filepath + '-1.png')
    img.show()


def get_correct_notes(mel_id):
    con = sqlite3.connect("esac.db")
    melody_df = pd.read_sql_query(f"SELECT * from melody WHERE melid = {mel_id}", con)
    melody_list = list(melody_df['pitch'])
    return melody_list
    
if __name__ == "__main__":
    solo_id, mel_id = get_solo_melody(4)
    file, opusnum = get_abc_file(solo_id)
    get_correct_notes(mel_id)
    display_music(file, opusnum)

