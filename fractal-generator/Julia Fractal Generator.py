# Julia Fractal 
from PIL import Image
import os, time
   
starttime = time.time()

# setting the width, height, zoom, background colour, init image
progress = 0
length = int(input("Length: "))
width = int(input("Width: "))
zoom = float(input("Zoom: "))
bgcolour = input("Background Colour: ")
fractal = Image.new("RGB", (length, width), bgcolour) 


# allocating the storage for the image and loading the pixel data. 
pix = fractal.load() 
 
# setting up the variables according to the equation to create the fractal 
cX, cY = -0.7, 0.27015
moveX, moveY = 0.0, 0.0
maxIter = 255

for x in range(length): 
    for y in range(width): 
        zx = 1.5*(x - length/2)/(0.5*zoom*length) + moveX 
        zy = 1.0*(y - width/2)/(0.5*zoom*width) + moveY 
        i = maxIter 
        while zx*zx + zy*zy < 4 and i > 1: 
            tmp = zx*zx - zy*zy + cX 
            zy,zx = 2.0*zx*zy + cY, tmp 
            i -= 1
            
        # convert byte to RGB (3 bytes), kinda magic to get nice colors 
        pix[x,y] = (i << 21) + (i << 10) + i*8
        
    # progress indicator
    progress += 1
    print('{}/{} operations complete. {}% done.'.format(progress, length, round((progress*100/(length)))))

# save the created fractal
os.chdir('C://Users/chena/Desktop')
fractal.save("fractal.png")
print('Generated in {} seconds.'.format(time.time()-starttime))
fractal.show()
