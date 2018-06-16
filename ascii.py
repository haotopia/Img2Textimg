import time
import sys
from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')#输入文件
parser.add_argument('-o','--output')#输出文件
parser.add_argument('--width',type=int,default = 80)#输出字符画宽度
parser.add_argument('--height',type=int,default=80)#输出字符画高度

#获取参数
args=parser.parse_args()

IMG=args.file
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

#将256灰度映射到70个字符上
def get_char(r,g,b,alpha=256):
	if alpha==0:
		return ' '
	length=len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g +0.0722 *b)

	unit=(256.0+1)/length
	return ascii_char[int(gray/unit)]

#进度条
def process_bar(precent, width=50):
    use_num = int(precent*width)
    space_num = int(width-use_num)
    precent = precent*100
    print('[%s%s]%d%%'%(use_num*'#', space_num*' ',precent),file=sys.stdout,flush=True, end='\r')

if __name__=='__main__':
	im = Image.open(IMG)
	im = im.resize((WIDTH,HEIGHT),Image.NEAREST)
	txt = ""
	time_start=time.clock()
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt +='\n'		

		#字符画输出到文件
		if OUTPUT:
			with open(OUTPUT,'w') as f:
				f.write(txt)
		else:
			with open("output.txt",'w') as f:
				f.write(txt)
		process_bar(i/(HEIGHT-1))
	print('\n')
	print(txt)