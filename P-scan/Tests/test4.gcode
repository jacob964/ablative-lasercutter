;(***************uWellPlate******************)
;(*** Monday, October 27, 2014 @ 03:23:36 PM ***)
G91 ; absolute coordinates
;(***************End of Beginning*********************)
M3 S0
G90
G0 X408 Y344 F2000
G91
G90
G0 Z122.25 F300
G4 P250
G91
G1 B1 X-5 F500 S1 L2000 P2.0
M3 S0
G0 X5 Y-1 F2000
G4 P500
G90
G0 Z120.25 F300
G4 P250
G91
G1 B1 X-5 F500 S1 L2000 P2.0
M3 S0
G0 X5 Y-1 F2000
G4 P500
M3 S0
G0 X0 Y-1.5 F2000
G4 P500
M3 S0
G0 X-7.5 Y3.5 F2000
G4 P500

;(end of the file, shutdown routines)
M3 S0 ; Laser PWM set to zero
