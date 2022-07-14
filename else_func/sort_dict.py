sam_dict = dict()

#key 기준 정렬
con1 = {k: v for k, v in sorted(sam_dict.items(), key=lambda item: item[0])}

#value 기준 정렬
con2 = {k: v for k, v in sorted(sam_dict.items(), key=lambda item: item[1])}