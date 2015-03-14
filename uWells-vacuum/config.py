#File
fname = '5D11-5ms_46x46.gcode'
f=open(fname,'w')

FOCUS = 124.1

#Laser Parameters
laserPower     = [10] #% max power
dwellTime      = [5] #ms
zValue		   = [1.5] #mm below focus
x_start        = 417
y_start        = 333
pauseTime      = 500 #ms; time paused after movement before ablation
feedRate       = 500 #movement speed

# Rectangle size properties
rectLength     = 46 #mm; x-direction
rectWidth      = 46 #mm; y-direction
spaceSmall     = 3 #mm; space between rectangles
hexLength      = 0.25 #mm

#Other
#relative       = 0 #0 for homing before beginning.  1 if machine has already been homed