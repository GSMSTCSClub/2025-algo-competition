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
