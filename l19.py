import matplotlib.pyplot as plt
x=(['delhi','mumbai','banglore','hyderabad'])
y=([23456123,20083104,18456123,13411093])
plt.xlabel('city')
plt.ylabel('population')
plt.barh(x,y)
plt.show()
