import text2emotion as te
import matplotlib.pyplot as plt
import numpy as np

# to read data from file:
file_name=input("enter file name:")
fp=open(file_name,'r')
data=fp.read()
# to find the persons in conversation:
con_find=[]
i=0
fp=open(file_name,'r')
while i<2:
    d=fp.readline()
    if(d!="\n"):
        i+=1
        con_find+=[d]

person_name=[]       
for i in con_find:
    copy=i.split(" â€“ ")
    person_name+=[copy[0]]
    
person1=person_name[0]
person2=person_name[1]

p1_conversation=[]
p2_conversation=[]
c=data.split("\n")

# to seperate data
for line in c:
    name=line.split(" â€“ ")
    if(name[0]==person1):
        p1_conversation+= [name[1]]
    if(name[0]==person2):
        p2_conversation+= [name[1]]


fp.close()

emotion_d1={"Surprise":0.0,"Angry":0.0,"Sad":0.0,"Fear":0.0,"Happy":0.0}
emotion_d2={"Surprise":0.0,"Angry":0.0,"Sad":0.0,"Fear":0.0,"Happy":0.0}
emotion_d={"Surprise":0.0,"Angry":0.0,"Sad":0.0,"Fear":0.0,"Happy":0.0}
for line in p1_conversation:
    result=te.get_emotion(line)
    for key in emotion_d1:
        emotion_d1[key]+=result[key]
        
for line in p2_conversation:
    result=te.get_emotion(line)
    for key in emotion_d2:
        emotion_d2[key]+=result[key]

for i in emotion_d:
    emotion_d[i]=emotion_d1[i] + emotion_d2[i]

print("emotion:\t",person_name[0],"emotion_polarity:\t",person_name[1],"emotion_polarity:")
print("1-Surprise\t",emotion_d1["Surprise"],"\t\t\t\t",emotion_d2["Surprise"])
print("2-Angry\t\t",emotion_d1["Angry"],"\t\t\t\t",emotion_d2["Angry"])
print("3-Sad\t\t",emotion_d1["Sad"],"\t\t\t\t",emotion_d2["Sad"])
print("4-Fear\t\t",emotion_d1["Fear"],"\t\t\t\t",emotion_d2["Fear"])
print("5-Happy\t\t",emotion_d1["Happy"],"\t\t\t\t",emotion_d2["Happy"])
print()
print("emotion in the whole conversation is :")
print(emotion_d)
# red line - person 1
# blue line - person 2

y=np.array(list(emotion_d.values()))
y1=np.array(list(emotion_d1.values()))
y2=np.array(list(emotion_d2.values()))


font1={'family':'serif','color':'orange','size':20}
font2={'family':'serif','color':'green','size':20}
title=person_name[0]+" & "+person_name[1]+" conversation"
plt.title(title)

plt.xlabel("Emotions 1-Surprise | 2-Angry | 3-Sad\n | 4-Fear | 5-Happy",fontdict=font1)
plt.ylabel("polarity",fontdict=font2)
plt.plot(y,"purple",marker='o')
plt.plot(y1,"r-",marker='o')
plt.plot(y2,"blue",marker='o')
plt.grid()
list_det=['Total_emotion',person1,person2]
plt.legend(list_det)

plt.show()
