
# @Title: 座位预约管理系统 (Seat Reservation Manager)
# @Author: cocofe
# @Date: 2021-05-01 23:36:26
# @Runtime: 792 ms
# @Memory: 40.8 MB

class SeatManager:

    def __init__(self, n: int):
        self.seats = list(range(n, 0, -1))

    def reserve(self) -> int:
        return self.seats.pop()
    
    def binary_search(self, target):
        left, right = 0, len(self.seats) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.seats[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return left
                
    def unreserve(self, seatNumber: int) -> None:
        if not self.seats:
            self.seats.append(seatNumber)
        idx = self.binary_search(seatNumber)
        self.seats.insert(idx, seatNumber)
        



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
