# Huannai_Eitherchoice

一个适用hoshinobot的 AI锐评 插件，欢迎提交 isuue 和 request

本插件仅供学习研究使用，插件免费，请勿用于违法商业用途，一切后果自己承担

## 项目地址：

https://github.com/SonderXiaoming/hunnai_eitherchoice

## 说明

```
让 AI 帮你对比两件事物
指令：对比(下/一下) 要顶的事物 和 要踩的事物
别名：比较、锐评、评价、如何评价
示例
对比 桥本环奈 新亘结衣
锐评一下 桥本环奈 内田真礼
比较 桥本环奈 三上悠亚
```

## 简单食用教程：

1. 下载或git clone本插件：

   在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目

   ```
   git clone https://github.com/SonderXiaoming/hunnai_eitherchoice
   ```

2. 在 HoshinoBot\hoshino\config\ `__bot__.py` 文件的 MODULES_ON 加入 'hunnai_eitherchoice'

   然后重启 HoshinoBot

3. 一些功能可自由配置，具体配置内容见下文

在`config.py`下设置：

```
proxy = None                           # 设置代理
either_choice_timeout = 90             # 设置超时
either_choice_retry = 2                # 设置重试次数
either_choice_lang = "zh-CN"           # 网站语言设置
either_choice_allow_public = "true"    # 是否允许AI联网
either_choice_pic_width = 1280         # 生成图片宽度
either_choice_main_font = "sans-serif" # 字体设置
either_choice_code_font = "Victor Mono"# 代码字体设置
```

## 更新日志

1.0.0 好的开始

灵感来自 [nonebot-plugin-eitherchoice](https://github.com/lgc-NB2Dev/nonebot-plugin-eitherchoice)

服务来自 [EitherChoice](https://eitherchoice.com/)