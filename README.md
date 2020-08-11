# Weather Conrtolled Walppapers
### What it is?
This is a little python script that changes your system wallpaper(currently working only on linux kde distro's(planning to make support for more distro's and windows)) according to weather outside.
### How do I install it?
1. Make sure you have `requests`, `json`, `datetime`, `dbus` python packages installed.
	- You can test it by writing `pip3 list` in your terminal and serach for this packages or just run python script and see errors.
	- You can install packages by writing `pip3 install <name-of-a-package>` in your terminal.
2. Download the [source code](https://github.com/4EBOOT/weather-controlled-wallpapers/archive/master.zip).
3. Unzip it wherever you want.
4. Before you add `weather-controlled-wallpapers.py` script to autoload, you can test it by modifying debug values in it. Example:
	```debug = True
	debug_value = "Sunny"```

### How can I modify/change wallpapers?
Script already goes with pack of predownloaded in `wallpapers/` folder. But you can modify/change. For that you need to place your wallpaper in `wallpapers/` folder and rename it to weather you want to replace(all names of weather can be found [here](https://github.com/chubin/wttr.in/blob/master/lib/constants.py)).
You can suggest to change some of preinstalled wallpapers or add them(Discord: Reboot#8695).