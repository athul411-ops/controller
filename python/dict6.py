sensor = { "temp":0,
	"humidity" :45,
	"pressure": None}
if sensor["temp"] == 0:
	print("error")
else:
	print("working")
for value in sensor.values():

	print(value)
