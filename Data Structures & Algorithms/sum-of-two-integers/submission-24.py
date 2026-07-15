class Solution:
    def getSum(self, a: int, b: int) -> int:
        
    
        ret=0
        car=0
        for i in range(32):
            bit1= a>>i&1
            bit2=  b>>i&1
            print(bit1,bit2)
            if bit1>bit2:
                bit1,bit2=bit2,bit1
            if bit1==bit2==car==1:
                
                ret^=1<<i
                continue
            bit1=bit1^car|bit1&car
            if bit1&bit2:
                car=1
            else:
                car=0
            
            ret^=(bit1^bit2)<<i
            print(ret)
        
        mask= 0xFFFFFFFF
        return ret if ret <= 0x7FFFFFFF else ~(ret ^ mask)
        
        

            