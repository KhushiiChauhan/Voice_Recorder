import sounddevice as sd
import numpy as np
import soundfile as sf
import tkinter as tk
from tkinter import messagebox

fs = 44100
recorded_data = []
stop_recording = False

input_stream = sd.InputStream(channels=2, samplerate=fs, dtype='float32')

# Function to start recording
def start_recording():
    global recorded_data, stop_recording
    recorded_data = []  # Reset the recorded data
    try:
        print("Recording Started. Press Stop to Stop Recording")
        while not stop_recording:
            audio_block, overflowed = input_stream.read(fs)
            recorded_data.extend(audio_block)
    except KeyboardInterrupt:
        pass

# Function to stop recording
def stop_recording():
    global stop_recording
    stop_recording = True
    input_stream.stop()
    input_stream.close()
    print("Recording stopped.")

# Function to play recorded audio
def play_recorded_audio():
    if recorded_data:
        print("Playing the recorded audio...")
        sd.play(np.array(recorded_data), fs)
        sd.wait()
    else:
        print("No data to play.")

# Create the main window
root = tk.Tk()
root.title("Audio Recorder")

# Create and configure the buttons
record_button = tk.Button(root, text="Record", command=start_recording)
stop_button = tk.Button(root, text="Stop", command=stop_recording)
play_button = tk.Button(root, text="Play", command=play_recorded_audio)
exit_button = tk.Button(root, text="Exit", command=root.quit)

# Pack the buttons into the window
record_button.pack()
stop_button.pack()
play_button.pack()
exit_button.pack()

# Start the input stream
input_stream.start()

# Run the GUI main loop
root.mainloop()
