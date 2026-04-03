from tqdm import tqdm
from color import color
from color import write_color

def main():
    imgWidth = 256
    imgHeight = 256

    print("P3")
    print(imgWidth, imgHeight)
    print("255")

    for j in tqdm(range(imgHeight)):
        for i in (range(imgWidth)):
            pixel_color = color(float(i) / (imgWidth - 1), float(j)/(imgHeight - 1), 0)

            write_color(pixel_color)


main()