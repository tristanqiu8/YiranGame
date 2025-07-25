# YiranGame - 儿童教育游戏集合

一个使用 Python 和 Pygame 开发的儿童教育游戏集合。

## 🎮 游戏概览

### 1. **宇宙飞船组装游戏** (`spaceship_assembly.py`)
一个互动教育游戏，教孩子们了解宇宙飞船的组件和组装过程。
- **功能特点**：
  - 组件介绍阶段 - 学习6个不同的飞船部件
  - 分步骤组装动画 - 观看组件按逻辑顺序组装
  - 发射序列 - 观看完成的飞船飞向太空
- **教育价值**：教授基础火箭工程概念和顺序组装思维

### 2. **小鸭子收集游戏** (`duck_game.py`)
一个有趣的收集游戏，玩家控制小鸭子收集食物。
- **功能特点**：
  - 使用方向键控制可爱的小鸭子角色
  - 收集带有不同分值的移动食物
  - 动态计分系统
  - 多彩的池塘环境
- **教育价值**：培养手眼协调能力和基础数学技能

### 3. **数学心形曲线** (`heart_curve.py`)
一个展示形成心形的数学参数方程的动画可视化工具。
- **功能特点**：
  - 使用海龟动画实时绘制曲线
  - 显示参数方程
  - 可交互控制速度和大小
  - 进度跟踪
- **教育价值**：介绍参数方程和数学曲线

### 4. **数学曲线探索器** (`math_curves.py`)
一个探索各种数学曲线的交互式工具。
- **功能特点**：
  - 5种不同的数学曲线（心形、玫瑰、利萨茹、螺旋、无穷）
  - 实时绘制动画
  - 使用数字键切换曲线
  - 数学概念的可视化呈现
- **教育价值**：高级数学概念可视化

## 🚀 安装与设置

### 前置要求
- Python 3.7 或更高版本
- pip（Python 包管理器）

### 所需库
```bash
pip install pygame
```

### 安装步骤
1. 克隆或下载此仓库
2. 进入项目目录：
   ```bash
   cd YiranGame
   ```
3. 安装依赖：
   ```bash
   pip install pygame
   ```

## 🎯 如何运行

### 运行单个游戏
```bash
# 宇宙飞船组装游戏
python spaceship_assembly.py

# 小鸭子收集游戏
python duck_game.py

# 数学心形曲线
python heart_curve.py

# 数学曲线探索器
python math_curves.py
```

## 🎨 游戏控制

### 宇宙飞船组装游戏
- **组件介绍阶段**：
  - `空格键` - 查看下一个组件
  - `A键` - 开始组装
- **组装阶段**：
  - 观看自动组装（无需输入）
  - `L键` - 发射火箭（组装完成后）
- **发射阶段**：
  - `R键` - 重新开始游戏

### 小鸭子收集游戏
- **方向键** - 移动小鸭子（上、下、左、右）
- **ESC键** - 退出游戏

### 数学心形曲线
- `空格键` - 暂停/继续动画
- `R键` - 重置曲线
- `上/下方向键` - 改变曲线大小
- `E键` - 切换方程显示

### 数学曲线探索器
- `1-5数字键` - 选择不同曲线
- `空格键` - 暂停/继续
- `R键` - 重置当前曲线

## 📋 系统要求

- **操作系统**：Windows、macOS 或 Linux
- **Python版本**：3.7+
- **显示器**：建议最低 1400x900 分辨率
- **内存**：最低 512MB RAM
- **显卡**：任何支持基础 2D 渲染的显卡

## 🔧 故障排除

### 常见问题

1. **"找不到pygame"错误**
   - 确保已安装 pygame：`pip install pygame`
   - 尝试：`python -m pip install pygame`

2. **显示问题或黑屏**
   - 更新您的显卡驱动
   - 尝试窗口模式运行（游戏已配置为窗口模式）

3. **声音无法工作**
   - 这些游戏中声音是可选的
   - 检查系统音量设置
   - 如果音频初始化失败，游戏仍会正常运行

4. **性能问题**
   - 关闭其他应用程序
   - 尝试在代码中减小窗口大小
   - 更新 pygame：`pip install --upgrade pygame`

## 📚 教育益处

- **STEM学习**：介绍物理、数学和工程概念
- **问题解决**：通过互动游戏培养逻辑思维
- **视觉学习**：以视觉化、易懂的形式呈现复杂概念
- **运动技能**：像小鸭子收集这样的游戏能提高手眼协调能力

## 🤝 贡献

欢迎通过以下方式贡献：
- 添加新的教育游戏
- 改进现有游戏功能
- 添加音效或音乐
- 翻译成其他语言
- 报告错误或问题

## 📄 许可证

本项目开源，可用于教育目的。

## 👨‍👩‍👧‍👦 目标受众

- 6-12岁儿童
- 寻找互动教学工具的教育工作者
- 希望为孩子提供教育游戏的家长
- 任何对通过游戏示例学习编程感兴趣的人

## 📮 联系方式

如有问题、建议或错误报告，请在项目仓库中创建 issue。

---

**祝学习和游戏愉快！🎮📚**