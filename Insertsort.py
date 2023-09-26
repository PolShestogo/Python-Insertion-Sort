import random

def insertSort(arr):
        for i in range (1,len(arr)):
                t=arr[i]
                j=i-1
                while(j>=0 and t<arr[j]):
                        arr[j+1]=arr[j]
                        j=j-1
                arr[j+1]=t

try:
        n= input("Введите количество элементов сортируемого массива: ")
        if abs(int(n))>=100000:
                print('Слишком большое количество элементов')
                exit()
except Exception:
        print("Некорректный ввод")
        exit() 

file=open('input.txt','w+')
file.write(str(random.randint(0,100)))
for i in range (1, int(n)-1):
        file.write(' ')
        file.write(str(random.randint(-100,100)))       
file.close()
file=open('input.txt','r')
arr=list((file.read()).split())
print('Исходный массив:', str(arr))
insertSort(arr)
print('Отсортированный массив: ', arr)
sorted=open('sorted.txt','w+')
sorted.write(str(arr))