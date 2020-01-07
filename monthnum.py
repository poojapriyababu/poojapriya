month=input("enter the month number : ")
month=int(month)
if(month==4 or month==6 or month==9 or month==11):
  num=30
  print("number of days in the month : ",num)
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
  num=31
  print("number of days in the month : ",num)
if(month==2):
  num=28
  num1=29
  print("number of days in this month : ",num,num1)
