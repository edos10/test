def rec(cur_chars: list, pos: int) -> str:
    if pos == -1:
        cur_str = ''.join(cur_chars).rstrip('+').rstrip('-')
        if eval(cur_str) == 200:
            return cur_str
        return None
    cur_chars.append(str(pos))
    return rec(cur_chars + ['+'], pos - 1) or rec(cur_chars + ['-'], pos - 1) or rec(cur_chars, pos - 1)

print(rec([], 9))
