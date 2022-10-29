class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkings = {}
        self.parkings[1] = big
        self.parkings[2] = medium
        self.parkings[3] = small


    def addCar(self, carType: int) -> bool:
        if self.parkings[carType] == 0:
            return False
        else:
            self.parkings[carType] -= 1 
            return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)