#! /usr/bin/env python
import pynotify
class notify_msg:
	def msg(self,mstr):
		#mstr='The scoreis 102/3'
		title="SCORE"
		#os.environ.setdefault('DISPLAY', ':0.0')
		#os.system('notify-send -i "notification-message-IM" "'+title+'" "'+mstr+'"')
		pynotify.init('my apps')
		pynotify.Notification(''+title+'',''+mstr+'').show()




