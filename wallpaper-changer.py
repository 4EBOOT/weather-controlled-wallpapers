import dbus
import requests
import json
import time
from datetime import date, datetime, timedelta



#changable variables
wallpaper_folder ="/home/reboot/Development/wallpaper-changer/wallpapers/"
#season_setting - the wallpapers with similar weather, but different seasons will be different(WIP)
season_check = False
check_time = 3
debug = False
debug_value = "Fog"

#don't change this variables!
Y = 2000
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]
current_wallpaper = None

#script that code sends to system and changes wallpaper
jscript = """
var Desktops = desktops();                                                                                                                       
for (i=0;i<Desktops.length;i++) {
        d = Desktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper",
                                    "org.kde.image",
                                    "General");
        d.writeConfig("Image", "file://%s%s.png");
}
"""

#function for getting current season(WIP)
def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

def change_wallpaper(wallpaper_name):
  session_bus = dbus.SessionBus()
  plasma = dbus.Interface(session_bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface = 'org.kde.PlasmaShell')
  plasma.evaluateScript(jscript % (wallpaper_folder, wallpaper_name))
  current_wallpaper = wallpaper_name

def check_weather():
  get_weather = requests.get("https://www.wttr.in/?format=j1")
  search = get_weather.json()
  current_weather = search["current_condition"][0]["weatherDesc"][0]["value"] if not debug else debug_value
  current_season = get_season(date.today()) if season_check else ""
  return current_season + current_weather

#main loop
while True:
  weather = check_weather()
  if weather != current_wallpaper or debug:
    change_wallpaper(weather)
  print(weather)
  time.sleep(check_time)







