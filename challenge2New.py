import cv2


def convertToMono(imageIn, threshold):
    width, height = imageIn.shape[:2]

    for i in range(0, height):
        for j in range(0, width):
            color = imageIn[j, i]
            total = 0
            for k in range(0, 2):
                total += color[k]
            average = total/3
            if average > threshold:
                imageIn[j, i] = [255, 255, 255]
            else:
                imageIn[j, i] = [0, 0, 0]
    return imageIn

def improvedQuality(imageIQ):
    width, height = imageIQ.shape[:2]
    average = 0
    count = 0
    for i in range(0, height):
        for j in range(0, width):
            color = imageIQ[j, i]
            total = 0
            for k in range(0, 2):
                total += color[k]
            average += total/3
            count += 1
    print(average/count)
    return convertToMono(imageIQ, average/count)

images = ['image1','image2','image3','image4']

for s in images:
    image = cv2.imread(s+'.jpg')
    image2 = convertToMono(image.copy(), 128)
    cv2.imwrite(s+'mono.jpg', image2)
    image3 = improvedQuality(image.copy())
    cv2.imwrite(s+'improved.jpg', image3)

cv2.waitKey(0)
cv2.destroyAllWindows()
