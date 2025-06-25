from dataclasses import dataclass
from os import wait
from pathlib import Path


@dataclass
class LineDiff:
    begin: int
    end: int


@dataclass
class ParagraphDiff:
    begin: int | None
    end: int | None
    line_diffs: dict[int, LineDiff]


def diff_file(file_path1: Path, file_path2: Path) -> ParagraphDiff:
    file1 = open(file_path1, "r").readlines()
    file2 = open(file_path2, "r").readlines()
    line_diffs = {}
    start = None
    end = None
    for i, (line1, line2) in enumerate(zip(file1, file2)):
        diff = diff_line(line1, line2)
        if diff is not None and start is None:
            start = i
        if diff is not None:
            line_diffs[i] = diff
            end = i
    if len(file1) != len(file2):
        end = len(file1) - 1 if len(file1) > len(file2) else len(file2) - 1
    return ParagraphDiff(begin=start, end=end, line_diffs=line_diffs)


def diff_line(line1: str, line2: str) -> LineDiff | None:
    start = None
    end = None
    for i, (l1, l2) in enumerate(zip(line1, line2)):
        if l1 != l2 and start is None:
            start = i
        if l1 != l2:
            end = i
    if len(line1) != len(line2):
        end = len(line1) - 1 if line1 > line2 else len(line2) - 1
        if start is None:
            start = len(line2) if line1 > line2 else len(line1)
    if start is None or end is None:
        return None
    return LineDiff(begin=start, end=end)


def main():
    print("Works")
