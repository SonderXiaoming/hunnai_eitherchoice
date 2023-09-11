from io import BytesIO
from nonebot import logger, MessageSegment
from .data_source import get_choice_pic
from hoshino import Service
from hoshino.util import pic2b64
from hoshino.typing import CQEvent, HoshinoBot
from PIL import Image 
command = ["对比", "比较", "锐评", "评价", "如何评价"]
command = command + [i + "一下" for i in command] + [j + "下" for j in command]

help = """让 AI 帮你对比两件事物
        ▶ 指令：对比(下/一下) 要顶的事物 和 要踩的事物
        ▶ 别名：比较、锐评、评价、如何评价
        ▶ 示例
        ▷ 对比 Python 和 JavaScript\n"
        ▷ 锐评一下 C# 和 Java\n"
        ▷ 比较 “下北泽” 和 东京 
        """

sv = Service('AI锐评', enable_on_default=True, visible=True)

@sv.on_prefix(command)
async def ai_comment(bot:HoshinoBot, ev:CQEvent):
    text :str = ev.message.extract_plain_text()
    things = text.split()
    if len(things) < 2:
        await bot.finish(ev, "请提供两个要对比的事物，例如：对比 桥本环奈 内田真礼")

    await bot.send(ev, "请稍等，AI 正在帮你评价...")
    try:
        pic = await get_choice_pic(*things)
    except Exception:
        logger.exception("发生错误")
        logger.error("如果多次发生 Server disconnected 错误，请尝试增加 retry 次数")
        await bot.finish(ev,"发生错误，请检查后台日志")
    await bot.send(ev, MessageSegment.image(pic2b64(Image.open(BytesIO(pic)))))
