import numpy as np

#creates a numpy array
a = np.array([2,3,4,5])

#accessing elements
a[0], a[2]
a[1:]
a[::2]
#multi-indexing...creates a new numpy array
a[[0,2,3]]
a.dtype

b = np.array([3,4,5,6,6,8], dtype=float) #creates an array as a float

#Dimensions and shapes
A = np.array([
    [2,3,4],
    [6,7,8]
], dtype=object) #provide the dtype attr 
A.shape #returns the shape of the array
A.size #returns the size:total number of elements
A.ndim #returns dimension

#index and slicing matrices
A[0:2]
A[1][0]
A[:, :2] #all rows but 2 element in each column
A[1]=np.array([10,20,20])
A[1]= 99 #replaces everything in A[2] with 99

#Summary statistics
A.sum()
A.mean() 
A.var()
A.sum(axis=0) #sums all elements in axis one

#broadcasting and vectorised operations
c = np.arange(4)
d = np.array([6,7,8,9])
c+10 #Adds 10 to every element..doesnt modify array
c
c+=10
c + d #adds the two

#Boolean arrays
c[[True,False,False,True]] #selects the true and returns 

c >= 2 #Return a boolean value
c <=10
c[c>10] #returns an array  

c < c.mean() #returns a boolean array of evaluating 
c[c>c.mean()]

c[(c>10) | (c==13)] #or operator

S = np.random.randint(100, size=(4,4)) #Random 4by4 matrix between 0 and 100
S > 70


#random functions in numpy
#arr = np.random.random(size=(2,4))
arra = np.random.normal(size=2)
ar = np.random.rand(2,4)

#reading from files 
fo = open('data1.txt','r')
fo.name
#print(fo.read())
my_data = np.loadtxt(fo.name,skiprows=1)  #only works with no missing values

my_data2 = np.genfromtxt('data2.txt',skip_header=1,filling_values=1.2575)

arr1 = np.ones((4,4),dtype=int)
arr2 = np.full((4,4),4)
arr3 =arr1-arr2
arr3 *= np.identity(4,dtype=int)
arr3*= -1
arr4 = np.sqrt(arr3)
arr4.max(axis=1)