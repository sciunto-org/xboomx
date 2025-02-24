# xboomx

xboomx is wrapper for dmenu. The goal is to apply sorting commands according to their launch frequency. In other words - if you launch emacs and lxterminal all the time - they will appear in the list of commands first.

## Installation
```sh
git clone https://github.com/sciunto-org/xboomx
cd xboomx
sudo apt-get install suckless-tools # here is instruction for debian. really we need only dmenu
sudo python setup.py install
```

Available via AUR as `xboomx-snilius`.

## Config
The config file is located at `~/.config/xboomx/config.txt`. It is created during the first execution of xboomx.


Here is an alternative content:
```json
{
  "dmenu_params": "-b -i -nb black -nf orange -sb black -p \"#\"",
  "ignorelist": ["X"],
  "complete_offpath": false
}
```

For `dmenu_params` please see the manpages for dmenu.
```sh
man dmenu
```

The `ignorelist` to prevent stuff that is in your path for showing up as suggestions. Like if you type `x` then `X` might show up before `xbmc`.

`complete_offpath` will add everything that's in you ranking database regardless of availability on PATH. This is off by default.

## License

    xboomx
    Copyright (C) 2014-2015  Victor Häggqvist
    Copyright (C) 2025 Francois Boulogne

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

For original license see the file `LICENSE.org`

This is a fork of https://bitbucket.org/dehun/xboomx and https://github.com/victorhaggqvist/xboomx
