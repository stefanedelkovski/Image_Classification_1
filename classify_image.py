import argparse
import json

from termcolor import colored
import cv2.cv2 as cv2
import colorama
colorama.init()


def classify_image():
    try:
        with open('thresholds.json') as threshold:
            thresholds = json.load(threshold)
    except:
        print('Please run define_thresholds script first.')

    lower_threshold = thresholds['lower_threshold']
    upper_threshold = thresholds['upper_threshold']

    ap = argparse.ArgumentParser()
    ap.add_argument("-i",
                    "--image",
                    required=True,
                    help="Provide full path to the image")
    args = vars(ap.parse_args())

    print(colored('Preprocessing image..', 'red'))

    original = cv2.imread(args['image'])
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

    if sharpness < lower_threshold:
        print('Image quality: ' + colored('Low quality', 'green'))
    elif lower_threshold < sharpness < upper_threshold:
        print('Image quality: ' + colored('Average quality', 'green'))
    elif sharpness > upper_threshold:
        print('Image quality: ' + colored('Good quality', 'green'))


if __name__ == '__main__':
    classify_image()
