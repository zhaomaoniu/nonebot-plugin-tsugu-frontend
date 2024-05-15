import nonebot
import tsugu_async.handler
from nonebot import require
from nonebot import on_message
from nonebot.log import logger
from nonebot.params import Depends
from nonebot.adapters import Event, Bot
from tsugu_async.config import config as tsugu_config
from tsugu_api_async import settings as tsugu_api_config
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")
require("nonebot_plugin_userinfo")

from nonebot_plugin_userinfo import get_user_info
from nonebot_plugin_alconna import UniMessage, Target, Image, Text, At

from .config import Config


if hasattr(nonebot, "get_plugin_config"):
    plugin_config = nonebot.get_plugin_config(Config)
else:
    plugin_config = Config.parse_obj(nonebot.get_driver().config)

if hasattr(plugin_config, "model_dump"):
    plugin_config_dict = plugin_config.model_dump()
else:
    plugin_config_dict = plugin_config.dict()


__plugin_meta__ = PluginMetadata(
    name="BanG Dream! Tsugu Frontend",
    description="基于 tsugu-python-frontend 的 tsugu-bangdream-bot 插件",
    usage="\n".join([f"{k}:\n{v}" for k, v in tsugu_config._help_doc_dict.items()]),
    type="application",
    homepage="https://github.com/zhaomaoniu/nonebot-plugin-tsugu-frontend",
    config=Config,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_userinfo"
    ),
)


# 更新配置对象
for key, value in plugin_config_dict.items():
    if key.startswith("tsugu_api_"):
        attr_name = key.replace("tsugu_api_", "")
        if hasattr(tsugu_api_config, attr_name):
            setattr(tsugu_api_config, attr_name, value)
    elif key.startswith("tsugu_"):
        attr_name = key.replace("tsugu_", "")
        if hasattr(tsugu_config, attr_name):
            setattr(tsugu_config, attr_name, value)


async def get_target(event: Event, bot: Bot):
    return UniMessage.get_target(event, bot)


@on_message(priority=10, block=False).handle()
async def tsugu_handle(
    bot: Bot,
    event: Event,
    target: Target = Depends(get_target),
):
    user_info = await get_user_info(bot, event, event.get_user_id())

    if not user_info:
        logger.warning("Failed to get user info")
        return None

    result = await tsugu_async.handler(
        message=event.get_message().extract_plain_text(),
        user_id=user_info.user_id,
        platform=plugin_config.platform,
        channel_id=(
            target.id if (target.channel or not target.private) else user_info.user_id
        ),
    )

    if not result:
        return None

    message = UniMessage([At("user", user_info.user_id), Text(" ")])

    for content in result:
        if isinstance(content, str):
            message.append(Text(content))
        elif isinstance(content, bytes):
            message.append(Image(raw=content))

    await message.send(target, bot)