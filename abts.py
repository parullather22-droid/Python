#airline booking ticket system
#departure                              #arrival
print("welcome yo hawa hawai airlines")
print("please select your departure place ")
print("1.delhi-DEL")
print("2.kolkata-KKL") 
print("3.ahemadabad-AHM")
print("4.benagaluru-BLR")
print("5.mumbai-BOM")
enter=int(input("enter your departure place = "))

print("select your arrival destination")
print("1.brazil-GIG")
print("2.sweden-ARN") 
print("3.london-LHR")
print("4.italy-FCO")
print("5.toronto-YYZ")
enter=int(input("enter your arrival place ="))

#Types of passenger
print("1.ADT-adult(18+) 80000")
print("2.YTH-youth(14-18) 80000")
print("3.CHD child(6-13) 50000")
print("4.INFS-infant on seat 50000")
print("5.INF-infant in lap 25000")


adult=int(input("Enter number of adults="))
if(adult>=0):
    adult_tkt_price = adult*80000
else:
    adult_tkt_price = adult*80000

youth=int(input("youth="))    
if(youth>=0):
    youth_tkt_price = youth*80000
else:
    youth_tkt_price = youth*80000

child=int(input("child="))
if(child>=0):
    child_tkt_price = child*80000
else:
    child_tkt_price = child*80000

INFseat=int(input("infant on seat="))    
if(INFseat>=0):
    INFseat_price = INFseat*50000
else:
    INFseat_price = INFseat*50000

INFlap=int(input("infant in lap="))    
if(INFlap>=0):
    INFlap_price = INFlap*30000
else:
    INFlap_price = INFlap*30000

Ticket_Price = adult_tkt_price + youth_tkt_price + child_tkt_price + INFseat +INFlap_price
print("Your ticket price = ",Ticket_Price)    

#baggage allowance
print("standardbag=4kg")
print("carriedbag=25kg per kg 1000rs fine")

carriedbag=int(input("enter no of carried bag="))
weight=int(input("enter carried bags weight="))

w=weight-25
if(carriedbag>0):
    carried_bg_weight =w*1000
else:
    carried_bg_weight = carriedbag * w *1000

print("Your bag price =",carried_bg_weight)    

Itenary_price = Ticket_Price + carried_bg_weight
print("Your final booking price =",Itenary_price)



