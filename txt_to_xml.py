import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, isdir, join
import cv2
mypath = '/home/mark/mark/new_bbox'
myimgpath = '/home/mark/mark/png/image_2'
files = listdir(mypath)


for f in files:
    
	print(f[:-4])
	txtpath = join(mypath , f)
	imgpath = join(myimgpath , f[:-4] +'.png')
	print(txtpath)
	print(imgpath)
	img = cv2.imread(imgpath)
	h ,w ,d = img.shape 
	annotation = ET.Element('annotation')
	folder = ET.SubElement(annotation , 'folder')
	folder.text = 'image_2'
	filename = ET.SubElement(annotation , 'filename')
	filename.text = f[:-4]+'.png'
	path = ET.SubElement(annotation , 'path')
	path.text = imgpath
	source = ET.SubElement(annotation , 'source')
	database = ET.SubElement(source , 'database')
	database.text = 'Unknown' 
	size = ET.SubElement(annotation , 'size')
	widgh = ET.SubElement(size , 'widgh')
	widgh.text = str(w) 
	height = ET.SubElement(size , 'height')
	height.text = str(h) 
	depth = ET.SubElement(size , 'depth')
	depth.text = str(d)
	segmented = ET.SubElement(annotation , 'segmented')
	segmented.text = '0'
	a = open(txtpath)
	for i in a:
		b=i.split()
		objects = ET.SubElement(annotation , 'object')
		name = ET.SubElement(objects , 'name')
		name.text = b[0]
		pose = ET.SubElement(objects , 'pose')
		pose.text = 'Unspecified'
		truncated = ET.SubElement(objects , 'truncated')
		truncated.text = '0'
		difficult = ET.SubElement(objects , 'difficult')
		difficult.text = '0'
		bndbox = ET.SubElement(objects, 'bndbox')
		xmin = ET.SubElement(bndbox, 'xmin')
		xmin.text = int(b[1])
		ymin = ET.SubElement(bndbox, 'ymin')
		ymin.text = int(b[2])
		xmax = ET.SubElement(bndbox, 'xmax')
		xmax.text = int(b[3])
		ymax = ET.SubElement(bndbox, 'ymax')
		ymax.text = int(b[4])
	tree = ET.ElementTree(annotation)
	tree.write(f[:-4]+'.xml')
