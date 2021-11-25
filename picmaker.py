import Image
from random import randrange as r   #We import in this format to make our code more condensed, as were only using this one feature of random for one prupose we can make it a single letter for simplicity

def rng():    #Generates a set of random values for the Red, Green, and Blue channels
  rvR = r(0,256)
  rvG = r(0,256)
  rvB = r(0,256)
  rvA = 255   #Sets the Alpha to 255
  rv = (rvR,rvG,rvG,rvA)    #Converts to Tuple
  return(rv)    #Returns the Tuple, exposing it as the output value of this constructor function

def makeTestImage(x,y):   #Generates a random image
  x = int(x)
  y = int(y)
  xy = (x,y)    #Converts user input to Int format and converts to Tuple
  img = Image.new('RGBA', (xy), (255,255,255,255))    #Creates a solid white backdrop of variable size, specified above
  px1 = img.size[0]
  px2 = img.size[1]
  for x in range(px1):    #Iterates through every column
    for y in range(px2):    #Iterates through every row, which in combination with the previous line results in a left to right top to bottom scan of the entire image
      rv = rng()    #for every pixel generates a new set of random color channel values
      img.putpixel((x,y),(rv))    #sets the pixel to its unique set of values
  img.save("test.png")    #saves the image