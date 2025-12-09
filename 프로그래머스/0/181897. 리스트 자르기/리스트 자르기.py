def solution(n, slicer, num_list):
    match n:
        case 1:
            return num_list[0:slicer[1] + 1]
        case 2:
            return num_list[slicer[0]:]
        case 3:
            return num_list[slicer[0]:slicer[1]+1]
        case 4:
            return num_list[slicer[0]: slicer[1]+1: slicer[2]]