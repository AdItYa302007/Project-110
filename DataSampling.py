import statistics
import csv
import pandas as pd
import random
import plotly.figure_factory as ff

df=pd.read_csv("Project110.csv")
data=df["reading_time"].tolist()
#fig=ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()

mean1=statistics.mean(data)
print(mean1)
st1=statistics.stdev(data)
print(st1)

def randomSamples():
    dataset=[]
    for i in range(1,100):
      rand=random.randint(1,len(data)-1)
      value=data[rand]
      dataset.append(value)
    mean2=statistics.mean(dataset)
    return mean2 

def FinalSample():
    mean_list=[]
    for i in range(1,1000):
        setofmean=randomSamples()
        mean_list.append(setofmean)
    finalSampleMean=statistics.mean(mean_list)
    finalSamplest=statistics.stdev(mean_list)
    print("The Mean Of Sampling Distribution(1000 Times)",finalSampleMean)
    print("The Standard Deviation Of Sampling Distribution(1000 Times)",finalSamplest)   
    fig=ff.create_distplot([mean_list],["reading_time"],show_hist=False) 
    fig.show()
    


FinalSample()
      
    




