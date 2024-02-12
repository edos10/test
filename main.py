REQUIRED_CONST = 200
START_CIPHER = 9

def rec(cur_chars: list, pos: int, ans: list) -> None:
    if pos == -1:
        cur_str = ''.join(cur_chars).rstrip('+').rstrip('-')
        if eval(cur_str) == REQUIRED_CONST:
            ans.append(cur_str)
        return
    cur_chars.append(str(pos))
    return rec(cur_chars + ['+'], pos - 1, ans) or rec(cur_chars + ['-'], pos - 1, ans) \
           or rec(cur_chars, pos - 1, ans)


ans = []
rec([], START_CIPHER, ans)
for elem in set(ans):
    print(elem)
