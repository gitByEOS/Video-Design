# Video Design 技能介绍视频设计

## 元素定义

| 代号 | 实际内容 | 描述 |
|------|---------|------|
| LOGO | HyperFrames Logo | 蓝白渐变图标 + 文字 |
| TITLE | "Video Design" 标题 | 大号蓝色粗体文字 |
| SUBTITLE | 副标题说明 | 白色/浅灰色小字 |
| HERO | 主视觉区 | 蓝色渐变背景 + 装饰元素 |
| CARD_STATIC | 静态布局卡片 | 文档图标 + "阶段一" 标签 + 示意文字 |
| CARD_GANTT | 甘特图卡片 | 柱状图图标 + "阶段二" 标签 + 示意条 |
| CARD_CODE | 代码动画卡片 | 代码图标 + "阶段三" 标签 + 示意代码 |
| CARD_FINAL | 整合交付卡片 | 播放图标 + "阶段四" 标签 + 示意按钮 |
| STEP_NUM | 步骤编号 | 圆形编号标签 1-4 |
| FLOW_ARROW | 流程箭头 | 连接四个阶段的箭头 |
| PROGRESS | 进度条 | 蓝色渐变进度条 |
| ICON_SPADE | 铲子图标 | 代表"设计/构建" |
| ICON_CLOCK | 时钟图标 | 代表"时间线" |
| ICON_CODE | 代码图标 | 代表"代码实现" |
| ICON_PLAY | 播放图标 | 代表"最终交付" |
| SLOGAN | "让视频创作像写文档一样简单" | 结尾标语 |
| CTA | "开始使用 /video-design" | 渐变按钮 |
| BG_BLUE | 蓝色背景 | 蓝白渐变底色 |
| PARTICLES | 装饰粒子 | 漂浮的蓝色小圆点 |

## 分幕动态设计

### 第一幕：开场标题
**时间范围**：0.0s - 20.0s
**元素清单**：BG_BLUE, PARTICLES, LOGO, TITLE, SUBTITLE

**关键帧**：
- 0.0s BG_BLUE 蓝白渐变背景淡入
- 0.5s PARTICLES 粒子从屏幕边缘浮现
- 1.5s LOGO 图标从中心缩放入场（弹性效果）
- 2.5s "HyperFrames" 文字从下方滑入
- 3.5s TITLE "Video Design" 逐字打字出现
- 5.0s SUBTITLE 副标题淡入
- 15.0s 粒子持续漂浮，LOGO 轻微呼吸光效
- 19.0s 整体保持，准备过渡到下一幕

### 第二幕：阶段一 - 静态布局
**时间范围**：20.0s - 40.0s
**元素清单**：BG_BLUE, STEP_NUM(1), ICON_SPADE, CARD_STATIC, TITLE(小)

**关键帧**：
- 0.0s（相对 20s）第一幕内容向左滑出淡出
- 0.5s STEP_NUM 编号"1"弹跳入场
- 1.0s ICON_SPADE 铲子图标旋转出现
- 2.0s "阶段一 静态布局设计" 文字从左侧滑入
- 3.0s CARD_STATIC 卡片从右侧滑入
- 4.5s 卡片内三条列表项依次出现
- 15.0s 卡片轻微脉冲光效
- 19.0s 准备过渡

### 第三幕：阶段二 - 甘特时间线
**时间范围**：40.0s - 60.0s
**元素清单**：BG_BLUE, STEP_NUM(2), ICON_CLOCK, CARD_GANTT, TITLE(小), PROGRESS

**关键帧**：
- 0.0s（相对 40s）第二幕内容向左滑出淡出
- 0.5s STEP_NUM 编号"2"弹跳入场
- 1.0s ICON_CLOCK 时钟图标旋转出现
- 2.0s "阶段二 动态时间线设计" 文字从左侧滑入
- 3.0s CARD_GANTT 卡片从右侧滑入
- 4.0s 第一条甘特条 "入场动画" 从左向右绘制
- 5.0s 第二条 "内容展示" 绘制
- 6.0s 第三条 "过渡转场" 绘制
- 15.0s 甘特条整体微微呼吸光效
- 19.0s 准备过渡

### 第四幕：阶段三 - 代码实现
**时间范围**：60.0s - 80.0s
**元素清单**：BG_BLUE, STEP_NUM(3), ICON_CODE, CARD_CODE, TITLE(小)

**关键帧**：
- 0.0s（相对 60s）第三幕内容向左滑出淡出
- 0.5s STEP_NUM 编号"3"弹跳入场
- 1.0s ICON_CODE 代码图标旋转出现
- 2.0s "阶段三 动画代码实现" 文字从左侧滑入
- 3.0s CARD_CODE 卡片从右侧滑入
- 4.0s 代码块逐行打字出现（打字机效果）
- 7.0s 代码关键字高亮闪烁
- 15.0s 卡片轻微脉冲光效
- 19.0s 准备过渡

### 第五幕：阶段四 - 整合交付
**时间范围**：80.0s - 100.0s
**元素清单**：BG_BLUE, STEP_NUM(4), ICON_PLAY, CARD_FINAL, TITLE(小), PROGRESS

**关键帧**：
- 0.0s（相对 80s）第四幕内容向左滑出淡出
- 0.5s STEP_NUM 编号"4"弹跳入场
- 1.0s ICON_PLAY 播放图标旋转出现
- 2.0s "阶段四 整合交付" 文字从左侧滑入
- 3.0s CARD_FINAL 卡片从右侧滑入
- 4.0s "1280×720" 和 "MP4" 徽章依次弹入
- 5.5s 进度条从 0 填充到 100%
- 8.0s 进度条到位后发光
- 15.0s 卡片轻微脉冲光效
- 19.0s 准备过渡

### 第六幕：结尾号召
**时间范围**：100.0s - 120.0s
**元素清单**：BG_BLUE, PARTICLES, LOGO, SLOGAN, CTA

**关键帧**：
- 0.0s（相对 100s）第五幕内容淡出
- 0.5s PARTICLES 粒子从屏幕边缘浮现
- 1.5s LOGO 图标从中心缩放入场
- 2.5s "HyperFrames" 文字从下方滑入
- 3.5s SLOGAN "让视频创作像写文档一样简单" 逐字打字出现
- 6.0s CTA 按钮发光脉冲弹入
- 15.0s 按钮持续呼吸光效，粒子漂浮
- 19.0s 保持至结束

## Mermaid 甘特图

```mermaid
gantt
    title Video Design 技能介绍视频时间线
    dateFormat X
    axisFormat %s

    section 第一幕
    BG_BLUE 背景              :bg1,       0.0, 20.0
    PARTICLES 粒子             :part1,     0.5, 19.5
    LOGO 图标                  :logo1,     1.5, 18.5
    HyperFrames 文字           :text1,     2.5, 17.5
    TITLE 标题                 :title,     3.5, 16.5
    SUBTITLE 副标题            :sub1,      5.0, 15.0

    section 第二幕
    STEP_NUM 编号              :step2,    20.5, 19.5
    ICON 铲子图标              :icon2,    21.0, 19.0
    标题文字                   :text2,    22.0, 18.0
    卡片                       :card2,    23.0, 17.0
    列表项                     :list2,    24.5, 15.5

    section 第三幕
    STEP_NUM 编号              :step3,    40.5, 19.5
    ICON 时钟图标              :icon3,    41.0, 19.0
    标题文字                   :text3,    42.0, 18.0
    卡片                       :card3,    43.0, 17.0
    甘特条1 入场动画            :bar1,     44.0, 16.0
    甘特条2 内容展示            :bar2,     45.0, 15.0
    甘特条3 过渡转场            :bar3,     46.0, 14.0

    section 第四幕
    STEP_NUM 编号              :step4,    60.5, 19.5
    ICON 代码图标              :icon4,    61.0, 19.0
    标题文字                   :text4,    62.0, 18.0
    卡片                       :card4,    63.0, 17.0
    代码块                     :code4,    64.0, 16.0

    section 第五幕
    STEP_NUM 编号              :step5,    80.5, 19.5
    ICON 播放图标              :icon5,    81.0, 19.0
    标题文字                   :text5,    82.0, 18.0
    卡片                       :card5,    83.0, 17.0
    徽章                       :badge5,   84.0, 16.0
    进度条                     :prog5,    85.5, 14.5

    section 第六幕
    PARTICLES 粒子             :part6,   100.5, 19.5
    LOGO 图标                  :logo6,   101.5, 18.5
    HyperFrames 文字           :text6,   102.5, 17.5
    SLOGAN 标语                :slog6,   103.5, 16.5
    CTA 按钮                   :cta6,    106.0, 14.0
```

---
*阶段二：动态时间线设计完成*
