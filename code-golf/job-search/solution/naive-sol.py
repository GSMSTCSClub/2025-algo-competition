def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    max_len = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
            else:
                dp[i][j] = 0
    return max_len


from time import perf_counter

start = perf_counter()
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
print(perf_counter() - start)
