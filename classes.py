# Class
class myclass:
    # Constructor
    def __init__(self,nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key work required as param
    def getLength(self):
        return self.size

    def getDoubleLength(self):
        return 2 * self.getLength()


if __name__ == '__main__':
    obj = myclass((2,3,4));
    print(obj.getLength())
    print(obj.getDoubleLength())