import sounddevice as sd
import numpy as np
import soundfile as sf
fs = 44100
recorded_data = []
stop_recording = False
input_stream = sd.InputStream(channels=2, samplerate=fs, dtype='float32')
# Start the input stream
input_stream.start()
while True:
    ch = int(input("Enter 1 to record, 2 - stop, 3 - play, 4-exit\n"))

    if ch == 1 :
        try:
            print("Recording Started. Press Crtl+C To Stop Recording")
            while not stop_recording:
                audio_block, overflowed = input_stream.read(fs)
                recorded_data.extend(audio_block)
        except KeyboardInterrupt:
            pass
    elif ch == 2:
        input_stream.stop()
        input_stream.close()
        print("Recording stopped.")
    elif ch == 3:
        if recorded_data:
            print("Playing the recorded audio...")
            sd.play(np.array(recorded_data), fs)
            sd.wait()
        else:
            print("No data to play.")
    elif(ch==4):
        exit(0)
