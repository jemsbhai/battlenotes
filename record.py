# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:04:42 2021

@author: Alice
"""

import pyaudio
import wave
import pretty_midi
from note_recognition import main
from solo_generation_esac import *

if __name__ == "__main__":
    difficulty = 6
    solo_id, mel_id = get_solo_melody(difficulty)
    file, opusnum = get_abc_file(solo_id)
    midi_list = get_correct_notes(mel_id)
    notes_list = [pretty_midi.note_number_to_name(note)[:-1] for note in midi_list]
    display_music(file, opusnum)
        
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = difficulty*6
    filename = "output.wav"
    
    p = pyaudio.PyAudio()
    
    # print available devices
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
    
    print('Recording')
    
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    
    frames = []  # Initialize array to store frames
    
    # Store data in chunks
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()
    
    print('Finished recording')
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    # run analysis
    #main(filename, note_arr=['C', 'E', 'G'], plot_starts=True)
    score = main("output.wav", notes_list, plot_starts=True)
    print(score)
