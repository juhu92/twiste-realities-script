from PIL import Image
import sys


firstImg = Image.open("./serie/0000.png")
frameSize = firstImg.width, firstImg.height
firstImg.close()


def fi (i):
  return str(i).zfill(4)



def writeRowToFrame( frame, source, y ):
  for x in range(source.width):
    frame.putpixel( (x,y), source.getpixel((x,y)) )


def makeframe(start_index):
  frame = Image.new("RGB", frameSize)
  source_index = start_index
  for y in range(frameSize[1]):
    source = Image.open("./serie/"+fi(source_index)+".png")
    writeRowToFrame( frame, source, y )
    print "frame: "+str(start_index)+ " row:"+fi(source_index)
    source.close()
    if source_index+1 < frameSize[1]:
      source_index += 1
    else:
      source_index = 0

  frame.save("./result/"+fi(start_index)+".png")
  frame.close()
  return



inputstr = raw_input("enter [1] for rendering a single frame \nenter [2] for rendering all frames:\n")
print inputstr

if inputstr == "1":
  makeframe(0)
elif inputstr == "2":
  for f in range(frameSize[1]):
    makeframe(f)
else:
  print "nothing done..."
  sys.exit();


