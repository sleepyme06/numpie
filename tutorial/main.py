from PIL import Image,  ImageDraw,ImageFont
import math as m
# word wrap off
# zoom

asciiChars="$@B%8&WM#*oahkbdpqwmZOOQLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. " 
interval=len(asciiChars)/256
chararray=list(asciiChars)

def getchar(iptext):
    return chararray[m.floor(iptext*interval)]

text_file=open('tutorial\\output_ascii.txt','w')

scale=0.2

im=Image.open("project\\op&ip\\sample.jpeg")
fnt=ImageFont.truetype('c:\\WINDOWS\\Fonts\\L_10646.TTF')
width,height=im.size
print(width,height)
im=im.resize((int(scale*width),int(scale*height*(8/18))),Image.NEAREST)
width,height=im.size
print(width,height)
pix=im.load()

outputim=Image.new('RGB',(8*width,18*height),color=(0,0,0))
width,height=im.size
d=ImageDraw.Draw(outputim)
print(width,height)

for i in range(height):
    for j in range(width):
        r,g,b=pix[j,i]
        h=int(r/3+g/3+b/3)
        pix[j,i]=(h,h,h)
        text_file.write(getchar(h))
        d.text((j*8,i*18),getchar(h),font=fnt,fill=(r,b,g))
    text_file.write('\n')

outputim.save("tutorial\\output.png")
# im.save("output_ascii.txt")
