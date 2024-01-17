heros = input().split(' -> ')
heros_dict = {
    heros[i]: ' -> '.join(
        [heros[i], heros[i + 1]] if i == 0 else 
        [heros[i - 1], heros[i]] if i == len(heros) - 1 else 
        [heros[i - 1], heros[i], heros[i + 1]]
    ) for i in range(len(heros))
}
n = int(input())
for _ in range(n):
    hero = input()
    print(heros_dict[hero])