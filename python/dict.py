car = { 
	"benz":2,
	"bmw":4,
	"bike" :[5,7],
	"jeep":{
	"mahindra":2,
	"susu":3}
}
print(car["bike"])
print(car)
print(car["jeep"]["susu"])
print(car.get(1))
for key,value in car["jeep"].items():
	print(key,value)
