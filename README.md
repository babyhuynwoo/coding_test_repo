# 코딩 테스트 연습 저장소

이 저장소는 코딩 테스트 문제를 연습하고 해결하기 위한 목적으로 만들어졌습니다. 각 문제는 알고리즘 별 별도의 디렉토리에 정리되어 있으며, 각 디렉토리에는 문제 설명, 풀이 코드, 및 관련 자료가 포함되어 있습니다.

## 목차

- [소개](#소개)
- [문제 목록](#문제-목록)
- [설치 및 실행](#설치-및-실행)
- [폴더 구조](#폴더-구조)


## 소개

이 저장소는 다양한 코딩 테스트 플랫폼(예: LeetCode, HackerRank, Programmers 등)에서 제공하는 문제들을 연습하고, 효율적인 풀이 방법을 공유하기 위한 저장소입니다. 


## 문제 목록

- [큰 수의 법칙](/Greedy_Algorithm/big_number_rule/solution.py)
- [숫자 카드 게임](/Greedy_Algorithm/number_card_game/solution.py)
- [1이 될 때까지](/Greedy_Algorithm/until_one/solution.py)


## 설치 및 실행

이 저장소를 클론하고 각 문제의 풀이 코드를 실행하는 방법을 설명합니다.


```bash
# 저장소 클론
git clone https://github.com/babyhuynwoo/coding_test_repo.git


# 프로젝트 디렉토리로 이동
cd greedy_algorithm


# Python 가상 환경 설정 (선택 사항)
python -m venv venv
source venv/bin/activate  # Unix/macOS
venv\Scripts\activate  # Windows


# 필요한 패키지 설치 
pip install -r requirements.txt


# 문제 디렉토리로 이동하여 실행
cd problems/problem1

python solution.py  /  python3 solution.py
```

## 폴더 구조

이 저장소의 폴더 구조는 다음과 같습니다:

- `/Algorithms`: 알고리즘별 디렉토리가 위치하는 곳입니다. 각 디렉토리는 별도의 문제를 포함하고 있습니다.
- `/problem`: 문제의 설명 및 문제의 풀이 코드를 포함하는 디렉토리입니다.
- `/tests`: 문제 풀이에 대한 테스트 결과를 저장하는 디렉토리입니다.

coding-test-repo/
- Algorithms/
  - Greedy_Algorithm/
    - problems/
      - solution.py
      - tests.py
  - Sorting_Algorithm/
    - problems/
      - solution.py
      - tests.py
  - Dynamic_Programming_Algorithm/
    - problems/
      - solution.py
      - tests.py
  - Hashing_Algorithm/
    - problems/
      - solution.py
      - tests.py
  - (추가예정)

- .gitignore
- README.md
- requirements.txt