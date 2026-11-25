# helpers.py
# 11주차 실습 경계값 테스트(슬라이드 15)에서 쓰는 도우미 함수입니다.
# 테스트 파일 맨 위에 from helpers import 쓰기 를 적고 사용합니다.


def 쓰기(경로, 점수):
    """헤더와 학생 한 명만 있는 시험용 CSV 파일을 만든다."""
    with open(경로, "w", encoding="utf-8") as f:
        f.write(f"name,score\n홍길동,{점수}\n")