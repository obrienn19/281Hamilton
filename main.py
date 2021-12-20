import numpy as np
import pandas as pd
import math

SmallStateWinner = 0
LargeStateWinner = 0
tie = 0
mindistrict=[]
df=[]
IA1=[]
IA2=[]
Re1=[]
Re2=[]
def Hamilton2State():
    global SmallStateWinner, LargeStateWinner, tie, mindistrict, df, IA1, IA2, Re1, Re2
    pop1=np.random.randint(1000,2000, size=1, dtype=int)
    pop2=np.random.randint(5000,10000, size=1, dtype=int)
    np.set_printoptions(suppress=True)
    #print("Population 2", pop2)
    #print("Population 1", pop1)
    sum=pop1+pop2
    sum1=sum.item(0)-2
    mindistrict=1
    length1=sum1/mindistrict
    length=math.trunc(length1)
    poplength=length-2
    #print("Available House Sizes", poplength)
    x = np.arange(poplength, dtype=int)
    population=np.full_like(x, sum)
    #print("Population Total Array", population)
    housesize=np.arange(2,length)
    #print("All House Sizes Array", housesize)
    StandardD=population/housesize
    #print("Standard Divisor Array", StandardD)
    y = np.arange(poplength, dtype=int)
    IA11=np.full_like(y, pop1.item(0))
    #print("State 1 Array", IA11)
    IA1=IA11/StandardD
    #print("Initial Allocation State 1 Array", IA1)
    z = np.arange(poplength, dtype=int)
    IA22=np.full_like(z, pop2.item(0))
    #print("State 2 Array", IA22)
    IA2=IA22/StandardD
    #print("Initial Allocation State 2 Array", IA2)
    LQ1=np.floor(IA1)
    LQ2=np.floor(IA2)
    Re1=IA1-LQ1
    Re2=IA2-LQ2
    #print("Lower Quota Lownde's", LQ1)
    #print("Lower Quota Lownde's", LQ2)
    #LQ1[LQ1 == 0] = 1
    #R1= Re1 / LQ1
    #R2= Re2 / LQ2
    #print("Fractional Part Lownde's 1", R1)
    #print("Fractional Part Lownde's 2", R2)
    R1=np.reshape(Re1,(poplength,1))
    R2=np.reshape(Re2,(poplength,1))
    combo=np.concatenate((R1,R2), axis=1)
    df=pd.DataFrame(combo, columns=['R1', 'R2'])
    df['R1Winner']=df['R1'].gt(df['R2'])
    df['R2Winner'] = df['R1'].lt(df['R2'])
    df.replace({False: 0, True: 1}, inplace=True)
    count1=df.R1Winner.values.sum()
    count3=df.R2Winner.values.sum()
    #print(count1, count3)
    if count1 > count3:
         SmallStateWinner += 1
    elif count1 == count3:
         tie += 1
    elif count3 > count1:
         LargeStateWinner += 1
    else:
        pass
def repeat_fun(times, f):
    for i in range(times): f()
    print("SmallStateWinner:", SmallStateWinner)
    print("LargeStateWinner:", LargeStateWinner)
    print("Tie:", tie)
repeat_fun(1, Hamilton2State)
#a1=np.array(['1000-2000'], dtype=object)
#a2=np.array(['5000-10000'], dtype=object)
#a3=np.array([SmallStateWinner], dtype=object)
#a4=np.array([LargeStateWinner], dtype=object)
#a5=np.array([tie], dtype=object)
#a6=np.array([mindistrict])
#df1=pd.DataFrame(a1, columns=['Small State Range'])
#df2=pd.DataFrame(a2, columns=['Large State Range'])
#df3=pd.DataFrame(a3, columns=['Small State Wins'])
#df4=pd.DataFrame(a4, columns=['Large State Wins'])
#df5=pd.DataFrame(a5, columns=['Ties'])
#df6=pd.DataFrame(a6, columns=['Minimum District Size'])
#df7=pd.concat([df1, df2, df3, df4, df5, df6], axis=1)
#print(df3)
#print(df4)
#p1=df.head(15)
#p2=df.tail(15)
#df7=p1.append(p2)
#df7=pd.DataFrame(IA1, columns=['Fractional Part'])
#df8=pd.DataFrame(IA2, columns=['Fractional Part'])
#df9=pd.concat([df7, df8], axis=1)
#print(df9.head())
#df.to_csv('mirror.csv', header=True)
# #df7.to_csv('df156.csv', header=True)



