from configDiffer.diff import LineDiff, ParagraphDiff, diff_file


def test_diffing_file(
    tmp_path,
):
    file1 = tmp_path / "test1.txt"
    file1.write_text("hello")
    file2 = tmp_path / "test2.txt"
    file2.write_text("hello2")
    assert diff_file(file1, file2) == ParagraphDiff(
        begin=0, end=0, line_diffs={0: LineDiff(begin=5, end=5)}
    )
