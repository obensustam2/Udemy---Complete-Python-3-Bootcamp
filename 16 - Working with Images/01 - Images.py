from PIL import Image

mac = Image.open('/home/oben-m/Images/example.jpg')
print(type(mac))
# mac.show()
size = mac.size
format = mac.format_description
print(size)
print(format)

# Crop Image
# mac.crop((0, 0, 700, 100)).show()

# Copy and Paste
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
computer = mac.crop((0,y,1993,h))
# computer.show()
# computer.resize((300,300)).show()
# computer.rotate(180).show()
mac.paste(im=computer,box=(0,int(halfway)))
# mac.show()

red = Image.open('/home/oben-m/Images/red_color.jpg')
red.putalpha(244)
red.show()