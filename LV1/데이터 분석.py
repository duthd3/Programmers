def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    ext_filter = []
    
    for i in data:
        if ext == "date":
            if i[1] < val_ext:
                ext_filter.append(i)
        elif ext == "code":
            if i[0] < val_ext:
                ext_filter.append(i)
        elif ext == "maximum":
            if i[2] < val_ext:
                ext_filter.append(i)
        elif ext == "remain":
            if i[3] < val_ext:
                ext_filter.append(i)
    if sort_by == "remain":
        answer = sorted(ext_filter, key = lambda x: x[3])
        print(answer)
    elif sort_by == "maximum":
        answer = sorted(ext_filter, key = lambda x: x[2])
    elif sort_by == "date":
        answer = sorted(ext_filter, key = lambda x: x[1])
    else:
        answer = sorted(ext_filter, key = lambda x: x[0])
    return answer
