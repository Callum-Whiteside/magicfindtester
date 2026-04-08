import random

def testmagicfind(weight, added_weight, stored_xp, required_xp, magic_find, iterations):
    base_base_base_weight = weight
    weight = weight * (1 + min(stored_xp/ required_xp, 2))
    print("weight: ", weight)
    weight = weight * (1 + (magic_find/100))
    # print("weight: ", weight)
    base_chance = (weight / added_weight)
    # print("weight: ", weight)
    print("base chance:", base_chance)
    dropped = False
    lst = []
    largest = 0
    smallest = 100000
    base_base_chance = base_chance
    base_weight = weight
    base_stored_xp = stored_xp
    for i in range(iterations):
        count = 0
        dropped = False
        base_chance = base_base_chance
        weight = base_weight
        stored_xp = base_stored_xp
        while (dropped == False):
            rand_num = random.random()
            count += 1
            if (rand_num <= base_chance or required_xp <= stored_xp):
                dropped = True
                # print("rand", rand_num)
                # print("base", base_chance)
                # if (count > 402 and count < 430):
                    # print("literally next one")
                lst.append(count)
                if (count > largest):
                    largest = count
                elif (count < smallest):
                    smallest = count
            stored_xp += 500
            weight = base_base_base_weight
            weight = weight * (1 + min(stored_xp/ required_xp, 2))
            weight = weight * (1 + (magic_find/100))
            base_chance = weight / added_weight
    # print(lst)
    print("average: ", sum(lst) / len(lst))
    print("largest: ", largest)
    print("smallest: ", smallest)
    count = 0
    for num in lst:
        if (num < 100):
            count += 1
    print("percent chance under: ", count / len(lst))


def main():
    testmagicfind(5, 12127, 0, 1232700, 195, 10000)

if __name__ == '__main__':
    main()
