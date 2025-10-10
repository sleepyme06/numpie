import numpy as np
from PIL import Image

ip=Image.open('project\\op&ip\\sample_1.jpeg')
print(ip.size)
# Image.fromarray(ip).show()

arr=np.asarray(ip)
print(arr.shape)

R,G,B=arr[:,:,0],arr[:,:,1],arr[:,:,2]
gray = 0.2989 * R + 0.5870 * G + 0.1140 * B #dot product 
gray = np.clip(gray, 0, 255).astype(np.uint8)
print(gray.shape)
# Image.fromarray(gray).show()

downsamplingFactor=6
# array[dim1_start:dim1_stop:dim1_step, dim2_start:dim2_stop:dim2_step, ...] SLICING
down=gray[::downsamplingFactor,::downsamplingFactor]
print(down.shape)
# Image.fromarray(down).show()
# print(np.max(down),np.min(down))
height,width=down.shape

output_file=open('project\\op&ip\\output_art_1.txt','w')
asciiChars="@%#*+=-:. " 
# $@B%8&WM#*oahkbdpqwmZOOQLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. 
print(len(asciiChars))
interval=256/len(asciiChars)
for i in range(0,height,2):
    for j in range(width):
        index=int(down[i,j]/interval)
        output_file.write(asciiChars[index])
    output_file.write('\n')
    

#img->array->grascale array->grascale img->downsample array->downsample img->asciiart txt->ascii art img
#tune->>downsampling factor,asciiChars,range(height)

# sample2=6,big asciichars
# sample1=6,small asciichars
# smaple=8,small asciichars
