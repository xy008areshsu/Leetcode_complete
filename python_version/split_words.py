def split_words(self, s):
    s = self.strip_words(s)
    if len(s) == 0:
        return []

    res = []
    start = 0
    end = len(s) - 1
    j = 0

    while start <= end:
        while j <= end and s[j] != ' ':
            j += 1

        if len(s[start : j]) >= 1:
            res.append(s[start : j])

        if j <= end:             # since s is already striped, so there is no leading and trailing spaces, so if j != end, then there must be some more words ahead.
            while s[j] == ' ':   # ignore the spaces between words
                j += 1

        start = j

    return res