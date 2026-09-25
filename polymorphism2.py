class bike:
    def ride(self,km):
        print(f"he ride bike so fast at {km}")

class car(bike):
    def ride(self,km):
        super().ride(km)
        print(f"he ride car so fast at {km}")
#creating object of class car
ob1=car()
ob1.ride(100)