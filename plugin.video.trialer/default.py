# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Trailer
# (c) 2016 - acidb
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.trailer'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Total film", "user/totalfilmvideo", 'https://yt3.ggpht.com/-61XBFf5PtS4/AAAAAAAAAAI/AAAAAAAAAAA/okxwI1OGv1E/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Falcon", "user/falcondistribuce", 'https://yt3.ggpht.com/-RgY7VU8CvUw/AAAAAAAAAAI/AAAAAAAAAAA/mhZVHHgOM34/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Freeman", "user/WarnerBrosCzech", 'https://yt3.ggpht.com/-i9JlCHxPfss/AAAAAAAAAAI/AAAAAAAAAAA/4B1pD1q7ARE/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Bonton film", "user/BontonfilmCZ", 'https://yt3.ggpht.com/-wvyWFZ73whY/AAAAAAAAAAI/AAAAAAAAAAA/MqnDw8vvwzI/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Filmové novinky", "user/filmnovinky", 'https://yt3.ggpht.com/-lErDxBXAl0o/AAAAAAAAAAI/AAAAAAAAAAA/QWLvrvVNzlo/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("HighFive", "channel/UC_h3dIgci4Hmb66yhQJyLoA", 'https://yt3.ggpht.com/-hpq5_qZoOMo/AAAAAAAAAAI/AAAAAAAAAAA/J-6CuAwizlw/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("CinemArt SK", "user/barracudamoviesro", 'https://yt3.ggpht.com/-PBX6jvwxTJw/AAAAAAAAAAI/AAAAAAAAAAA/VWwMEpR-bG4/s250-c-k-no-rj-c0xffffff/photo.jpg'),		
        ("Svět filmu", "user/svetfilmu", 'https://yt3.ggpht.com/-JErYnzBX8K4/AAAAAAAAAAI/AAAAAAAAAAA/IYDgjyrjr8Q/s250-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Film Europe", "user/filmeuropepictures", 'https://yt3.ggpht.com/-UjxyZPJKVgo/AAAAAAAAAAI/AAAAAAAAAAA/ITX1NSMuips/s250-c-k-no-rj-c0xffffff/photo.jpg'),					
]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()