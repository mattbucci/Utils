import sys
import urllib
from PIL import Image

im = Image.open(sys.argv[1])
width, height = im.size
import urllib

testfile = urllib.URLopener()
txtsize = "~text?txtsize=%d" % (int(im.size[1] / 5))
txt = "&txt=%dx%d" % im.size
size = "&w=%d&h=%d" % im.size
url = "https://placeholdit.imgix.net/" + txtsize + txt  + size
testfile.retrieve(url, sys.argv[1])
