def strip_words(self, s):

    start = 0
    while start != len(s):
        if s[start] == ' ':
            start += 1
        else:
            break


    if start != len(s):
        s = s[start: ]
    else:
        return ''

    end = len(s) - 1
    while end >= 0:
        if s[end] == ' ':
            end -= 1
        else:
            break

    if end >= 0:
        s = s[: end + 1]

    return s
