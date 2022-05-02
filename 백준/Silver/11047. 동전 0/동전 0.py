N, K = map(int, input().split())
coin_list = list()
coin_num = 0

def get_coinNum():
    global K, coin_num, coin_list

    for i in range(0, N):
        i = int(input())
        coin_list.append(i)

    coin_list.reverse()

    for i in range(0, len(coin_list)):
        coin_num = coin_num + (K//coin_list[i])
        K = K%coin_list[i]
    return coin_num

print(get_coinNum())