# 阶段二：动态时间线设计 - 追加内容

---

## 分幕动态设计

### 第一幕：Logo 入场
**时间范围**：0.0s - 5.0s
**元素清单**：LOGO, VER, GLOW

**关键帧**：
- 0.0s GLOW 光晕从中心开始扩散
- 0.5s LOGO 从中心缩放入场（弹性效果）
- 1.5s VER "V4" 逐字打字显示，光标闪烁
- 2.5s 粒子从 Logo 向外扩散
- 3.5s 整体轻微放大营造压迫感
- 4.0s 保持至结束

---

### 第二幕：能力展示
**时间范围**：5.0s - 10.0s
**元素清单**：LOGO（顶部小）, CODE, REASON, MULTI

**关键帧**：
- 0.0s LOGO 上滑缩小至顶部
- 0.5s CODE 卡片从左侧滑入，代码片段打字动画
- 1.5s REASON 卡片从底部滑入，推理链展开
- 2.5s MULTI 卡片从右侧滑入，检测框绘制
- 3.5s 三卡片同时高亮发光
- 4.0s 标签依次出现
- 4.5s 粒子在卡片间流动

---

### 第三幕：数据展示
**时间范围**：10.0s - 15.0s
**元素清单**：STATS1, STATS2, STATS3

**关键帧**：
- 0.0s 卡片聚合入场（从四周向中心）
- 0.5s 数值从 0 滚动到目标值
- 1.5s 卡片分裂成三列
- 2.0s 卡片脉冲光效
- 2.5s 粒子爆发
- 3.0s 卡片微微悬浮
- 3.5s 保持至结束

---

### 第四幕：结尾号召
**时间范围**：15.0s - 20.0s
**元素清单**：SLOGAN, CTA

**关键帧**：
- 0.0s 数据卡片淡出
- 0.5s SLOGAN 从下方滑入
- 1.0s SLOGAN 弹性放大定格
- 1.5s CTA 按钮发光脉冲
- 2.0s 粒子从屏幕四周汇聚成 Logo 形状
- 3.0s 底部品牌出现
- 3.5s 整体淡出至品牌色背景

---

## Mermaid 甘特图

```mermaid
gantt
    title DeepSeek V4 发布视频时间线
    dateFormat X
    axisFormat %s

    section 第一幕
    GLOW 光晕扩散      :glow,    0.0, 5.0
    LOGO Logo展示      :logo,    0.5, 4.5
    VER 版本号打字     :ver,     1.5, 3.5
    PART 粒子扩散      :part1,   2.5, 2.5

    section 第二幕
    LOGO 顶部定位      :logomini, 5.0, 5.0
    CODE 代码能力      :code,     5.5, 4.5
    REASON 推理能力    :reason,   6.5, 3.5
    MULTI 多模态       :multi,    7.5, 2.5
    TAG 标签出现       :tag,      8.5, 1.5
    PART 粒子流动      :part2,    9.0, 1.0

    section 第三幕
    STATS 卡片聚合     :stats,    10.0, 1.0
    STATS 数字滚动     :roll,     10.5, 2.0
    STATS 脉冲光效     :pulse,    12.0, 3.0
    PART 粒子爆发      :part3,    12.5, 2.5

    section 第四幕
    SLOGAN 标语        :slogan,   15.5, 4.5
    CTA 按钮           :cta,      16.5, 3.5
    PART 粒子汇聚      :part4,    17.0, 3.0
```

---
