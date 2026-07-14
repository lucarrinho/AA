from sys import stdin
input = stdin.readline
n = int(input())
moedas = list(map(int, input().split()))

dp = [0]*(n+1)
#caso base
dp[0] = 1
#calcula os demais
for i in range(1, n+1):
    #considera as 6 faces do dado
    for moeda in moedas:
        #só soma se o valor não for negativo
        if i - moeda >= 0:
            #recorrência
            dp[i] = (dp[i] + dp[i-face]) % mod
print(dp[n]) #imprime a resposta