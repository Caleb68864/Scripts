# Downloads everything from a YouTube Playlist before a certain date
# Use -d option to set the date

from ydl import ydl
from optparse import OptionParser
import sys

parser = OptionParser()

parser.add_option("-d", "--date",
                  action="store", dest="datebefore",
                  help="Download all videos after this Date")

(options, args) = parser.parse_args()

ydl_opts = {
	'format' :'bestvideo/best',
	'format' : 'mp4',
	'outtmpl' : '%(title)s.%(ext)s',
	'ignoreerrors' : 'True',
	'restrictfilenames' : 'True',
		}

if options.datebefore:
    print(options.datebefore)
    ydl_opts['dateafter'] = options.datebefore

ydl(ydl_opts, args)
