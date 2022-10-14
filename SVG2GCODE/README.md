## SVG to Gcode converter for GRBL pen plotter

Forked from [vishpat/svg2gcode](https://github.com/vishpat/svg2gcode)


I found that the plugins for inkscape and illustrator would crash when I tried to convert SVG's with many thousands of lines to gcode.  
So I modified this to generate gcode for GRBL based pen plotter

**Usage as cli:**

>python convert.py source.svg destination.gcode

**or in bash**

copy 's2g' to your path and run from anywhere
>s2g source.svg target.gcode

**There is a brute force path optimisator algorithm. Very slow for large files, can be disabled in config.py**

**Illustrator exports in points, not mm** regardless of your document settings.  
If units are set to points in the config file, we convert to mm on the fly.

There are various settings you can change in config.py. Most notably, you must set an upper and lower position for the z axis.

* zTravel is the height it will move to before traveling to the next stroke
* zDraw should be the height at which the pen will make contact with the paper
* zDraw should be the height at which the pen will make contact with the paper

