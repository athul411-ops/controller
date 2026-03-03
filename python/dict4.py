device = {"network" : {"ip":123,
			"port":5050},
	"relay":{"r1": False,
	"r2":True}
	}
device["network"]["port"]=9090
device["relay"]["r1"]=True
for values in device["relay"].values():
	print(values)
