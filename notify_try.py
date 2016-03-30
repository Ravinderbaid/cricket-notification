#! /usr/bin/env python
import os
class notify_msg:
	def msg(self,mstr):
		#mstr='The scoreis 102/3'
		title="SCORE"
		os.system('notify-send -i "notification-message-IM" "'+title+'" "'+mstr+'"')



