import numpy as np

data = np.zeros([10, 10], dtype=int)
data[2, 3:6] = 1
data[1:5, 6] = 1

print(data)


def get_context(data, pos):
    tep_replace_num = data[pos]
    data[pos] = 1

    horizontal = data[pos[0], np.where(pos[1] - 4 >= 0, pos[1] - 4, 0):pos[1] + 5]
    vertical = data[np.where(pos[0] - 4 >= 0, pos[0] - 4, 0):pos[0] + 5, pos[1]]
    print('horizontal', horizontal)
    print('vertical', vertical)

    diagonal_down_start = min(pos)
    if diagonal_down_start < 4:
        diagonal_down_start = np.array(pos) - diagonal_down_start
    else:
        diagonal_down_start = np.array(pos) - 4
    diagonal_down_end = min(np.array(data.shape) - np.array(pos))
    if diagonal_down_end < 4:
        diagonal_down_end = np.array(pos) + diagonal_down_end
    else:
        diagonal_down_end = np.array(pos) + 4
    diagonal_down = [data[tuple(diagonal_down_start + i)] for i in range(min(diagonal_down_end - diagonal_down_start))]
    print('diagonal_down', diagonal_down)

    diagonal_up_start = min(data.shape[0] - pos[0], pos[1])
    if diagonal_up_start > 4:
        diagonal_up_start = np.array([pos[0] + 4, pos[1] - 4])
    else:
        diagonal_up_start = np.array([pos[0] + diagonal_up_start, pos[1] - diagonal_up_start])
    diagonal_up_end = min(pos[0], data.shape[1] - pos[1])
    if diagonal_up_end > 4:
        diagonal_up_end = np.array([pos[0] - 4, pos[1] + 4])
    else:
        diagonal_up_end = [pos[0] - diagonal_up_end, pos[1] + diagonal_up_end]
    diagonal_up = [data[tuple([diagonal_up_start[0] - i, diagonal_up_start[1] + i])] for i in
                   range(max(diagonal_up_end - diagonal_up_start))]
    print('diagonal_up', diagonal_up)
    # data[pos] = tep_replace_num
    return [horizontal, vertical, diagonal_down, diagonal_up]


def max_length(context, num=1):
    result = 0
    now_max = 0
    k = num
    for i in context:
        if k == i:
            now_max += 1
        else:
            now_max = 0
        if result < now_max:
            result = now_max
    return result


context = get_context(data, pos=(2, 7))

for i in context:
    res = max_length(i)
    print(i, res, np.where(res >= 5, True, False))
