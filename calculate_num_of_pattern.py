'''
각 패턴별로 나온 폴더에서 각 패턴별로 몇개의 이미지가 수집되었는지 알려주는 script입니다.
각 패턴의 개수를 조절하기위해서는 pattern_dict_sort[:x] 의 x값을 조절하세요. 상위 x개의 패턴을 출력해줍니다.
이 파일을 패턴들이 모아져 있는 집합을 모든 폴더(예)2018-nasdaq-top100 과 같은 위치에 두세요. random_select_item.py와 같은 위치에 있어야 합니다.
아니면 os.getcwd()위치에 경로를 조작하세요.
'''
import os
import random
import sys

def run(folder_name):
    base_path = os.getcwd() + f"/{folder_name}"
    pattern_list = os.listdir(base_path)
    pattern_dict = {}
    for pattern in pattern_list:
        pattern = os.path.join(base_path, pattern)
        try:
            pattern_dict[pattern.split("/")[-1]] = len([name for name in os.listdir(pattern) if os.path.isfile(os.path.join(pattern, name))])
        except:
            print("file occured")

    pattern_dict_sort = sorted(pattern_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)\

    # for x in pattern_dict_sort:
    #     print(x[0] , x[1])
    print(pattern_dict_sort[:])
    '''
    pattern_dict = sorted(pattern_dict.values())
    print(pattern_dict)
'''
if __name__ == "__main__":
    folder_name = sys.argv[1]
    run(folder_name)