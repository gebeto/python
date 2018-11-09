import pyaudio
from ConfigParser import ConfigParser
from SoundListener import SoundListener
from SendQueue import SendQueue

config = ConfigParser(allow_no_value=True)
config.read('config.ini')
TOKEN = config.get('telegram', 'token')
CHAT_ID = config.get('telegram', 'chat_id')
_PROXY = config.get('telegram', 'proxy') if 'proxy' in config.options('telegram') else None
PROXY = {
	'https': _PROXY,
	'http': _PROXY,
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
