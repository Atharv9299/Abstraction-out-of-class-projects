class BMW():
    def fuel_type(self):
        print("Premium unleaded gasoline")
    def max_speed(self):
        print("Most BMW's have a top speed of 250km/h")
    def mileage(self):
        print("Moderate to high")
class Ferrari():
    def fuel_type(self):
        print("premium petrol(gasoline)")
    def max_speed(self):
        print("Most ferrari's have a max speed exceeding 322km/h")
    def mileage(self):
        print("Very low")
obj_BMW = BMW()
obj_Ferrari = Ferrari()
for car in(obj_BMW, obj_Ferrari):
    car.fuel_type()
    car.max_speed()
    car.mileage()