def zippy(s1, s2):
    # find the shortest list
    if len(s1) < len(s2):
        short, long = s1, s2
    else:
        short, long = s2, s1

    new = []
    for i in range(len(short)):
        new.append([short[i], long[i]])

    return new