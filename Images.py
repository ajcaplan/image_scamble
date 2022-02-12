from PIL import Image
from tqdm import tqdm

def encrypt(file, key):
    img = Image.open(file)
    pixels = img.load() # create the pixel map
    key = [ord(i) for i in key]
    
    unique = 0
    for j in tqdm(range(img.size[1])): # for every pixel:
        for i in range(img.size[0]):
            new = []
            for t in range(0,3):
                tmp = pixels[i,j][t] + key[unique]**2
                while tmp > 255:
                    tmp -= 256
                new.append(tmp)
            pixels[i,j] = (new[0], new[1], new[2])
        unique += 1
        if unique == len(key):
            unique = 0
                
    unique = 0
    for i in tqdm(range(img.size[0])): # for every pixel:
        for j in range(img.size[1]):
            new = []
            for t in range(0,3):
                tmp = pixels[i,j][t] + key[unique]**2
                while tmp > 255:
                    tmp -= 256
                new.append(tmp)
            pixels[i,j] = (new[0], new[1], new[2])
        unique += 1
        if unique == len(key):
            unique = 0     
    img.save(file+"_out.png")

def decrypt(file, key):
    img = Image.open(file)
    pixels = img.load() # create the pixel map
    key = [ord(i) for i in key]
    
    unique = 0
    for j in tqdm(range(img.size[1])): # for every pixel:
        for i in range(img.size[0]):
            new = []
            for t in range(0,3):
                tmp = pixels[i,j][t] - key[unique]**2
                while tmp < 0:
                    tmp += 256
                new.append(tmp)
            pixels[i,j] = (new[0], new[1], new[2])
        unique += 1
        if unique == len(key):
            unique = 0  
    
    unique = 0
    for i in tqdm(range(img.size[0])): # for every pixel:
        for j in range(img.size[1]):
            new = []
            for t in range(0,3):
                tmp = pixels[i,j][t] - key[unique]**2
                while tmp < 0:
                    tmp += 256
                new.append(tmp)            
            pixels[i,j] = (new[0], new[1], new[2])
        unique += 1
        if unique == len(key):
            unique = 0
    img.save(file + "_fresh.png")

key = "anyone who is not shocked by quantum theory has not understood it"
encrypt("test.jpg", key)
decrypt("test.jpg_out.png", key)
