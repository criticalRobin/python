def clonewars(katas_per_day):
    total_clones = 1
    total_katas = katas_per_day

    for day in range(1, katas_per_day):
        total_clones *= 2
        total_katas += total_clones * (katas_per_day - day)
    return [total_clones, total_katas]

print(clonewars(5))