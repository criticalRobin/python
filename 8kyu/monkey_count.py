def monkey_count(num):
    monkeys = []

    for i in range(num):
        monkeys.append(i + 1) 
    
    return monkeys

print(monkey_count(5))