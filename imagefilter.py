######################################
# Image Filter Project Starter Code  #
#                                    #
#             UTeach CSP             #
#                                    #
######################################


# importing PIL.Image library and os library
from distutils.ccompiler import new_compiler
from PIL import Image  # from PIL import Image
import os
import random

# Deletes old created images if they exist
images = ["StudentWork/combinedFilters.jpg", "StudentWork/filter1.jpg",
    "StudentWork/filter2.jpg", "StudentWork/filter3.jpg", "StudentWork/gray.jpg"]
for i in images:
	if os.path.exists(i):
		os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('StudentWork/image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
	scale = mwidth
else:
	scale = mheight
if scale != 0:
	img = img.resize((width // scale, height // scale))

########################
#    Example Filter    #
########################


def gray():
	print("Code for grayscale")
	# Creates an ImageCore Object from original image
	pixels = img.getdata()
	# Creates empty array to hold new pixel values
	new_pixels = []
	# For every pixel from our original image, it saves
	# a copy of that pixel to our new_pixels array
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		# Perform pixel manipulation and stores results
		# to a new red, green and blue components
		newr = (r + g + b) // 3
		newg = (r + g + b) // 3
		newb = (r + g + b) // 3
		# Assign new red, green and blue components to pixel
		# # at that specific location
		new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
		location = location + 1
	# Creates a new image, the same size as the original
	# using RGB value format
	newImage = Image.new("RGB", img.size)
	# Assigns the new pixel values to newImage
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage


#####################
#    Your Filter    #
#####################

def filter1():
    print("Code for filter1")
    pixels = img.getdata()
    new_pixels = []
    tempinverted = []
    for p in pixels:
        new_pixels.append(p) 
        tempinverted.append(p)
    location = len(new_pixels)-1
    templocation = 0
    while location > 0 and templocation < len(new_pixels):
        p = new_pixels[location]
        r = p[0]
        g = p[1]
        b = p[2]
		# Perform pixel manipulation and stores results
		# to a new red, green and blue components
        if(r%2==0):
            newr = r
        else:
            newr = 0
        if(g%2==0):
            newg = g
        else:
            newg = 0
        if(b%2==0):
            newb = b
        else:
            newb = 0
		# Changes the location to the next pixel in array
        tempinverted[templocation] = (newg, newb, newr)
        location -= 1
        templocation += 1
	# Creates a new image, the same size as the original
	# using RGB value format
    newImage = Image.new("RGB", img.size)
    newImage.putdata(tempinverted)
    return newImage

#####################################
#    Your Filters with User Input   #
#####################################

### Hostile Mob Filter
def filter2():
	print("Code for filter2")
	pixels = img.getdata()
	new_pixels = []
	for p in pixels:
		new_pixels.append(p) 
	userChoice = input("What mob filter would you like?"+
    "Case sensitive! (creeper, enderman, derek)\n")
	while True:
		if(userChoice!="creeper" and userChoice!="enderman" and userChoice!="derek"):
			userChoice = input("Invalid filter! What mob filter would you like?"
            + "Case sensitive! (creeper, enderman, derek)\n")
		else:
			break
	pastedImage = Image.open(userChoice+'.png', 'r')
	pastedImage.thumbnail((64,64), Image.ANTIALIAS)
	# pastedImage.putalpha(50)
	bg_w, bg_h = img.size
	creeperoverload = int(input("Input the number of mobs you want on this filter\n"))
	random.seed(random.randint(0,100))
	for i in range (0,creeperoverload):
		r1 = random.randint(0, bg_w-64)
		r2 = random.randint(0, bg_h-64)
		img.paste(pastedImage,(r1, r2))
	newImage = img
	return newImage

### The "shoutout to Minecraft" filter
def filter3():
    print("Code for filter3")
    pixels = img.getdata()
    new_pixels = []
    for x in range(0, len(pixels), 8):
        for y in range(8):
            new_pixels.append(pixels[x])
    location = 0
    while location < len(new_pixels):
        p = new_pixels[location]
        r = p[0]
        g = p[1]
        b = p[2]
        newg = g
        if(r>0):
            newr = r-255
        else:
            newr = 0		
        if(b>0):
            newb = b-255
        else:
            newb = 0
        # newr = 0
        # newb = 0
        new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
        location = location + 1
    newImage = Image.new("RGB", img.size)
    newImage.putdata(new_pixels)
    return newImage

# # Creates the four filter images and saves them to our files
# a = gray()
# a.save("StudentWork/gray.jpg")
# b = filter1()
# b.save("StudentWork/filter1.jpg")
# c = filter2()
# c.save("StudentWork/filter2.jpg")
# d = filter3()
# d.save("StudentWork/filter3.jpg")

# Image filter names for use below
f1 = "filter1"
f2 = "filter2"
f3 = "filter3"

# Apply multiple filters through prompts with the user
print("\nThe following prompt will ask you which filter to apply to the combined filter. It will keep asking until you answer 'done'.")
answer = input("\nWhich filter do you want me to apply?\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n done\n\n")
while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "done":
	answer = input("\nIncorrect filter, please enter:\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n done\n\n")

while answer == "gray" or answer == f1 or answer == f2 or answer == f3:
	if answer == "gray":
		img = gray()
	elif answer == f1:
		img = filter1()
	elif answer == f2:
		img = filter2()
	elif answer == f3:
		img = filter3()
	else:
		break
	print("Filter \"" + answer + "\" applied...")
	answer = input("\nWhich filter do you want me to apply next?\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n done\n\n")
	while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "done":
		answer = input("\nIncorrect filter, please enter:\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n done\n\n")

print("Combined filter being created...Done")

# Create the combined filter image and saves it to our files
img.save("StudentWork/combinedFilters.jpg")