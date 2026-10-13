import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
# 创建一个窗口
window = tk.Tk()
window.title("Image Viewer")
# 图片路径
image_path = "lane.jpg"
# 打开并显示图片
image = Image.open(image_path)
image.thumbnail((600, 600))
image = ImageTk.PhotoImage(image)
panel = tk.Label(window, image=image)
panel.pack(side="top", padx=10, pady=10)
# 获取图片像素矩阵
img_bgr = cv2.imread(image_path)
# 将BGR空间转换为HSV空间
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
# 创建HSV值显示标签
hsv_label = tk.Label(window, text="HSV: ", font=("Helvetica", 16))
hsv_label.pack(side="bottom", padx=10, pady=10)
# 鼠标移动事件处理函数
def on_mouse_move(event):
   x = int(event.x / panel.winfo_width() * img_bgr.shape[1])
   y = int(event.y / panel.winfo_height() * img_bgr.shape[0])
   # 获取像素的HSV值
   pixel_hsv = img_hsv[y, x]
   # 更新HSV值显示标签
   hsv_label.config(text="HSV: {}".format(pixel_hsv))
# 绑定鼠标移动事件
panel.bind("<Motion>", on_mouse_move)
# 运行窗口主循环
window.mainloop()