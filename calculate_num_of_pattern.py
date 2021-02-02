'''
각 패턴별로 나온 폴더에서 각 패턴별로 몇개의 이미지가 수집되었는지 알려주는 script입니다.
각 패턴의 개수를 조절하기위해서는 pattern_dict_sort[:x] 의 x값을 조절하세요. 상위 x개의 패턴을 출력해줍니다.
이 파일을 각 패턴의 사진들이 모아져 있는 폴더들의 집합과 동일한 레벨에 코드를 옮겨 놓으세요.
아니면 os.getcwd()위치에 경로를 조작하세요.
'''
import os

pattern_list = os.listdir(os.getcwd())
pattern_dict = {}
for pattern in pattern_list:
    try:
        pattern_dict[pattern] = len([name for name in os.listdir(pattern) if os.path.isfile(os.path.join(pattern, name))])
    except:
        print("file occured")

pattern_dict_sort = sorted(pattern_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
print(pattern_dict_sort[:20])
'''
pattern_dict = sorted(pattern_dict.values())
print(pattern_dict)
'''