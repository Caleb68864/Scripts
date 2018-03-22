# Downloads a YouTube Playlist with different name conventions based on the options set
# -r, --reverse - Downloads playlist in reverse
# -n, --no-numbers - -Downloads the playlist with no numbers at beginning of the title
# -s, --start - Sets the Start point of the playlist
# -e, --end - Sets the End point of the playlist

from ydl import ydl
from optparse import OptionParser
import sys

parser = OptionParser()

parser.add_option("-r", "--reverse",
                  action="store_true", dest="reverse", default=False,
                  help="Download Playlist in Reverse")
parser.add_option("-n", "--no-numbers",
                  action="store_true", dest="nonumbers", default=False,
                  help="Download Playlist with No Numbers in front of the title")
parser.add_option("-s", "--start",
                  action="store", dest="start", default=False,
                  help="Set The Start Playlist Downlaod")
parser.add_option("-e", "--end",
                  action="store", dest="end", default=False,
                  help="Set The End Playlist Downlaod")



(options, args) = parser.parse_args()

ydl_opts = {
	'format' :'bestvideo/best',
	'format' : 'mp4',
	'outtmpl' : '%(playlist)s/00%(playlist_index)s-%(title)s.%(ext)s',
	#'download_archive' : '%(playlist)s/%(playlist)s.txt',
	'ignoreerrors' : 'True',
	'restrictfilenames' : 'True',
		}

if options.nonumbers == True:
	ydl_opts['outtmpl'] = '%(playlist)s/%(title)s.%(ext)s'

if options.reverse == True:
	ydl_opts['playlistreverse'] = True

if options.start:
	ydl_opts['playliststart'] = int(options.start)

if options.end:
	ydl_opts['playlistend'] = int(options.end)



ydl(ydl_opts, args)
