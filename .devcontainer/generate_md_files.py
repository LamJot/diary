import os
from datetime import datetime, timedelta

# Define the number of files and the starting date, 文件数和起始时间自己改
num_files = 342
start_date = datetime(2025, 1, 23)
# os_path = os.path.join('../content/posts')
# Template content with placeholders for title and date
template_content = """---
title: "{date}"
date: {date}
tags:
  - Daily
draft: true
hidden: false
disable_feed: false
---

"""

# Generate files
for i in range(num_files):
    date = start_date + timedelta(days=i)
    date_str = date.strftime('%Y-%m-%d')
    year_month = date.strftime('%Y-%m')
    # output_dir = os.path.join('/workspaces/diary/content/posts', year_month) 
    # posts_folder 的地址是在 codespace 中 博客内容对应的file path，右击 `posts`文件夹 copy path 即可

    # 上面是在github codespace中输出路径的获得方式，我是在本地生成再提交，所以修改了路径
    output_dir = os.path.join('../content/posts', year_month)
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{date_str}.md")
    content = template_content.format(date=date_str)
    with open(filename, 'w') as new_file:
        new_file.write(content)
# print({os_path})
print(f'{num_files} Markdown files generated successfully in their respective directories.')