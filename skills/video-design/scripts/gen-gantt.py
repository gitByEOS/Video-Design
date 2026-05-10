#!/usr/bin/env python3
"""从 Markdown 文件中提取 mermaid gantt 代码，生成纯 CSS 甘特图 HTML"""

import re
import sys

COLORS = ['#7c3aed', '#0089ff', '#238636', '#d29922', '#f85149', '#bc8cff']


def parse_mermaid(text):
    sections = []
    current = None
    max_end = 0
    for line in text.split('\n'):
        line = line.strip()
        if line.startswith('section '):
            current = line[8:]
            sections.append({'name': current, 'items': []})
        elif re.match(r'.*:\s*\w+,', line) and not line.startswith(('title', 'dateFormat', 'axisFormat')):
            m = re.match(r'^(.*?)\s*:\s*\w+,\s*([\d.]+),\s*([\d.]+)$', line)
            if m:
                start = float(m.group(2))
                dur = float(m.group(3))
                end = round(start + dur, 1)
                max_end = max(max_end, end)
                if current:
                    sections[-1]['items'].append({'name': m.group(1).strip(), 'start': start, 'dur': dur, 'end': end})
    total = int(max_end) + (1 if max_end % 1 > 0 else 0)
    return sections, total


def gen_html(sections, total, title="视频时间线"):
    # 每秒最小宽度（像素），确保条形图不会被压缩得太窄
    PX_PER_SEC = 50
    min_width = max(PX_PER_SEC * total, 1200)  # 至少1200px

    axis_items = ''.join(f'<div class="tick" style="left:{t * PX_PER_SEC}px">{t}s</div>' for t in range(total + 1))
    grids = ''.join(f'<div class="grid" style="left:{t * PX_PER_SEC}px"></div>' for t in range(total + 1))

    rows_html = ''
    for si, sec in enumerate(sections):
        c = COLORS[si % len(COLORS)]
        for item in sec['items']:
            left_px = item['start'] * PX_PER_SEC
            width_px = item['dur'] * PX_PER_SEC
            rows_html += f'<div class="row"><div class="rb"><div class="bar" style="left:{left_px}px;width:{width_px}px;background:{c}" data-fulltext="{item["name"]}">{item["name"]}</div></div></div>'

    return f'''<!doctype html>
<html lang="zh">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>视频时间线</title>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:"Noto Sans SC",-apple-system,sans-serif; background:#0d1117; color:#cdd6f4; padding:40px; }}
h1 {{ font-size:28px; margin-bottom:8px; }}
.sub {{ color:#6c7086; font-size:14px; margin-bottom:30px; }}
.gantt {{
  background:#161b22;
  border-radius:12px;
  border:1px solid #21262d;
  padding:0 0 24px;
  position:relative;
  overflow:auto;
  max-height:80vh;
}}
.timeline {{ min-width:{min_width}px; padding:20px 30px 0; }}
.axis {{
  position:sticky;
  top:0;
  height:28px;
  margin-bottom:8px;
  padding-top:20px;
  background:#161b22;
  z-index:10;
}}
.tick {{ position:absolute; top:0; font-size:12px; color:#484f58; transform:translateX(-50%); }}
.tick::after {{ content:""; position:absolute; bottom:-5px; left:50%; width:1px; height:5px; background:#30363d; }}
.row {{ display:flex; align-items:center; padding:3px 0; position:relative; }}
.rb {{ flex:1; position:relative; height:28px; min-width:{min_width - 60}px; }}
.bar {{
  position:absolute; height:24px; border-radius:4px; top:2px;
  display:flex; align-items:center; padding:0 10px; font-size:13px;
  color:#fff; font-weight:600; white-space:nowrap; opacity:.9;
  overflow:hidden; text-overflow:ellipsis; min-width:60px;
  cursor:pointer; transition:all 0.2s;
}}
.bar:hover {{
  opacity:1;
  z-index:100;
  overflow:visible;
}}
.bar:hover::after {{
  content:attr(data-fulltext);
  position:absolute;
  left:0;
  top:0;
  height:24px;
  padding:0 10px;
  background:inherit;
  border-radius:4px;
  display:flex;
  align-items:center;
  white-space:nowrap;
  z-index:101;
  box-shadow:0 4px 12px rgba(0,0,0,0.5);
}}
.grid {{ position:absolute; top:0; width:1px; background:#21262d; pointer-events:none; transform:translateX(-50%); }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="sub">1920×1080 · 30fps · {total}s 总时长</p>
<div class="gantt">
    <div class="timeline">
        <div class="axis">{axis_items}{grids}</div>
        {rows_html}
    </div>
</div>
<script>
(function(){{
  var tl = document.querySelector('.timeline');
  var h = tl.offsetHeight;
  document.querySelectorAll('.grid').forEach(function(el){{ el.style.height = h + 'px'; }});
  new ResizeObserver(function(){{
    var h2 = tl.offsetHeight;
    document.querySelectorAll('.grid').forEach(function(el){{ el.style.height = h2 + 'px'; }});
  }}).observe(tl);
}})();
</script>
</body>
</html>'''


def main():
    if len(sys.argv) < 3:
        print("用法: python3 gen-gantt.py <input.md> <output.html>")
        print("示例: python3 gen-gantt.py time-line.md time-line.html")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    with open(in_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取第一个 mermaid 代码块
    m = re.search(r'```mermaid\n(.*?)```', content, re.DOTALL)
    if not m:
        print("错误: 未在文件中找到 mermaid 代码块")
        sys.exit(1)

    # 提取标题
    title_match = re.search(r'title\s+(.*?)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "视频时间线"

    mermaid = m.group(1)
    sections, total = parse_mermaid(mermaid)

    html = gen_html(sections, total, title)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Total: {total}s, {sum(len(s['items']) for s in sections)} items")
    print(f"Written: {out_path}")


if __name__ == '__main__':
    main()
