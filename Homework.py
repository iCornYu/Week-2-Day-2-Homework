#Problem 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]
list1 = [1,11,14,5,8,9]

def lessten(numlist):
    tenlist = []
    for n in numlist:
        if n < 10:
            tenlist.append(n)
    print(tenlist)

            
lessten(list1)



#Problem 2
#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

# lists merged with duplicates
def combinelist1(list1,list2):
    flist = list1 + list2
    flist.sort()
    print(flist)
    



#lists merged without duplicates
def combinelist2(list1,list2):
    flist = list1 + list2
    xlist = []
    for f in flist:
        if f not in xlist:
            xlist.append(f)
    print(xlist)
        
    
combinelist2(l_1,l_2)
    
