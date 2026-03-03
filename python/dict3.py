employe ={"emp1" :4000,
	"emp2" :5000,
	"emp3" :6000,
	"emp4" :7000,}
for key,value in employe.items():
	if value < 7000 :
	  employe[key]+= 500
	
print(employe)
for key,value in employe.items():
	if value < 7000:
	 print(key,value)
print("Updated:", employe)
