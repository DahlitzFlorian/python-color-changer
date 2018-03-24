import cv2
import numpy as np
import click


def red_green(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.array([image[i][j][0], image[i][j][2],
                                    image[i][j][1]])

    return image


def green_blue(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.array([image[i][j][1], image[i][j][0],
                                    image[i][j][2]])

    return image


def blue_red(image):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i][j] = np.array([image[i][j][2], image[i][j][1],
                                    image[i][j][0]])

    return image


@click.command()
@click.option("-i", "--image", help="Path to image. Can be a relative path.")
@click.option("-c", "--changer", default="red-green", help="Specify the changer. Can be red-green, green-blue or blue-red")
@click.option("-r", "--result", default="new.jpg", help="Specify the images name.")
def main(image, changer, result):
    img = cv2.imread(image)
    if changer == "red-green":
        new_img = red_green(img)
        cv2.imwrite(result, new_img)
    elif changer == "green-blue":
        new_img = green_blue(img)
        cv2.imwrite(result, new_img)
    elif changer == "blue-red":
        new_img = blue_red(img)
        cv2.imwrite(result, new_img)
    else:
        print("Changer does not exist.")


if __name__ == "__main__":
    main()
