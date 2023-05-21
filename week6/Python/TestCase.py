import random
import copy

def get_test_case(goal_state, moving):
    n = len(goal_state)
    cnt = 0
    x, y = n-1, n-1
    tmp_x, tmp_y = x, y
    
    def is_duplicate_state(state):
        state_tuple = tuple(map(tuple, state))
        return state_tuple in visited_states
    
    visited_states = set()
    
    while cnt < moving:   
        num = random.randint(1, 4)
        if num == 1: # UP
            tmp_x -= 1
        elif num == 2: # DOWN
            tmp_x += 1
        elif num == 3: # LEFT:
            tmp_y -= 1
        else: # RIGHT
            tmp_y += 1
        
        if 0 <= tmp_x <= n-1 and 0 <= tmp_y <= n-1:
            new_state = copy.deepcopy(goal_state)
            new_state[x][y], new_state[tmp_x][tmp_y] = new_state[tmp_x][tmp_y], new_state[x][y]
            if not is_duplicate_state(new_state):
                visited_states.add(tuple(map(tuple, new_state)))
                goal_state = new_state
                x, y = tmp_x, tmp_y
                cnt += 1
            else:
                tmp_x, tmp_y = x, y
                

                
        else:
            tmp_x, tmp_y = x, y
    
    return goal_state

n = 17
goal_state_1 =[  [  1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16,  17],
  [ 18,  19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30,  31,  32,  33,  34],
  [ 35,  36,  37,  38,  39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51],
  [ 52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,  65,  66,  67,  68],
  [ 69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85],
  [ 86,  87,  88,  89,  90,  91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102],
  [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
  [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136],
  [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153],
  [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170],
  [171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187],
  [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204],
  [205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221],
  [222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238],
  [239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255],
  [256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272],
  [273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288,   0]
]


moving = 13

res = []
for i in range(3):
    res.append(sum(get_test_case(goal_state_1, moving), []))

    
for r in res:
    print(r)
    
