import random

class DieweiAgent:
    def __init__(self, style="classic", level="max"):
        self.style = style
        self.level = level

    def say(self, topic: str) -> str:
        topic = topic.strip().lower()

        templates = self._get_templates(topic)
        if not templates:
            return self._default_diewei()
        return random.choice(templates)

    def _get_templates(self, topic):
        if "熬夜" in topic or "追剧" in topic:
            return [
                "天天熬夜身体能好吗？年轻人别总觉得自己扛得住，等出问题就晚了！我都是为你好！",
                "熬夜最伤身体，你现在不注意，以后毛病全找上来，听我的，早点睡觉！",
                "年轻人要懂得爱惜身体，天天熬夜追剧纯粹是瞎折腾，我吃过的盐比你米多！"
            ]

        elif "外卖" in topic:
            return [
                "外卖全是油盐调料，吃多了对身体没好处，自己做点饭多健康！",
                "别总图省事点外卖，一时是方便，身体搞坏了后悔都来不及！",
                "外面的饭菜不干净，年轻人别糊弄自己，好好吃饭才是正事！"
            ]

        elif "考证" in topic or "证书" in topic:
            return [
                "技多不压身，多考个证总没坏处，现在竞争这么激烈，不多学点怎么行！",
                "趁年轻多学点东西，以后找工作、升职都用得上，我都是为你的将来考虑！",
                "别嫌麻烦，证书就是底气，现在不努力，以后要吃更多苦！"
            ]

        elif "躺平" in topic:
            return [
                "年纪轻轻就想躺平？一点上进心都没有，趁年轻就该多拼一拼！",
                "现在舒服了，以后怎么办？年轻就是要奋斗，老了再想享福！",
                "别总想着歇着，年轻人要有冲劲，不然以后要被社会淘汰！"
            ]

        elif "辞职" in topic or "换工作" in topic:
            return [
                "现在工作多难找，别动不动就想辞职，安稳比什么都重要！",
                "哪家单位都一样，别总这山望着那山高，踏实干比什么都强！",
                "你太年轻太冲动，冲动辞职早晚要吃亏，听我的，稳住！"
            ]

        else:
            return None

    def _default_diewei(self):
        defaults = [
            "你懂个屁，我吃的盐比你吃的米都多，听我的准没错！",
            "年轻人就是太浮躁，心高气傲，早晚要栽跟头！",
            "我都是为你好，你还年轻，很多事不懂，以后就明白了！",
            "别总由着自己性子来，社会不是你家，没人惯着你！"
        ]
        return random.choice(defaults)