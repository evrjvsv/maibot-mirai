import random
import re

from PIL import Image

from nonebot.typing import T_State
from src.libraries.image import *
from nonebot.log import logger
from random import randint
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.adapters.mirai2 import MessageEvent, Bot, MessageChain, GroupMessage
from nonebot.adapters.mirai2.message import MessageType

command_test = on_command('miecho')


@command_test.handle()
async def _echo(bot: Bot, event: MessageEvent):
    text = event.get_plaintext()
    await bot.send(event, text, at_sender=True)


help = on_command('help')


@help.handle()
async def _(bot: Bot, event: MessageEvent):
    help_str = '''可用命令如下：
/今日舞萌 查看今天的舞萌运势
/XXXmaimaiXXX什么 随机一首歌
/随个[dx/标准][绿黄红紫白]<难度> 随机一首指定条件的乐曲
/查歌<乐曲标题的一部分> 查询符合条件的乐曲
/[绿黄红紫白]id<歌曲编号> 查询乐曲信息或谱面信息
/<歌曲别名>是什么歌 查询乐曲别名对应的乐曲
/定数查歌 <定数>  查询定数对应的乐曲
/定数查歌 <定数下限> <定数上限>
/分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看'''

    await help.send(MessageChain([
        {
            "type": MessageType.IMAGE,
            "base64": f"{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        }
    ]))
    # await help.send(MessageChain([{
    #     "type": "Image",
    #     "data": {
    #         "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
    #     }
    # }]))


# async def _group_poke(bot: Bot, event: Event, state: dict) -> bool:
#     #value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
#     return True
#
#
# poke = on_notice(rule=_group_poke, priority=10, block=True)
#
#
# @poke.handle()
# async def _(bot: Bot, event: Event, state: T_State):
#     if event.__getattribute__('group_id') is None:
#         event.__delattr__('group_id')
#     await poke.send(Message([{
#         "type": "poke",
#         "data": {
#             "qq": f"{event.sender_id}"
#         }
#     }]))

