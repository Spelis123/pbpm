# <ins>PBPM</ins>

<ins>**P**</ins>oly<ins>**b**</ins>ar <ins>**P**</ins>ac<ins>**m**</ins>an

Polybar plugin that tells you how many outdated packages you have

# Installation
## Pre-built
1. Download [the executable](https://github.com/Spelis123/pbpm/raw/main/pbpm) And put it in `/bin/` or any other place (just remember where it is)
2. Put this in your `.config/polybar/config.ini` file:
```
[module/pbpm]
type = custom/script
exec = /bin/pbpm
interval = 15
format = <label>
label = %output%
label-foreground = ${colors.primary}
```
## Build from source
### Build Dependencies:
* pyinstaller
* (optional), a text editor
* and a functioning computer running an OS (totally optional, no sarcasm (sarcasm))
* Polybar (or any other status bar)
# Building
1. Download [this](https://github.com/Spelis123/pbpm/raw/main/main.py) source code
2. Make Changes (optional)
3. Run `pyinstaller <file-name> -F` in a terminal
4. Put it anywhere you want as long as you remember it. (least effort with `/bin`)
5. Put this in your polybar config file (`.config/polybar/config.ini`):
```
[module/pbpm]
type = custom/script
exec = /bin/pbpm
interval = 15
format = <label>
label = %output%
label-foreground = ${colors.primary}
```
