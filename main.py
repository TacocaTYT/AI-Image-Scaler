import Image
from picmaker import makeTestImage as mti

mti(input("How wide?: "),input("How tall?: "))    #User tells the program how large the test image should be

def ScaleImage(file):   #This large function allows the user to specify any image in the programs folder and upscale it using the algorithm
  imgSource = Image.open(file)
  sipx = (imgSource.size[0]*2, imgSource.size[1]*2)
  imgTemp = Image.new('RGBA', sipx, (0,0,0,0))    #Here we create a new blank transparent image as our canvas for expansion
  imgOutput = imgTemp.load()
  px1 = imgSource.size[0]
  px2 = imgSource.size[1]
  for x in range(px2):
    for y in range(px1):    #Also iterates thorugh the source image
      cpx1 = (x*2,y*2)    #Gets every other pixel of every other row
      cpx2 = (x,y)
      imgTemp.putpixel(cpx1, imgSource.getpixel(cpx2))    #Puts the pixel of the source image onto its corresponding pixel in the canvas, but moved one pixel away from the previous and when a new row is reached it will skip a row. This results in a staggered pattern of pixels if the program stops here.
  for x in range(imgTemp.size[0]):
    for y in range(imgTemp.size[1]):    #Now we begin iterating through the canvas
      if x%2 == 0:
        if y%2 == 0:    #The % operator performs remainder division and returns the remainder. In our case we use it to find every even pixel
          xpx = (x,y)
          xpx2 = (x-2,y)
          xpx3 = (x-1, y)
          dummy2 = tuple(map(sum, zip(imgTemp.getpixel(xpx), imgTemp.getpixel(xpx2))))    #Here we have queued up the current pixel, the pixel to its left, and the pixel 2 pixels to the left. The pixel directly left of the current pixel will be blank, so to fill it in we take the color value of the current pixel and the pixel 2 spots to the left and add the 3 color channels together.
          if dummy2[3]/2 < 255:   #Here we check for transparent pixels, and if a pixel is transparent (indicated by the Alpha channels of the targeted pixels being summed and divided by 2 resulting in a number less than 255) and if so, we set the pixel we are editing to also be transparent.
            dummy3 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 0)
          else:   #If it is not adjacent to transparent pixels, we average the Red, Green, and Blue channels by summing the individual channels and dividing by the number of sources, in this case 2.
            dummy3 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 255)
          imgTemp.putpixel(xpx3,dummy3)   #We then set the pixel we are editing to the averaged value. Stopping here leaves us with an interesting streak effect
          xpx = (x,y)
          xpx2 = (x,y-2)
          xpx3 = (x, y-1)
          dummy2 = tuple(map(sum, zip(imgTemp.getpixel(xpx), imgTemp.getpixel(xpx2))))    #We then repeat the above process for the vertical columns.
          if dummy2[3]/2 < 255:
            dummy3 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 0)
          else:
            dummy3 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 255)
          imgTemp.putpixel(xpx3,dummy3)   #Stopping here gives us a patchwork pattern
          xpx = (x,y)   #Things get complicated here, but basically we grab the current pixel and the pixel 2 spots to the left, 2 spots below, and 2 spots diagonally down and to the left.
          xpx2 = (x-2,y)
          xpx3 = (x-1, y-1)
          xpx21 = (x, y-2)
          xpx22 = (x-2, y-2)
          dummy2 = tuple(map(sum, zip(imgTemp.getpixel(xpx), imgTemp.getpixel(xpx2))))    #We add 2 of those pixels together
          dummy3 = tuple(map(sum, zip(imgTemp.getpixel(xpx21), imgTemp.getpixel(xpx22))))   #Then the other 2 pixels
          if dummy2[3]/2 < 255:   #Next we find the transparency of the first 2 pixels
            dummy5 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 0)    #and the average
          else:   #and if it is not adjacent to transparent we set the Alpha to 255
            dummy5 = (int(dummy2[0]/2), int(dummy2[1]/2), int(dummy2[2]/2), 255)
          if dummy3[3]/2 < 255:   #Rinse and repeat for the other 2 pixels
            dummy6 = (int(dummy3[0]/2), int(dummy3[1]/2), int(dummy3[2]/2), 0)
          else:
            dummy6 = (int(dummy3[0]/2), int(dummy3[1]/2), int(dummy3[2]/2), 255)
          dummy4 = tuple(map(sum, zip(dummy5, dummy6)))   #Sum those averages together
          if dummy4[3]/2 < 255:   #And repeat the process once more to find the average of all 4 pixels
            dummy7 = (int(dummy4[0]/2), int(dummy4[1]/2), int(dummy4[2]/2), 0)
          else:
            dummy7 = (int(dummy4[0]/2), int(dummy4[1]/2), int(dummy4[2]/2), 255)
          imgTemp.putpixel(xpx3,dummy7)   #And then we set teh pixel in the middle of the 4 pixels we tested to the average of all 4 pixels, which fills in the patchwork pattern and completes our upscaling algorithm.



  imgTemp.save("output.png")    #Finally we save the image so it can be opened and viewed
ScaleImage(input("What file? remeber to type in the file extension as well, for example \"cabbage.png\" -> "))    #This line allows the user to input the name of a file when they run the program