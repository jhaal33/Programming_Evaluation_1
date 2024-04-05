#_____________QUESTION 1 : ASCII ART______________
# to print my name i used https://patorjk.com/software/taag/#p=display&f=NV%20Script&t=Jayne%0A this is a Ascii art generator
print("""
     gg                                                   
    dP8,                                                  
   dP Yb                                                  
  ,8  `8,                                                 
  I8   Yb                                                 
  `8b, `8,     ,gggg,gg  gg     gg   ,ggg,,ggg,    ,ggg,  
   `"Y88888   dP"  "Y8I  I8     8I  ,8" "8P" "8,  i8" "8i 
       "Y8   i8'    ,8I  I8,   ,8I  I8   8I   8I  I8, ,8I 
        ,88,,d8,   ,d8b,,d8b, ,d8I ,dP   8I   Yb, `YbadP' 
    ,ad88888P"Y8888P"`Y8P""Y88P"8888P'   8I   `Y8888P"Y888
  ,dP"'   Yb                  ,d8I'                       
 ,8'      I8                ,dP'8I                        
,8'       I8               ,8"  8I                        
I8,      ,8'               I8   8I                        
`Y8,___,d8'                `8, ,8I                        
  "Y888P"                   `Y8P"                         




""")

#_____________QUESTION 2 : Triangle calulator______________
print("TRIANGLE CALCULATOR")
#import math to help with calulations
import math 

print("Hi there! Allow me to help you calculate the area of a triangle! To do this we will need the three side lengths",)

# ask the user for 3 side lengths of the triangle of the triangle
s1 = float(input("what is the length of the first side of the triangle?"))
s2 = float(input("what is the length of the second side of the triangle?"))
s3 = float(input("what is the length of the third side of the triangle?"))

#calculate s 
s = (s1 + s2 + s3)/2

#calculate the area of the triangle
a = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

#print the area of the triangle
print('\n' "The area of the triangle is", a, "square units", "thats", round(a, 2), "rounded to 2 decimals\n")

#_____________QUESTION 3 : Budget calculator______________
import random
print("\n \n \n BUGET CALCULATOR")
#ask the user for their income and calculate that per month
print("lets make a monthly budget together!")
income = float(input("What is your annual income?"))

#RESEARCH 
#average person spends $150-200 on gas each month
#average person spend $1655 on car insurance
#apparently you should spend 10-15 percent on grocies i read this in a global news article


#ask user for some of their regular expenses expenses
rent = float(input("What is the cost of rent or mortgage each month?"))
carpay = float(input("What is the cost of your car payments each month(without insurance or gas)?"))

#calculate the total car expenses (150 for gas and 1655 for car insurance) then subract that and rent and food from the income
monthly_car = carpay + 1655 + 150
annual_car = monthly_car * 12
annual_rent = rent * 12
CP = ((annual_car/income)*100)
CR = ((annual_rent/income)*100)
CF = 0.15

annual_food = income*0.15
monthly_food = annual_food/12
new_amount = income - annual_car - annual_rent - annual_food

#other stuff to buget for (using random percents)
p1 = random.uniform(0.01,0.2)
p2 = random.uniform(0.01,0.2)
p3 = random.uniform(0.01,0.2)
p4 = random.uniform(0.01,0.2)
p5 = random.uniform(0.01,0.2)
p6 = 1-p5-p4-p3-p2-p1


other_bills = new_amount*p1/12
savings = new_amount*p2/12
enertainment = new_amount*p3/12
member = new_amount*p4/12
necessities = new_amount*p5/12
personal =new_amount*p6/12

#change the percents values to whole numbers so we can print
p_p1 = p1*100
p_p2 = p2*100
p_p3 = p3*100
p_p4 = p4*100
p_p5 = p5*100
p_p6 = p6*100

print("\n \n Car Expenses: $", round(annual_car,2), "per year", "or", round(monthly_car, 2), "per month thats", CP, "percent of your income")
print("Rent : $", round(annual_rent,2), "per year", "or", rent, "per month thats", CR, "percent of your income")
print("Food : $", round(annual_food,2), "per year", "or", round(monthly_food, 2), "per month thats", CF, "percent of your income")
print("\n After these expenses you are left with", round(new_amount,2))

print("\n Other bills: $", round(other_bills, 2), "per month thats", round(p_p1, 2) ,"% of your new amount anually(this is for water, electricity, ect)")
print("Savings: $", round(savings, 2), "per month thats", round(p_p2, 2), "% of the new amount (this is highly reccondmended but not necassary)")
print( "Enertainment: $", round(enertainment, 2),"per month thats", round(p_p3, 2), "% of the new amount per year")
print( "Member: $", round(member, 2), "per month thats", round(p_p4, 2), "% of the new amount per year this includes any gym meberships and subscriptions such as netflix")
print( "Necessities: $", round(necessities, 2), "per month thats", round(p_p5, 2), "% of the new amount per year this is for essentials such as tolietries, clothes, etc")
print( "Personal: $", round(personal, 2), "per month thats", round(p_p6, 2),"% of the new amount per year this is for things such as hobbies, gifts and anything you want!")
Text only submission	Feb 21, 2024 10:52 AM
10 hours late
