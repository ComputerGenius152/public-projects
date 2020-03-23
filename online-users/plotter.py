import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
timeofget = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

print("DO NOT CLOSE THIS WINDOW!")
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("plotting.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)
    plt.xlabel("Seconds Passed",fontsize=12)
    plt.ylabel('Online Users',fontsize=12)
    fig.suptitle(timeofget, fontsize=16)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
