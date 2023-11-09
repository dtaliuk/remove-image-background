from PIL import Image
from rembg import remove

input_path = '27-01-2021-1.jpg'
output_path = '27-01-2021-1.png'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)
