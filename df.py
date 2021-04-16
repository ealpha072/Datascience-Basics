import pandas as pd 

myData = {'Day':[1,2,3,4,5,6], 'Visitors':[900,400,300,500,200,700],'Bounce Rate':[20,34,25,15,25,40]}

myDf = pd.DataFrame(myData)
print(myDf)