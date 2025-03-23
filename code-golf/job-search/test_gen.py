from os.path import join
import random
import sys
from time import perf_counter


FOLDER_PATH = "code-golf\\job-search\\test-data"
TESTS: list[list | str] = [
    # sample
    '''\
2 2 6 2
Python
kotlin
Fangoogle
Sealin
Pyxotl
Bookface
Dokotl
Pygame''',
    [2, 1, 5, 1],
    [2, 5, 10, 5],
    [5, 5, 10, 5],
    [10, 5, 10, 5],
    [10, 10, 10, 5],
    [10, 10, 10, 10],
    [10, 10, 100, 10],
    [10, 10, 500, 10],
    [10, 10, 500, 10],
    [10, 1, 10_000, 1],
    [5, 1, 20_000, 1],
    [2, 1, 50_000, 1],
    [2, 1, 100_000, 1],
    [2, 1, 100_000, 1],
    [2, 1, 100_000, 1],
]
random.seed(1)


def solution():
    """Generates solution for a testcase. Expects input from std.in and expects output from std.out."""
    def suffix_array(s):
        n = len(s)
        sa = sorted(range(n), key=lambda i: s[i])
        rank = [0] * n
        for i in range(1, n):
            rank[sa[i]] = rank[sa[i - 1]] + (s[sa[i]] != s[sa[i - 1]])
        k = 1
        while k < n:
            sa = sorted(sa, key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
            new_rank = [0] * n
            for i in range(1, n):
                prev = (rank[sa[i - 1]], rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)
                curr = (rank[sa[i]], rank[sa[i] + k] if sa[i] + k < n else -1)
                new_rank[sa[i]] = new_rank[sa[i - 1]] + (prev != curr)
            rank = new_rank
            k *= 2
        return sa


    def lcp_array(s, sa):
        n = len(s)
        lcp = [0] * n
        rank = [0] * n
        for i in range(n):
            rank[sa[i]] = i
        k = 0
        for i in range(n):
            if rank[i] == n - 1:
                k = 0
                continue
            j = sa[rank[i] + 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            lcp[rank[i]] = k
            if k > 0:
                k -= 1
        return lcp


    def lcs(s1, s2):
        s = s1 + '#' + s2
        n = len(s)
        separator_pos = len(s1)
        sa = suffix_array(s)
        lcp = lcp_array(s, sa)
        max_lcp = 0
        for i in range(1, n):
            if (sa[i] < separator_pos and sa[i - 1] > separator_pos) or (sa[i] > separator_pos and sa[i - 1] < separator_pos):
                max_lcp = max(lcp[i - 1], max_lcp)
        return max_lcp


    j, n, l, total = map(int, input().split())
    gerald_skills = []
    for _ in range(total): gerald_skills.append(input())
    companies = {}
    for _ in range(j):
        name = input()
        companies[name] = [input() for _ in range(n)]
    job_scores = []
    for name, skills in companies.items():
        total = 0
        for skill in skills:
            max_lcs = 0
            for g_skill in gerald_skills:
                max_lcs = max(lcs(skill, g_skill), max_lcs)
            total += max_lcs
        # sorting in acending order now sorts lcs in decending order
        job_scores.append([-total, name])
    job_scores.sort()
    print(" ".join(name for _, name in job_scores))


def generate(*args):
    """Generates a test case. Expects an output from std.out."""
    if len(args) == 1 and type(args[0]) == str:
        print(args[0])  # just printout the pre-written testcase
        return
    j, n, l, s = args
    print(j, n, l, s)
    char_set = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    company_names = set()
    for _ in range(s): print("".join(random.choices(char_set, k=l)))
    for _ in range(j):
        # guarentee that company names are unique
        while (company_name := "".join(random.choices(char_set, k=random.randint(3, 30)))) in company_names: 
            continue
        company_names.add(company_name)
        print(company_name)
        for _ in range(n): print("".join(random.choices(char_set, k=l)))


def main():
    stdout = sys.stdout
    times = []
    for test_num, test in enumerate(TESTS):
        input_path = join(FOLDER_PATH, f"{test_num}in.txt")
        output_path = join(FOLDER_PATH, f"{test_num}out.txt")
        with open(input_path, mode='w') as sys.stdout:
            if isinstance(test, str):
                generate(test)
            else:
                generate(*test)
        start_time = perf_counter()
        with open(output_path, mode='w') as sys.stdout:
            with open(input_path) as sys.stdin:
                solution()
        end_time = perf_counter()
        times.append(end_time - start_time)
        assert end_time - start_time < 10, f"It should not take more than 10s to solve the testcase. Time taken was {end_time - start_time}"
    sys.stdout = stdout
    print(times)


if __name__ == "__main__":
    main()
