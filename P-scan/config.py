#File
fname = 'ParamScanC_14-10-28.gcode'
f=open(fname,'w')

FOCUS = 125.25

#Laser Parameters
laserPowers     = [20,17.5,15,12.5,10] #% max power
dwellTimes      = [9,7,5,3,1] #ms
zValues			= [0,0.5,1,1.5,2]
x_start        	= 414
y_start        	= 343
pauseTime      	= 500 #ms; time paused after movement before ablation
feedRate       	= 500 #movement speed

# Rectangle size properties
length 			= 4
spaceSmall     	= 0.6 #mm; space between rectangles
spaceLarge		= 1.5
hexLength      	= 0.5 #mm


#Other
relative       	= 0 #1 for no starting x,y; 0 for using starting co-ordinates

## Orientation
#Note: Enter a combination of 1, 2, and 3
# Positions one and two will be prominently visible from the side.  Position Three will be
# manifest in multiple strips of PDMS
#1 = Laser power
#2 = Dwell Time
#3 = z Values
orientation = "213"