# 图像 HSV 取色小工具 · HSV Color Inspector

> 显示一张图片，并实时查看鼠标所在像素的 **HSV 值**，用于辅助设定颜色阈值（车道线 / 路标检测调参）。

## 功能

- 用 Tkinter 窗口显示图片
- 鼠标移动时实时显示当前位置像素的 HSV 值
- 帮助确定车道线/颜色分割所需的 HSV 上下阈值

## 运行环境

```bash
pip install opencv-python numpy Pillow
```

（`tkinter` 为 Python 标准库）

## 运行方法

1. 准备一张图片（默认读取同目录下的 `lane.jpg`，可在脚本中修改 `image_path`）；
2. 运行：

```bash
python showHSV.py
```

## 目录结构

```
.
├── showHSV.py   # HSV 取色工具
├── lane.jpg     # 示例图片（可选）
└── README.md
```

## 说明

- 本项目为《人工智能编程实训》课程实训作业，作为车道线检测的辅助调参工具。
- `main.py` 为空格占位文件。
