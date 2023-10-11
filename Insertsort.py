import random
import timeit

def insertSort(arr):
        for i in range (1,len(arr)):
                t=int(arr[i])
                j=i-1
                while(j>=0 and t<int(arr[j])):
                        arr[j+1]=arr[j]
                        j=j-1
                arr[j+1]=t

def main():  
        max=1000
        min=-1000
        nmax=100000              
        try:
                n= input("Введите количество элементов сортируемого массива: ")
                if abs(int(n))>=nmax:
                        print('Слишком большое количество элементов')
                        exit()
        except Exception:
                print("Некорректный ввод")
                exit() 
        file=open('input.txt','w+')
        file.write(str(random.randint(min,max)))
        for i in range (1, int(n)-1):
                file.write(' ')
                file.write(str(random.randint(min,max)))       
        file.close()
        file=open('input.txt','r')
        arr=list((file.read()).split())
        print('Исходный массив:', str(arr))
        start = timeit.default_timer()
        insertSort(arr)
        end= timeit.default_timer()
        print('Отсортированный массив: ', arr)
        sorted=open('sorted.txt','w+')
        sorted.write(str(arr))
        print("Время сортировки: ", end-start)

if __name__ == '__main__':
    main()