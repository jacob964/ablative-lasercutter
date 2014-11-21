import math

#File 
fname = "12-well_4.gcode"
f = open(fname,"w")

#Polygon Parameters
nSides      = 500   # Number of sides to polygon
radius      = 11   # Radius of polygon
theta		= 0

#Laser Parameters
feedRate    = 250   # mm/s
laserPower  = 14    # percent max power
pauseTime   = 500   # ms
x_start 	= 421-radius-0.5  # mm
y_start		= 348-radius-0.5	# mm
z_start     = 124.1 # mm

#Other
decimal     = 3     # number of decimal places in gcode

