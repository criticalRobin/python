def stone_pick(arr):
    total_sticks = (arr.count("Wood") * 4) + arr.count("Sticks")
    total_stone = arr.count("Cobblestone")

    if total_stone < 3:
        return 0
    if (total_sticks // 2) < total_stone // 3:
        return total_sticks // 2

    return total_stone // 3


stone_pick(
    ["Wool"] * 21
    + ["Sticks"] * 11
    + ["Stone"] * 31
    + ["Cobblestone"] * 41
    + ["Diamond"] * 8
)
