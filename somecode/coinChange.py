#coding=utf-8


def coinChange(values, money, coinsUsed):
    #values 数组
    #valuesCounts 钱币对应的种类数
    #money  找出来的总钱币数
    #coinsUsed 对应于目前钱币总数i使用的钱币数目

    for cents in range(1, money+1):
        minCoins = cents
        for value in values:
            if value <= cents:
                temp = coinsUsed[cents - value] + 1
                if temp < minCoins:
                    minCoins = temp
        coinsUsed[cents] = minCoins
        print '面值为:{0}的最小硬币数为:{1}'.format(cents, coinsUsed[cents])


if __name__=="__main__":
    values = [25, 21, 10, 5, 1]
    money = 63
    coinsUsed = {1: 0 for i in range(money+1)}
    coinChange(values, money, coinsUsed)
