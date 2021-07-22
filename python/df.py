import pandas as pd 

myData1 = {'Day':[1,2,3,4,5,6], 'Visitors':[900,400,300,500,200,700],'Bounce Rate':[20,34,25,15,25,40]}
myData2 = {'HPI':[50,50,60,70],'Int_r':[10,15,12,10]}
myData3 = {'HPI':[50,50,60,70],'Int_r':[10,15,12,10]}
index = [2001,2002,2003,2004]
myDf = pd.DataFrame(myData1)

df1 = pd.DataFrame(myData1)
df2 = pd.DataFrame(myData2,index)
df3 = pd.DataFrame(myData3,index)

#slicing dataframes

firstTwo = myDf.head(2)
lastThree = myDf.tail(3)

##Merging and joining 
merged = pd.merge(df2,df3, on = 'HPI')

print(merged)

