class Atm(object):
    def __init__(self,AtmCardNumber,pinNumber) :
        self.AtmCardNumber=AtmCardNumber
        self.pinNumber=pinNumber
       
     
        
    def CashWithdrawl(self):
        print("CashWithdrawl")
        
    def BalanceEnquiry(self):
        print("BalanceEnquiry")
   
        
cash=Atm("432578","756")
print(cash.pinNumber)