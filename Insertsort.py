def insertSort(arr):
        for i in range (1,len(arr)):
                t=arr[i]
                j=i-1
                while(j>=0 and t<arr[j]):
                        arr[j+1]=arr[j]
                        j=j-1
                arr[j+1]=t


f=open('t.txt','r')
arr=f.read()
arr = [int(x) for x in arr.split()]
print('исходный массив:', arr)
insertSort(arr)
print('отсортированный массив: ', arr)
sorted=open('sorted.txt','w+')
sorted.write(str(arr))