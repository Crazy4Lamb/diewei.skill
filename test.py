from diewei_skill import DieweiAgent

def test_diewei():
    agent = DieweiAgent()

    print("===== 测试1：熬夜追剧 =====")
    print(agent.say("我想熬夜追剧"))

    print("\n===== 测试2：总点外卖 =====")
    print(agent.say("我天天点外卖"))

    print("\n===== 测试3：不想考证 =====")
    print(agent.say("我不想考证书"))

    print("\n===== 测试4：想躺平 =====")
    print(agent.say("我就想躺平休息"))

    print("\n===== 测试5：想辞职 =====")
    print(agent.say("我想辞职换工作"))

    print("\n===== 测试6：随机默认爹味 =====")
    print(agent.say("随便说点啥"))

if __name__ == "__main__":
    test_diewei()