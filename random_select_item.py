import os
import random
import sys
from shutil import copyfile
SAMPLE_NUM = 7000

def run(folder_name):
    base_path = os.getcwd() + f"/{folder_name}/"
    base_path_reduced = os.getcwd() + f'/{folder_name}-reduced/'
    pattern_list = os.listdir(base_path)
    reduced_pattern_list = []

    if not os.path.exists(base_path_reduced):
        os.makedirs(base_path_reduced)

    for pattern in pattern_list:
        pattern_images = os.listdir(os.path.join(base_path, pattern))
        pattern_images_reduced = []
        try:
            pattern_images_reduced = random.sample(pattern_images, SAMPLE_NUM)
            print(len(pattern_images_reduced))
            reduced_pattern_list.append(pattern)
        except:
            print("pattern {0} showed less than {1} images".format(pattern, SAMPLE_NUM))
            continue
        
        src_image_path = base_path + pattern 
        reduced_image_path = base_path_reduced + pattern
        if not os.path.exists(reduced_image_path):
            os.makedirs(reduced_image_path)

        for image in pattern_images_reduced:
            copyfile(os.path.join(src_image_path, image), os.path.join(reduced_image_path, image))

        print("pattern {0} finished".format(pattern))

    print("----------- results --------------")
    print("reduced {0} patterns to {1} paterns".format(len(pattern_list), len(reduced_pattern_list)))
    print("reduced patterns are down below")
    print(reduced_pattern_list)
    print("Number of Each images are {0}".format(SAMPLE_NUM))


if __name__ == "__main__":
    folder_name = sys.argv[1]
    run(folder_name)