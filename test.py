##def func(string,value):
##    if value==0:
##        print(string[1::2])
##    elif value==1:
##        print(string[::2])
##
##def prime(num):
##    for i in range(2,num):
##        if num%i==0:
##            print(f"{num} is not prime num")
##            break
##        else:
##            print(f"{num} is prime num")
##            break
##
##def last_num(num):
##    res=num%10
##    print(res)
##
##def len_iter(a,string,list_,tup,dic):
##    total_len=len(str(a))+len(string)+len(list_)+len(tup)+len(dic)
##    return total_len
##num=50
##p=[]
##def prime():
##    for i in range(2,num+1):
##        if num%i==0:
##            break
##    print(num)
##
### to check number is perfect square
##def perfect_sq(num):
##    for i in range(2,num):
##        if num/i==i:
##            print(f"{num} is perfect square")
##            break
##    else:
##        print(f"{num} is NOT perfect square")
##
###[1,2,3,4,5,6]
##def last(a,n):
##    res=a[-1:-n-1:-1]
##    print(list(res[::-1]))
##
##l=range(1,51)
##
##def even(l):
##    if num%2==0:
##        return num
##
##even_num=lambda num:num%2==0
##
##print(list(filter(even_num,l)))
##
##
##names=['apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram']
##
##even_str=lambda name:len(name)%2==0
##
##even_=print(list(filter(even_str,names)))
##
##names=['laura','steve','bill','james','bob','grieg','scott','alex','ive']
##
##vow_char=lambda name: name[0] in "aeiou"
##
##def vow_ch(name):
##    if name[0] in "aeiou":
##        return name
##    
##
##print(list(filter(vow_ch,names)))
##
####program to return positive numbers
##
##numbers=[-2,-1,0,1,2]
##
##def pos(num):
##    if num>=0:
##        return num
##
##pos_num=lambda num:num>=0
##
##print(list(filter(pos_num,numbers)))
##
####program to print prime number from 1 to 50
##
##p=range(0,51)
##
##def prime(num):
##    for i in range(2,num):
##        if num%i==0:
##            return False
##            break
##    else:
##        return True
##
##print(list(filter(prime,p)))
##
##l=[1,2,3,4,-4,5,-1,-7,9,-4]
##
##neg=lambda num:num<0
##
##print(list(filter(neg,l)))

##square the cube for every num in list

l=[1,2,3,4,5]

sq=lambda num:num**2


def star(string,char):
    if string[0]==char:
        return True

print(star('deepa','d'))



















    
