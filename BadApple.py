import thumby



#The video's framerate is 30 fps
thumby.display.setFPS(30)

f = open("Games/BadApple/videodata.bin", "rb")

def GetByte():
    return int.from_bytes(f.read(1),"big")

#Get file size
f.seek(0, 2)
length = f.tell()
f.seek(0)

xPos = 9
width = GetByte()
height = GetByte()
imageDataLength = width*(height/8) #NOTE: This doesn't work properly if the height isn't a multiple of 8


while(f.tell() < length):
    spritedata = bytearray()
    
    #Read and decode the sprite data
    #Format (repeated): 1st byte: sequence byte, 2nd byte: sequence length
    while(True):
        byte = f.read(1) #Get the sequence byte
        sequenceLength = GetByte() #Get the sequence length (1 for single bytes)
        
        #Add all the copies of the single byte to the list
        for i in range(sequenceLength):
            spritedata += byte
        
        if len(spritedata) >= imageDataLength: break
    

    sprite = thumby.Sprite(width,height,spritedata)
    
    sprite.x = xPos

    thumby.display.fill(0) # Fill canvas to black

    # Display the bitmap using bitmap data, position, and bitmap dimensions
    thumby.display.drawSprite(sprite)
    thumby.display.update()
