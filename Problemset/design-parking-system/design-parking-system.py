
# @Title: 设计停车系统 (Design Parking System)
# @Author: cocofe
# @Date: 2021-03-19 00:05:29
# @Runtime: 500 ms
# @Memory: 13.5 MB

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parking = [big, medium, small]


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.parking[carType-1] > 0:
            self.parking[carType-1] -= 1
            return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
