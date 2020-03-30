#import smbus
import time
from firebase import firebase

	
	
bus = smbus.SMBus(1) #If I2C library detects the pull up then initialize the register using sensors

	



bus.write_i2c_block_data(0x44, 0x2C, [0x06])
	
time.sleep(0.5)

	
data = bus.read_i2c_block_data(0x44, 0x00, 6)

	
	
temp = data[0] * 256 + data[1] #shifting data[0] to left side and adding data[1] xisting in right side
cTemp = -45 + (175 * temp / 65535.0)              #formula mentioned in datasheet
fTemp = -49 + (315 * temp / 65535.0)              #formula mentioned in datasheet
humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

	
	
print ("Temperature in Celsius is : %.2f C" %cTemp)
print ("Temperature in Fahrenheit is : %.2f F" %fTemp)
print ("Relative Humidity is : %.2f %%RH" %humidity)

	
time.sleep(5)                                                       #5milliseconds
	
	
firebase= firebase.FirebaseApplication('HOST ID')

	
	
result = firebase.post('Project Name', {'cTemp':str(cTemp),'ftemp':str(fTemp), 'humidity':str(humidity)})
print(result)