def BubbleSort(ls):
    for i in xrange(len(ls)-1, 0, -1):
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

def shortBubbleSort(ls):
    exchanges = True
    passnum = len(ls) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if ls[i] > ls[i+1]:
                exchanges = True
                ls[i], ls[i+1] = ls[i+1], ls[i]
        passnum -= 1

#selection sort improves upon bubble sort by making fewer swaps  
def SelectionSort(ls):
    for fillSlot in range(len(ls)-1, 0, -1):
        posMax = 0
        for loc in range(1, fillSlot+1):
            if ls[loc] > ls[posMax]:
                posMax = loc
        #exchange two elements
        ls[posMax], ls[fillSlot] = ls[fillSlot], ls[posMax]
 
def InsertionSort(ls):
    for index in range(1, len(ls)):
        current = ls[index]
        pos = index
        while pos > 0 and ls[pos-1] > current:
            ls[pos] = ls[pos-1]
            pos -= 1
        ls[pos] = current

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
          gapInsertionSort(alist,startposition,sublistcount)

          #print("After increments of size",sublistcount, "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)
   
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

ls = [54,26,93,17,77,31,44,55,20]
quickSort(ls)
print(ls)
