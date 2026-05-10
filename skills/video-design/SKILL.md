---
name: video-design
description: 生成 HyperFrames 视频时间线设计文档，并渲染可视化甘特图。
---

# Video Design

## 前置工作

- 需要用户给出一个 HyperFrames 的工作目录
- 如果没有告知用户使用 `hyperframes init` 创建

## 工作流程（四阶段）

### 阶段一：静态布局设计

**目标**：确定每幕视觉元素和布局，供用户在浏览器中确认

**输出目录**：`design/`

1. **生成 design.md（静态版）**
   参考 `reference/design-step1.md` 格式，仅包含静态信息：
   - 元素定义表（代号 → 实际内容描述）
   - 分幕画面设计：
     - 时间范围（如 `0.0s - 5.0s`，默认每幕 5s）
     - **元素清单**：每幕包含哪些元素
     - **最终布局 ASCII 图**：元素位置关系
   - **实现映射表**：composition 文件与幕的对应
   - 阶段一不包含哪些：动态关键帧、动画描述、Mermaid 甘特图

2. **生成静态 compositions**

   | 幕 | 输出文件 | 内容 |
   |----|---------|------|
   | 第一幕 | `design/scene-1.html` | 纯 HTML/CSS，无脚本 |
   | 第二幕 | `design/scene-2.html` | 纯 HTML/CSS，无脚本 |
   | ... | ... | ... |

   要求：
   - 仅 HTML 结构 + CSS 样式
   - 无 `<script>` 标签、无 GSAP、无 timeline
   - 代号替换为实际视觉元素
   - 画布尺寸 1920×1080（或指定分辨率）

3. **生成 preview.html**
   参考 `reference/preview.html`：
   - **布局**：左右分栏
   - **左侧**：各幕 iframe 预览，动态缩放适应容器
   - **右侧**：简化时间条（仅幕名称和时间范围）
   - **阶段标签**：显示"阶段一：静态布局"

**用户确认布局后** → 进入阶段二

---

### 阶段二：动态时间线设计（甘特图）

**目标**：确定动画关键帧和时间线

1. **更新 design.md**
   参考 `reference/design-step2-append.md`：
   - 每幕追加「关键帧列表」
   - 尾部追加「Mermaid 甘特图」
   - `duration` 代表元素存活时间（从入场到退场）
2. **渲染甘特图**
   ```bash
   python3 {skills}/scripts/gen-gantt.py design.md design/time-line.html
   ```

**⏸️ 等待用户确认甘特图**

用户可能需要：调整时长、增减关键帧、修改时机

**确认后** → 阶段三

---

### 阶段三：动画代码实现

**目标**：编写 GSAP timeline 代码

1. **为每幕添加 timeline**

   在每个 `design/scene-N.html` 底部追加：
   ```html
   <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
   <script>
     (function() {
       const tl = gsap.timeline({ paused: true });
       // 按 design.md 关键帧添加动画

       // 5s 后重置（每幕默认时长，preview 中循环预览用）
       tl.call(() => { tl.restart(); }, null, 5.0);

       window.__timelines = window.__timelines || {};
       window.__timelines["scene-N"] = tl;

       tl.play();
     })();
   </script>
   ```

   **注意**：
   - **禁止 `repeat: -1`**：循环统一用末尾 5s `tl.call` 控制
   - **同一元素不写多个 `tl.from()`**：第二个 `from` 会覆盖第一个的初始值导致闪烁
   - **禁止 `Math.random()` / `Date.now()`**：用固定数组替代随机值
   - **动态创建的 DOM 元素**：在 `restart()` 前清空容器，否则 DOM 累积
   - **公共 SVG 元素**(如Logo)：各幕复用同一 SVG 代码，不可缺省节点
   - **父容器不设置初始 opacity: 0**，需要逐个动画的元素各自设置 opacity: 0

**⏸️ 等待用户确认动画效果**

**确认后** → 阶段四

---

### 阶段四：整合交付

**目标**：输出最终可渲染的视频项目

1. **复制文件**
   - `design/scene-*.html` → `compositions/scene-*.html`

2. **生成 index.html**
   ```html
   <div id="main-composition" data-composition-id="main" data-start="0" data-duration="20" data-width="1920" data-height="1080">
     <div data-composition-src="compositions/scene-1.html"
          data-start="0" data-duration="5" data-width="1920" data-height="1080"></div>
     <!-- ... -->
   </div>
   ```

3. **运行检查**
   ```bash
   npm run check
   ```

4. **预览最终效果**
   ```bash
   npm run dev
   ```
   告知用户：可以使用 `npm run dev` 查看最终视频效果

---

## 关键原则

1. **先静后动**：静态布局 → 时间线 → 代码 → 整合
2. **分阶段确认**：每阶段需用户确认后再进入下一阶段
3. **先确认时间线再写代码**：甘特图确认后再生成 timeline
4. **代号替换**：HTML 中应是实际内容
5. **默认时长**：每幕 5s（可调整）
6. **分辨率**：1920×1080（或按项目指定）
7. **确定性**：不使用 `Date.now()`、`Math.random()`

## 文件结构

```
project/
├── design/                  # 阶段一/二/三工作目录
│   ├── design.md          # 阶段一静态 → 阶段二追加动态
│   ├── g       # 阶段一静态预览 → 阶段二甘特图 → 阶段三播放控制
│   ├── time-line.html     # 阶段二生成（甘特图）
│   └── scene-*.html       # 阶段一纯静态 → 阶段三追加动画
├── compositions/          # 阶段四复制至此
│   └── scene-*.html
└── index.html             # 阶段四生成（最终交付）
```
