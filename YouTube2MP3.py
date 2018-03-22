# Downloads Link and Converts it to MP3
# Use -n to add numbers to the beginning of the title based on the playlist index

from ydl import ydl
from optparse import OptionParser
import sys

parser = OptionParser()

parser.add_option("-n", "--numbers",
                  action="store_true", dest="numbers", default=False,
                  help="Add's Numbers to beginning of title based on playlist index")

(options, args) = parser.parse_args()

ydl_opts = {
	'format' :'bestaudio/best',
	'audio-format' : 'mp3',
	'outtmpl' : '%(title)s.%(ext)s',
	'ignoreerrors' : 'True',
	'restrictfilenames' : 'True',
		}

if options.numbers:
    #print(options.datebefore)
    ydl_opts['outtmpl'] = '%(playlist_index)s-%(title)s.%(ext)s'

ydl(ydl_opts, args)
