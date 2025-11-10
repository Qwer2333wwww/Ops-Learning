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
    "我是吴一一，电话 19922334455 ，节目 想报名 合唱",
    "姓名：郑十二；学号不需要；手机号：18811223344；项目：绘画",
    "报名 姓名十三 电话 17799887766 活动 器乐独奏",
    "活动申请-何十四-13955667788-报名-话剧",
    "姓名：施十五；手机：16634561234；参与项目：电竞赛",
    "【社团招新】 姓名：贺十六； 18511112222； 加入 社团 摄影",
    "我要报名！姓名十七 手机号 13311112222 活动 街舞",
]


def parse_message(message):
    """
    使用生成器逐条解析短信
    返回: (姓名, 电话, 项目) 或带错误标记的元组
    """
    # 提取姓名（中文2-4字）
    name_pattern = r'(?:姓名|名字|我是)[：:=\s]*([^\d\W]{2,4})(?![^\d\W])'
    name_match = re.search(name_pattern, message)

    # 如果上面没匹配到，尝试匹配开头或特殊分隔的姓名
    if not name_match:
        # 匹配类似 "刘十 ·" 或 "何十四-" 的格式
        name_pattern2 = r'(?:^|[\s【】]|活动申请-)([^\d\W]{2,4})(?=[\s·\-：:，,])'
        name_match = re.search(name_pattern2, message)

    name = name_match.group(1) if name_match else None

    # 提取电话（11位数字）
    phone_pattern = r'(?:电话|手机(?:号)?)[：:=\s]*(\d{11})'
    phone_match = re.search(phone_pattern, message)

    # 如果上面没匹配到，尝试匹配独立的11位数字
    if not phone_match:
        phone_pattern2 = r'(?<![0-9])(\d{11})(?![0-9])'
        phone_match = re.search(phone_pattern2, message)

    phone = phone_match.group(1) if phone_match else None

    # 提取项目（中文/英文，不含数字）
    project_pattern = r'(?:项目|活动|参与|节目|摊位|报名|加入|社团)[：:=\s]*(?:报名)?(?:项目)?[：:=\s]*([a-zA-Z\u4e00-\u9fa5\s]+?)(?=[；;，,。！!、|·\-\s]*(?:$|(?![a-zA-Z\u4e00-\u9fa5])))'
    project_match = re.search(project_pattern, message)

    if project_match:
        project = project_match.group(1).strip()
        # 清理项目名称中的无关词汇
        project = re.sub(r'想|报名|参加|活动|填写信息', '', project).strip()
    else:
        project = None

    # 检查信息完整性
    if not name or not phone or not project:
        return name or "未知", "信息错误", project or "未知项目"

    return name, phone, project


def message_generator(messages):
    """生成器：逐条处理短信"""
    for msg in messages:
        yield parse_message(msg)


# 按项目分组
project_dict = defaultdict(list)

print("=" * 60)
print("解析结果：")
print("=" * 60)

for name, phone, project in message_generator(messages):
    print(f"姓名: {name:6} | 电话: {phone:15} | 项目: {project}")

    if phone == "信息错误":
        project_dict[project].append((name, "信息错误"))
    else:
        project_dict[project].append((name, phone))

# 输出按项目分组的结果
print("\n" + "=" * 60)
print("按项目分组：")
print("=" * 60)
for project, members in sorted(project_dict.items()):
    print(f"\n{project}: {members}")

# 输出每个项目的报名人数
print("\n" + "=" * 60)
print("各项目报名人数统计：")
print("=" * 60)
for project, members in sorted(project_dict.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{project}: {len(members)}人")

# 输出报名人数最多的前3个项目
print("\n" + "=" * 60)
print("报名人数最多的前3个项目：")
print("=" * 60)
top3_projects = sorted(project_dict.items(), key=lambda x: len(x[1]), reverse=True)[:3]
for rank, (project, members) in enumerate(top3_projects, 1):
    print(f"第{rank}名: {project} - {len(members)}人")
    for name, phone in members:
        print(f"  └─ {name}: {phone}")

# 输出最终字典格式
print("\n" + "=" * 60)
print("最终数据字典：")
print("=" * 60)
result_dict = dict(project_dict)
print(result_dict)
