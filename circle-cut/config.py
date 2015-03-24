import math

#File 
fname = "24-well_34x34.gcode"
f = open(fname,"w")

#Polygon Parameters
nSides      = 500   # Number of sides to polygon
radius      = 7.8   # Radius of polygon
theta		= 0

#Laser Parameters
feedRate    = 500   # mm/s
laserPower  = 13    # percent max power
pauseTime   = 500   # ms
x_start 	= 414-radius-0.5  # mm
y_start		= 340-radius-0.5	# mm
z_start     = 124.1 #- 25  # mm

## Focus = 124.1 

#Other
decimal     = 3     # number of decimal places in gcode

