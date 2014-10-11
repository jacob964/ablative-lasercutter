#File 
fname = "6-well.gcode"
f = open(fname,"w")

#Polygon Parameters
nSides      = 500   # Number of sides to polygon
radius      = 17.5   # Radius of polygon

#Laser Parameters
feedRate    = 500   # mm/s
laserPower  = 13    # percent max power
pauseTime   = 500   # ms
x_start 	= 401-radius   # mm
y_start		= 342-radius	# mm
z_start     = 110.4 # mm

#Other
decimal     = 3     # number of decimal places in gcode

