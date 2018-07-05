from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record(c_context=None):
    p = pyaudio.PyAudio()
    # stream = p.open(format=FORMAT, channels=1, rate=RATE,
    stream = p.open(format=FORMAT, channels=1, rate=c_context.PITCH if c_context else RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()

        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        # elif not silent and not snd_started and not c_context.STARTED:
        elif not c_context.STARTED:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    c_context.record_btn.setEnabled(False)

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path, pitch=0, c_context=None):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record(c_context=c_context)
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    # wf.setframerate(RATE + pitch)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

def rec(filename, rate=0, c_context=None):
    print("please speak a word into the microphone")
    record_to_file(filename, pitch=rate, c_context=c_context)
    print("done - result written to demo.wav")

if __name__ == '__main__':
    rec('test.mp3')