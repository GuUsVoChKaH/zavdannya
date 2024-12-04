a = 'Hello world!'
name ='pavlo'
surname = 'Soroka'
age = 16

lst = [a, name, surname, age] # Список змінних
lst1 = [] #Значення змінних  
lst2 = [] #Типи змінні
string = [] #змінні з str
floatt = [] # float
intt = [] # int
for item in lst:
     lst1.append(item) 
     lst2.append(type(item)) 
     if type(item) == str:
          string.append(item)
     elif type(item) == int:
          intt.append(item)
     elif type(item) == float:
          floatt.append(item)
if len(string) > len(floatt) and len(string) > len(intt):
     print('Більше значень із типом str')
elif len(floatt) > len(string) and len(floatt) > len(intt):
     print('Більше значень із типом float')
else:
     print('Більше значень із типом int')
print (lst2)
print (lst1)