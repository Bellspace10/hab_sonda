from mpu6050 import mpu6050
import time
import logging

logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('logs/mpu.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

sensor = mpu6050(0x68)
try:
   while True:
      accel_data = sensor.get_accel_data()
      gyro_data = sensor.get_gyro_data()  
      temp = sensor.get_temp()            

      ax = accel_data['x']
      ay = accel_data['y']
      az = accel_data['z']
      gx = gyro_data['x']
      gy = gyro_data['y']
      gz = gyro_data['z']

   
      print ("accel. x: %s \t y: %s \t z: %s" % (str(round(ax,4)), str(round(ay,4)), str(round(az,4))))
      print ("gir. x: %s \t y: %s \t z: %s" % (str(round(gx,4)), str(round(gy,4)), str(round(gz,4))))
      print ("temp: %s C" % str(round(temp,2)))

      logger.info(str(round(ax,4)) + "|" + str(round(ay,4)) + "|" + str(round(az,4)) + "|" + str(round(gx,4)) + "|" + str(round(gy,4)) + "|" + str(round(gz,4)) + "|" + str(round(temp,2)));
      time.sleep(1)

except:
  print ('execucio interrompuda')
