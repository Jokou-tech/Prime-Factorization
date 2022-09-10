primes=[]
divisors=[]
values=[]
results={}
num=2
a= input("Give number for prime factorization: ")
while a.isnumeric() is False:
    print("Give a positive integer: ")
    a= input("Give number for prime factorization: ")
else:
    if int(a) > 0:
        a = int(a)
        if a == 1:
            print (1)
            exit
        else:
            while num < (a/2):
                x=(num//2)
                while x > 1:
                    if num % x == 0:
                        break
                    x -=1
                else:
                    primes.append(num)
                num += 1
            for i in primes:
                if a % i == 0:
                    divisors.append(i)
                else:
                    continue
            y=a
            for t in divisors:
                while y % t == 0:
                    y = y/t
                    values.append(t)
                    v = values.count(t)
                    results[t]= v
            resultsword=f"{results}"
            resultsword=resultsword.replace("{", "")
            resultsword=resultsword.replace("}", "")
            resultsword=resultsword.replace(": ", "**")
            resultsword=resultsword.replace(",", " x")
            print(resultsword)
