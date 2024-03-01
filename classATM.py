from itertools import chain,combinations                                 #importing the combinations from itertools
class ATM:
    def __init__(self):
        self.currency_notes = {}                                   #it is dictionary type to store the no of nominations of respective currency
    def deposit_denominations(self,ten,twenty,fifty,hundred,two_hundred,five_hundred):     #take input of no of nominations input
        self.ten = ten
        self.twenty = twenty                                            #using the self. parameter to use that in other function
        self.fifty = fifty
        self.hundred = hundred
        self.two_hundred = two_hundred
        self.five_hundred = five_hundred
        
        self.currency_notes["Tens"] = [10]*ten
        self.currency_notes["Twentys"] = [20]*twenty                         #these lines stores the lists in self.currency_notes -
        self.currency_notes['Fiftys'] = [50]*fifty                            #like [tens] = [10,10] etc 
        self.currency_notes["Hundreds"] = [100]*hundred
        self.currency_notes["Two_Hundreds"] = [200]*two_hundred
        self.currency_notes["Five_Hundreds"] = [500]*five_hundred
        
        
    def Balance(self):                          
        self.notes = ["Tens","Twentys",'Fiftys',"Hundreds","Two_Hundreds","Five_Hundreds"]
        self.currency = []                                      #using this self.currency to store respective currency like [[10,10],[20],..etc]
        for x in range(len(self.notes)):
            self.currency.append(self.currency_notes[self.notes[x]])
        self.result = (list(chain(*self.currency)))                             #chain from itertools used to remove outerlist brackets
        balance = 0                                                       #storing in self.result as [10,10,20,....etc]
        for i in  self.result :
            balance += i
        #print(f"Initial Balance : {balance}")                       #used to print the balance
    
    def with_draw(self,amount):                                      #takes how much amount user want to withdraw
        self.amount = amount
        final = []
        
        for i in range(len(self.result)+1):                     #using here self.result to currency notes 
          for j in combinations(self.result,i):               #using combinations from itertools to check what combinations sum is withdraw amount
                if sum(j) == self.amount:
                    final.append(j)                #j will be in tuple as (...) this append this in final list
                  
        used_notes = (list(*[final[0]]))            #eg :[(10,20,50)] this * is used to remove () outside brackets 0 here indicate index 
                                                         #starting index is the best case of choosing the currency notes
        for k in used_notes :
            self.result.remove(k)                     #the nominations which are used to remove from total nominations
        self.balance_notes = self.result                  #stores the remaining  nominations
        
        a10 = []
        a20 = []
        a100 = []                      #making the seperate the respective nominations
        a50 = []
        a200 = []
        a500 = []
        
        for i in range(len(used_notes)):                        
            if 10 in used_notes:
                used_notes.remove(10)                                            #this for loop is used to remove nominations from usednotes and append them their resp list
                a10.append(10)
            elif 20 in used_notes:
                used_notes.remove(20)
                a20.append(20) 
            if 50 in used_notes:
                used_notes.remove(50)
                a50.append(50)
            elif 100 in used_notes:
                used_notes.remove(100)
                a100.append(100) 
            if 200 in used_notes:
                used_notes.remove(200)
                a200.append(200)
            elif 500 in used_notes:
                used_notes.remove(500)
                a500.append(500)                  

        for i in range(len(a10)):
            self.currency_notes['Tens'].remove(10)                              #removing the nominations the main self.currencey dict this removes the used nominations
        for i in range(len(a20)):
            self.currency_notes['Twentys'].remove(20) 
        for i in range(len(a50)):
            self.currency_notes['Fiftys'].remove(50)         
        for i in range(len(a100)):
            self.currency_notes['Hundreds'].remove(100)     
        for i in range(len(a200)):
            self.currency_notes['Two_Hundreds'].remove(200)  
        for i in range(len(a500)):
            self.currency_notes['Five_Hundreds'].remove(500)     
               
        USED_NOTES = [self.ten-len(self.currency_notes["Tens"]),self.twenty-len(self.currency_notes["Twentys"]),self.fifty-len(self.currency_notes["Fiftys"])
                      ,self.hundred-len(self.currency_notes["Hundreds"]),self.two_hundred-len(self.currency_notes["Two_Hundreds"]),
                      self.five_hundred-len(self.currency_notes["Five_Hundreds"])]  
        print(f"{USED_NOTES}")                   #subtract the user_no_notes notes and final notes using  the len parameter shows the res number which notes are used
          
        final_result =  [len(self.currency_notes["Tens"]),len(self.currency_notes["Twentys"]),len(self.currency_notes["Fiftys"]),
                         len(self.currency_notes["Hundreds"]),
                         len(self.currency_notes["Two_Hundreds"]),len(self.currency_notes["Five_Hundreds"])]  
        #print(f"[10,20,50,100,200,500] = {final_result}")                                      #return the remaining nominations left  from the initial 
             
    def update_Balance(self):
        final_balance = 0
        for i in self.balance_notes:
            final_balance += i                                                        #print the final balance after withdraw
        #print(f"FINAL BALANCE : {final_balance}")    
             
        
                 
            
            
user = ATM()
user.deposit_denominations(1,4,3,3,4,1)  
(user.Balance())
(user.with_draw(330)) 
user.update_Balance()          