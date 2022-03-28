<div align="center">
  <img alt="Arco Design Logo" width="200" src="https://octodex.github.com/images/hula_loop_octodex03.gif"/>
</div>
<div align="center">
  <h1>✨ 欢迎访问GarlicGo的Jupyter笔记本！</h1>
</div>

<div align="center">

[English](./README.en-US.md) | 简体中文

</div>

维护：周新宇
开发环境：VS Code、Python 3.9.7
支持语言：Python ES6


学习资源:
- [【2021B站最好的OpenCV课程推荐】OpenCV从入门到实战 全套课程](https://www.bilibili.com/video/BV1PV411774y?from=search&seid=15932565624720465096&spm_id_from=333.337.0.0)
- [Python教程 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400)

Tips:
1. 使用cv2展示图片的代码如下所示，最后一句`cv2.waitKey(1)`是用于解决macOS中窗口不关闭的问题，Windows系统可直接删除。
```python
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
```