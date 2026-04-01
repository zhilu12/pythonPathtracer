from tqdm import tqdm

def main():
    imgWidth = 256
    imgHeight = 256

    print("P3")
    print(imgWidth, imgHeight)
    print("255")

    for j in tqdm(range(imgHeight)):
        for i in (range(imgWidth)):
            r = float(i) /(imgWidth-1)
            g = float(j) /(imgHeight-1)
            b = 0.0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(ir, ig, ib)


main()