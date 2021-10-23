print("ELASTICITY CALCULATOR")

question1 = input("do you want income elasticicty of demand (type(INCOME)) or cross price elasticity(type(CROSS)):")

def income_elasticicty():
 q1 = (float(input("put your initial quantity here: ")))
 q2 = (float(input("put the new quantity here: ")))
 y1 = (float(input("put the initial income: ")))
 y2 = (float(input("put the new income: ")))
 
 quantity_difference = q2-q1
 quantity_average = (q2+q1)/2
 quantity = quantity_difference/quantity_average
 income_difference = y2-y1
 income_average = (y2+y1)/2
 income = income_difference/income_average
 elasticity = quantity/income
 
 print(f"the income elasticity is {elasticity:.1f}")
 if elasticity == 1:
  print("unitary")
 if elasticity > 1:
  print("elastic")
 if elasticity < 1:
  print("inelastic") 


def cross_price_elasticity():
 p1 = (float(input("put the intial product price here: ")))
 p2 = (float(input("put your new product price here: ")))
 q1 = (float(input("put your initial quantity here: ")))
 q2 = (float(input("put the new quantity here: ")))

 difference = q2-q1
 average  =  (q2 + q1)/2
 quantity = difference/average
 price_diffence = p2-p1
 price_average = (p2 + p1)/2
 price = price_diffence/price_average 

 elasticity = quantity/price

 print(f"the elastiscity of this product is {elasticity:.1f}")
 if elasticity == 1:
  print("unitary")
 if elasticity > 1:
  print("elastic")
 if elasticity < 1:
  print("inelastic")
 
if question1 == "INCOME":
 income_elasticicty()
 
if question1 == "CROSS":
 cross_price_elasticity()
 
 

