import matplotlib.pyplot as plt

labels = ['PNG','JPEG','SVG','GIF','Other']
numSites = [376,348,153,104,19]
explode = (.1,0,0,0,0)
wedgeColors = ('green','blue','orange','red', 'purple')
plt.pie(numSites, explode=explode,labels=labels,autopct='%3.1f%%',shadow=True,startangle=-45,colors=wedgeColors)
plt.suptitle("Popular Image Formats on the Web")
plt.show()