import pyaudio
from ConfigParser import RawConfigParser
from SoundListener import SoundListener
from SendQueue import SendQueue

config = RawConfigParser()
config.read('config.ini')
TOKEN = config.get('telegram', 'token')
CHAT_ID = config.get('telegram', 'chat_id')
PROXY = {
	'https': config.get('telegram', 'proxy'),
	'http': config.get('telegram', 'proxy'),
}

print PROXY



p = pyaudio.PyAudio()
p.get_default_input_device_info()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
    		print "Input Device id ", i, " - ", [p.get_device_info_by_host_api_device_index(0, i).get('name')]

# input_device = raw_input("Select input device: ")


queue = SendQueue(TOKEN, CHAT_ID, PROXY = PROXY)
lis = SoundListener(queue)

raw_input("Press enter to stop\n")

del lis
