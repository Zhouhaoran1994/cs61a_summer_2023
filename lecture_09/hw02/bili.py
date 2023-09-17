"""
读取文件成绩计算最高分和最低分
student.txt
101,小白,88
102,小然,87
103,小周,89
104,小王,78
105,小李,92
106,小同,79
"""
import re

def highest_lowest(score_file):
    """
    >>> highest_lowest("student.txt")
    ('105,小李,92', '104,小王,78')
    """
    content = []
    with open(score_file, "r", encoding="utf-8") as f:
        for line in f:
            content.append(line.rstrip())
    highest, lowest = max(content, key=get_score), min(content, key=get_score)
    return highest, lowest

def get_score(score_line):
    pattern = r"(\d+)\,(.+)\,(\d+)"
    score = re.match(pattern, score_line).group(3)
    return int(score)
