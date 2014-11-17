import math

#File 
fname = "test-rotated_square.gcode"
f = open(fname,"w")

#Polygon Parameters
nSides      = 4   # Number of sides to polygon
radius      = 10   # Radius of polygon
theta		= math.pi / 4.0

#Laser Parameters
feedRate    = 250   # mm/s
laserPower  = 13    # percent max power
pauseTime   = 500   # ms
x_start 	= 416-radius   # mm
y_start		= 341-radius	# mm
z_start     = 124.1 # mm

#Other
decimal     = 3     # number of decimal places in gcode

