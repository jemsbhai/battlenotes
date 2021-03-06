# taken largely from https://github.com/ianvonseggern1/note-prediction

from pydub import AudioSegment
import pydub.scipy_effects
import numpy as np
import scipy
import matplotlib.pyplot as plt
from solo_generation_esac import *

from utils import frequency_spectrum, \
    calculate_distance, \
    classify_note_attempt_1, \
    classify_note_attempt_2, \
    classify_note_attempt_3


def main(file, note_arr=None, plot_starts=False, plot_fft_indices=[]):
    actual_notes = []
                
    if note_arr:
        actual_notes = note_arr

    song = AudioSegment.from_file(file)
    #song = song.high_pass_filter(80, order=4)

    starts = predict_note_starts(song, plot_starts)

    predicted_notes = predict_notes(song, starts, plot_fft_indices)

    print("")
    if actual_notes:
        print("Actual Notes")
        print(actual_notes)
    print("Predicted Notes")
    print(predicted_notes)

    if actual_notes:
        lev_distance = calculate_distance(predicted_notes, actual_notes)
        score = abs(len(actual_notes) - lev_distance)/len(actual_notes)
        print("Levenshtein distance: {}/{}".format(lev_distance, len(actual_notes)))
        return score

# Very simple implementation, just requires a minimum volume and looks for left edges by
# comparing with the prior sample, also requires a minimum distance between starts
# Future improvements could include smoothing and/or comparing multiple samples
#
# song: pydub.AudioSegment
# plot: bool, whether to show a plot of start times
# actual_starts: []float, time into song of each actual note start (seconds)
#
# Returns perdicted starts in ms
def predict_note_starts(song, plot):
    # Size of segments to break song into for volume calculations
    SEGMENT_MS = 50
    # Minimum volume necessary to be considered a note
    VOLUME_THRESHOLD = -27.8
    # The increase from one sample to the next required to be considered a note
    EDGE_THRESHOLD = 0.09
    # Throw out any additional notes found in this window
    MIN_MS_BETWEEN = 100

    # Filter out lower frequencies to reduce noise
    #song = song.high_pass_filter(80, order=4)
    # dBFS is decibels relative to the maximum possible loudness
    volume = [segment.dBFS for segment in song[::SEGMENT_MS]]

    predicted_starts = []
    for i in range(1, len(volume)):
        if volume[i] > VOLUME_THRESHOLD and volume[i] - volume[i - 1] > EDGE_THRESHOLD:
            ms = i * SEGMENT_MS
            # Ignore any too close together
            if len(predicted_starts) == 0 or ms - predicted_starts[-1] >= MIN_MS_BETWEEN:
                predicted_starts.append(ms)
            #predicted_starts.append(ms)
    #for i in range(len(predicted_starts)-2):
    #    if predicted_starts[i+1] - predicted_starts[i] <= MIN_MS_BETWEEN:
    #        predicted_starts.remove(predicted_starts[i])


    # Plot the volume over time (sec)
    if plot:
        x_axis = np.arange(len(volume)) * (SEGMENT_MS / 1000)
        plt.plot(x_axis, volume)

        # Add vertical lines for predicted note starts and actual note starts
        for ms in predicted_starts:
            plt.axvline(x=(ms / 1000), color="g", linewidth=0.5, linestyle=":")

        plt.show()

    return predicted_starts


def predict_notes(song, starts, plot_fft_indices):
    predicted_notes = []
    for i, start in enumerate(starts):
        sample_from = start + 50
        sample_to = start + 200
        if i < len(starts) - 1:
            sample_to = min(starts[i + 1], sample_to)
        segment = song[sample_from:sample_to]
        freqs, freq_magnitudes = frequency_spectrum(segment)

        predicted = classify_note_attempt_2(freqs, freq_magnitudes)
        predicted_notes.append(predicted or "U")

        # Print general info
        print("")
        print("Note: {}".format(i))
        print("Predicted start: {}".format(start))
        length = sample_to - sample_from
        print("Sampled from {} to {} ({} ms)".format(sample_from, sample_to, length))
        print("Frequency sample period: {}hz".format(freqs[1]))

        # Print peak info
        peak_indicies, props = scipy.signal.find_peaks(freq_magnitudes, height=0.015)
        print("Peaks of more than 1.5 percent of total frequency contribution:")
        for j, peak in enumerate(peak_indicies):
            freq = freqs[peak]
            magnitude = props["peak_heights"][j]
            print("{:.1f}hz with magnitude {:.3f}".format(freq, magnitude))

        if i in plot_fft_indices:
            plt.plot(freqs, freq_magnitudes, "b")
            plt.xlabel("Freq (Hz)")
            plt.ylabel("|X(freq)|")
            plt.show()
    return predicted_notes


if __name__ == "__main__":
    main("untitled.wav", note_arr=["C", "D", "E", "F", "G", "A"], plot_starts=True)
    