import matplotlib.pyplot as plt

#subplot 1
cubed=[]
inputVal=[1,2,3,4,5]
for num in inputVal:
    cubed.append(num*num*num)
ax1=plt.subplot(1,2,1)
ax1.plot(inputVal,cubed, marker="D", c="purple", lw="3.0", ls=":")
plt.title("Cubed Numbers")
plt.ylabel("Values Cubed")
plt.xlabel("Input Values")
plt.grid()

#subplot 2
list2=[]
for num in inputVal:
    list2.append(num*num)
ax2=plt.subplot(1,2,2)
plt.style.use("seaborn-poster")
ax2.plot(inputVal,list2, c="green")
plt.title("Numbers Raised", c="green")
plt.ylabel("Second Power")
plt.xlabel("Input Values")
plt.grid(color="green")
plt.suptitle("Fun with Numbers", c="orange", fontfamily="Courier New",fontsize="18")
plt.show()