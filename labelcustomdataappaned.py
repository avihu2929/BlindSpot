"""
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
img = 'https://cdn.londonandpartners.com/asset/a8470577bb79a7460c342bf9a290b604.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
#results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.show()
results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]  # img1 predictions (pandas)
"""

from PIL import Image
import torch
import os

# Model
#model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\Users\avihu\Desktop\inpainting\yolo\yolov5\models\scooter.pt', force_reload=True)


# assign directory
directory = r'C:\Users\avihu\Desktop\inpainting\yolo\labelinyolo\images\\'

# iterate over files in
# that directory


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
i = 0
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
         im=Image.open(f)
         w= int(im.size[0])
         h= int(im.size[1])
         print("===========================")
         results = model(f)
         #print(results.pandas().xyxy[0])
         filenamenew = os.path.splitext(filename)[0]
         #results.show()
         i+=1
         print(i)  
        # print(results.pandas().xyxy[0])
         with open(r'C:\Users\avihu\Desktop\inpainting\yolo\labelinyolo\labels\\'+filenamenew+".txt", 'a') as label:
             for index, row in results.pandas().xyxy[0].iterrows():
                # print(row['class'], row['xmin'])
               # if row["class"] == 0 or row["class"] == 1 or row["class"] == 2: 
                
                 b = (row["xmin"], row["xmax"], row["ymin"], row["ymax"])
                 bb = convert((w,h), b)
                 #print(str(row["class"])+" "+str(bb[0])+" "+str(bb[1])+" "+str(bb[2])+" "+str(bb[3]))
                # if row["confidence"]>0.6:
                 # results.show()
                 
                 #print(bb)
                # print("_________________________")
                 #print(results.pandas().xyxy[0])
                 #results.pandas().xyxy[0].to_txt(r'C:\Users\avihu\Desktop\inpainting\yolo\labelinyolo\labels\\'+filenamenew+".txt", sep='\t')
                 if row["confidence"]>0.6:
                     print(filenamenew)
                     label.write(str(9)+" "+str(bb[0])+" "+str(bb[1])+" "+str(bb[2])+" "+str(bb[3]))
                     label.write('\n')




# Images
#img = r'C:\Users\avihu\Desktop\inpainting\yolo\labelinyolo\images\Screenshot (106).jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
#results = model(img)

# Results
#results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
#results.show()
#print(results.pandas().xyxy[0])
