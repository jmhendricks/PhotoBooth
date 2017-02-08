#tumblr post 20140427010031.gif --host=drumminhands.tumblr.com

import os

filename = "20140427194302.gif"
tumblr_hostname = "drumminhands.tumblr.com"
tumblr_auth_path = "/home/pi/.tumblr" # a file on your computer with all the authorization credentials

tumblr_upload = "tumblr post " + filename + " --host=" + tumblr_hostname + " --credentials=" + tumblr_auth_path

#print tumblr_upload

os.system(tumblr_upload) 

print "Done"




# NOTE this works, but it takes about 2 minutes to post the file.