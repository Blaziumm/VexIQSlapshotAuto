def fowardvel(rvel, lvel, delay):
  rmotor.set_velocity(rvel, PERCENT)
  lmotor.set_velocity(lvel, PERCENT)
  wait(delay, MSEC)
  
