欢迎访问GarlicGo的Jupyter笔记本

资源地图:
(【2021B站最好的OpenCV课程推荐】OpenCV从入门到实战 全套课程)[https://www.bilibili.com/video/BV1PV411774y?from=search&seid=15932565624720465096&spm_id_from=333.337.0.0]
(Python教程 - 廖雪峰)[https://www.liaoxuefeng.com/wiki/1016959663602400]

常见问题:
1. 使用cv2展示图片的代码如下所示，最后一句`cv2.waitKey(1)`是用于解决macOS中窗口不关闭的问题，Windows系统可直接删除。
```python
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
```