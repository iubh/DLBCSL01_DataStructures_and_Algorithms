import unittest

class CustData:
    def __init__(self, ID, age):
        self._ID = ID
        self._age = age
        self._points = 0
        
    def get_ID(self):
        return self._ID
    
    def get_age(self):
        return self._age
    
    def get_points(self):
        return self._points
    
    def update_points(self,r):
        self._points+=r
        
    def offer(self, low, high, amt):
        if(self._age in range(low,high+1)) \
            and (self._points == 0):
                self.update_points(amt)
                return True
        else:
                return False
       
 
custList=[]   
custList.insert(0,CustData(1555,18))
custList.insert(1,CustData(1322,23))
custList[1].update_points(50)
custList.insert(2,CustData(1687,25))
custList.insert(3,CustData(3231,53))
        
    
def test_offer():
    assert custList[0].offer(18,25,50) == True,\
        "test_offer0_FAIL"
        
    assert custList[1].offer(18,25,50) == False,\
        "test_offer1_FAIL"
                
    assert custList[2].offer(18,25,50) == True,\
        "test_offer2_FAIL"
              
    assert custList[3].offer(18,25,50) == False,\
        "test_offer3_FAIL"              
        
test_offer()

if __name__ == '__main__':
    unittest.main()
