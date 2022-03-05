from PIL import Image

mask_img = Image.open('/home/oben-m/Images/mask.png')
print(mask_img.size)
puzzle = Image.open('/home/oben-m/Images/word_matrix.png')
print(puzzle.size)

mask_img = mask_img.resize(puzzle.size)
print(mask_img.size)
mask_img.putalpha(220)
puzzle.paste(mask_img, box=(0,0), mask=mask_img)
puzzle.show()
