import os
import json

from termcolor import colored
from tqdm import trange
import cv2.cv2 as cv2
import colorama
colorama.init()

WD = os.getcwd()


def define_thresholds():
    good = []
    average = []
    bad = []
    scores = []

    images = len(os.listdir('frames'))
    with open('scores.txt', 'r') as sc:
        for record in sc.readlines():
            scores.append(record.split(',')[1].rstrip('\n'))

    print(colored('Generating thresholds..', 'red'))
    for image in trange(images):
        original = cv2.imread(f'frames/{image}.png')
        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

        if scores[image] == 'good':
            good.append(sharpness)
        elif scores[image] == 'average':
            average.append(sharpness)
        elif scores[image] == 'bad':
            bad.append(sharpness)

    lower_threshold = (max(bad) + min(average)) / 2
    upper_threshold = (max(average) + min(good)) / 2

    with open('thresholds.json', 'w') as fp:
        json.dump({'lower_threshold': lower_threshold, 'upper_threshold': upper_threshold}, fp)

    print(colored('\nThresholds saved to disk.', 'green'))


if __name__ == '__main__':
    define_thresholds()
