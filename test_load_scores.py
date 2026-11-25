import pytest
from load_scores import load_scores

def test_reading_normal_files():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5
    assert ("윤보람", 64) in kept
    assert all(original for _, original, _ in skipped)

def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert ("최,네번", 77) in kept

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")

def test_헤더만_있으면_빈_결과(tmp_path):
    scores_file = tmp_path / "scores.csv"
    scores_file.write_text("name,score\n", encoding="utf-8")

    kept, skipped = load_scores(scores_file)

    assert kept == []
    assert skipped == []

@pytest.mark.parametrize(
    ("score", "expected_kept", "expected_skipped"),
    [
        (0, 1, 0),
        (100, 1, 0),
        (101, 0, 1),
    ],
)
def test_점수_경계값(score, expected_kept, expected_skipped, tmp_path):
    scores_file = tmp_path / "scores.csv"
    scores_file.write_text(f"name,score\n테스트,{score}\n", encoding="utf-8")

    kept, skipped = load_scores(scores_file)

    assert len(kept) == expected_kept
    assert len(skipped) == expected_skipped

