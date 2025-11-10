records = [66, 84, 82, 53, 11, 59, 5, 77, 97, 25, 25, 68, 31, 56, 29, 56, 88, 38, 12, 21, 49, 48, 62, 47, 87, 34, 83,
           62, 63, 80]

total_people = sum(records)
average_people = round(total_people / len(records), 1)
max_people = max(records)
max_day_index = records.index(max_people)
days_over_50 = sum(1 for count in records if count > 50)
weekdays = ['一', '二', '三', '四', '五', '六', '日']
max_weekday = weekdays[max_day_index % 7]

#这里以第一天为星期一
print(f"总人数：{total_people}")
print(f"平均人数：{average_people}")
print(f"最高人数：{max_people}人（第{max_day_index + 1}天，星期{max_weekday}）")
print(f"超过50人的天数：{days_over_50}天")
