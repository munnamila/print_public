import cv2
import numpy as np
import glob
from tqdm import tqdm
import os

def process_one_dir(dir_name, save_dir):

    print('Process start: %s' % dir_name)

    temp_list = []

    imgs = sorted(glob.glob(dir_name + '/*.jpg'))

    for i in tqdm(range(len(imgs))):

        img = cv2.imread(imgs[i], 0)
        img = cv2.resize(img, (360, 270))

        temp_list.append(img)

    temp_list = np.array(temp_list)

    np.save(save_dir + '/sm.npy', temp_list)

def main(src, tgt):

    dirs = sorted(glob.glob(src + '/*'))

    for i in dirs:

        save_dir = tgt + '/' + i.split('/')[-1]

        if os.path.exists(save_dir):
            continue
        else:
            os.mkdir(save_dir)
            print('mkdir: %s' % save_dir)

        process_one_dir(i, save_dir)

if __name__ == '__main__':
    # termination criteria

    dir_name = '/media/ilcs/5014243614242188/01_SALIENCYMAP_nagase/00_VOD5018464160'
    save_dir = '/media/ilcs/5014243614242188/07_sm_npy/00_VOD5018464160'

    process_one_dir(dir_name, save_dir)
