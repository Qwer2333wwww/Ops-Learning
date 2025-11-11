import re
from collections import defaultdict

messages = [
    "我想报名！姓名：张三；电话：13577889900；项目：COSPLAY",
    "姓名王五 电话 18812345678 活动 跑酷",
    "【报名】李四-18900011223-摊位：手作饰品",
    "想参加活动！赵六：13399887766，报名项目：街舞",
    "报名|姓名：周七|手机 16622331155|项目 摄影",
    "名字：钱八；手机号：abc123；项目：魔术",  # 无效
    "报名 填写信息：姓名=孙九，电话=15566778899，参与：汉服巡游",
    "刘十 · 13155667788 · 节目：小品表演",
    "我是吴一一，电话 19922334455 ，节目 想报名 合唱",  # ？？？？？
    "姓名：郑十二；学号不需要；手机号：18811223344；项目：绘画",
    "报名 姓名十三 电话 17799887766 活动 器乐独奏",  # ？？？？？？
    "活动申请-何十四-13955667788-报名-话剧",
    "姓名：施十五；手机：16634561234；参与项目：电竞赛",
    "【社团招新】 姓名：贺十六； 18511112222； 加入 社团 摄影",
    "我要报名！姓名十七 手机号 13311112222 活动 街舞",  # ？？？？？
]

# 百家姓
SURNAMES = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍郤璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公'


def msg_process(message):
    # 提取电话
    phone_match = re.search(r'1\d{10}', message)
    if phone_match:
        phone = phone_match.group()
    else:
        phone = None

    # 提取姓名
    name_matches = re.findall(r'[\u4e00-\u9fa5]{2,4}', message)
    name = None
    for match in name_matches:
        if match[0] in SURNAMES:
            name = match
            break

    # 特判：处理"我是XXX"格式
    if not name:
        is_match = re.search(r'我是([\u4e00-\u9fa5]{2,4})', message)
        if is_match:
            potential_name = is_match.group(1)
            # if potential_name[0] in SURNAMES:
            name = potential_name

    # 特判：处理"姓名XXX"格式
    if not name:
        name_keyword_match = re.search(r'姓名([\u4e00-\u9fa5]{2,4})[\s|：:\-；;，,]', message)
        if name_keyword_match:
            potential_name = name_keyword_match.group(1)
            # if potential_name[0] in SURNAMES:
            name = potential_name

    # 提取项目
    parts = re.split(r'[：:\-|；;，,\s]+', message)
    project = None
    for part in reversed(parts):
        clean_part = re.sub(r'[^\u4e00-\u9fa5a-zA-Z]', '', part)  # 洗掉分隔符
        if clean_part and len(clean_part) > 1:
            project = clean_part
            break

    return (name, phone, project)


def message_generator(messages):
    for msg in messages:
        yield msg_process(msg)


# 按项目分组
projects = defaultdict(list)

# print("短信处理后: ")
# print(f"{'序号':<4} {'姓名':<10} {'电话':<15} {'项目':<20}")

for index, (name, phone, project) in enumerate(message_generator(messages), 1):
    if name:
        final_name = name
    else:
        final_name = "未知姓名"

    if phone:
        final_phone = phone
    else:
        final_phone = "未知电话"

    if project:
        final_project = project
    else:
        final_project = "未知项目"

    # print(f"{index:<4} {final_name:<10} {final_phone:<15} {final_project:<20}")

    # 分组
    if not name or not phone or not project:
        projects[final_project].append((final_name, "信息错误"))
    else:
        projects[project].append((name, phone))

# print("按项目分组:  ")
# result_dict = {}
# for project in sorted(projects.keys()):
#     members = projects[project]
#     result_dict[project] = members
# print(result_dict)

print("\n各项目报名人数: ")
for project, members in projects.items():
    valid_count = sum(1 for _, phone in members if phone != "信息错误")
    print(f"{project:<15} 总计: {len(members)}人 (有效报名: {valid_count}人)")

print("\n报名人数最多的前3个项目: ")
# 按有效人数排序
top_projects = sorted(projects.items(), key=lambda x: sum(1 for _, phone in x[1] if phone != "信息错误"), reverse=True)
for rank, (project, members) in enumerate(top_projects[:3], 1):
    valid_count = sum(1 for _, phone in members if phone != "信息错误")
    print(f"\n{rank}. {project} - {valid_count}人")
    for name, phone in members:
        print(f"    {name!r}, {phone!r}")