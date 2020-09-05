from game import Game

def main():
    q = Game()
    q.start()
    while q.status == 1:
        for i in range(len(q.players)):
            if q.players[i] is None:
                continue
            print(i) # 玩家序号
            print(q.players[i].inCards) # 手牌
            hello = input("Enter 'd' to pop a card:")
            if q.players[i].inCards != []:  # 确保没有手牌了但打出去的牌还没被收走的玩家还有按铃的机会
                q.popCard(q.players[i])
            print(q.players[i].inCards)
            print(q.players[i].outCards)
            print(q.fruitNum)
            hi = input("Enter number to ring:") # 为了测试方便，输入玩家序号以表示该玩家按了铃
            if hi != 'r': # 按r表示没人按铃
                q.checkRing()
                if q.ring == 0:
                    q.punish(q.players[int(hi)])
                else:
                    q.reward(q.players[int(hi)])
            print(q.deskCard)
            for m in range(len(q.players)):
                q.checkSituation(q.players[m])
                if q.status != 1:
                    break
            print("Status: ", q.status)
            if q.status != 1:
                break

if __name__ == "__main__":
    main()