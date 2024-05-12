# Nonebot-Plugin-Tsugu-Frontend

## 介绍
基于 tsugu-python-frontend 的 tsugu-bangdream-bot 插件, 用于查询 BanGDream 手游的相关信息

> 使用了 [NoneBot-Plugin-Alconna](https://github.com/nonebot/plugin-alconna) 实现了跨平台

## 功能
请参考 [关于 Tsugu V3.0](https://www.bilibili.com/read/cv18082802)

## 安装方法
<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-tsugu-frontend

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-tsugu-frontend
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-tsugu-frontend
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-tsugu-frontend
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-tsugu-frontend
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_steam_info"]

</details>



## 配置
| 配置项                                | 值                            | 说明                                       |
| ------------------------------------- | ----------------------------- | ------------------------------------------ |
| TSUGU_BACKEND                         | "http://tsugubot.com:8080"    | Tsugu 后端地址                             |
| TSUGU_USER_DATA_BACKEND               | "http://tsugubot.com:8080"    | Tsugu 用户数据后端地址                     |
| TSUGU_BACKEND_USE_PROXY               | False                         | 是否使用代理访问 Tsugu 后端                  |
| TSUGU_USER_DATA_BACKEND_USE_PROXY     | False                         | 是否使用代理访问 Tsugu 用户数据后端          |
| TSUGU_SUBMIT_CAR_NUMBER_USE_PROXY     | False                         | 是否使用代理提交车牌号                     |
| TSUGU_VERIFY_PLAYER_BIND_USE_PROXY    | False                         | 是否使用代理验证玩家绑定，取决于对 Bestdori 的访问性 |
| TSUGU_PROXY_URL                       | "http://localhost:7890"       | 代理地址                                   |
| TSUGU_TOKEN_NAME                      | "Tsugu"                       | 车站 Token 名称                            |
| TSUGU_BANDORI_STATION_TOKEN           | "ZtV4EX2K9Onb"                | 车站 Token                                 |
| TSUGU_USE_EASY_BG                     | True                          | 是否使用简易背景                           |
| TSUGU_COMPRESS                        | True                          | 是否压缩图片                               |
| TSUGU_PLATFORM                        | "red"                         | 用于绑定/获取玩家数据的平台，一般 QQ 为 red，其他平台可能需要根据 Koishi 适配器的具体实现来修改 |
| TSUGU_BAN_GACHA_SIMULATE_GROUP_DATA    | []                            | 禁止模拟抽卡的群 ID                         |
| TSUGU_CAR_NUMBER_FORWARDING           | True                          | 是否启用车牌转发                           |
| TSUGU_CHANGE_MAIN_SERVER              | True                          | 是否启用更改主服务器                       |
| TSUGU_SWITCH_CAR_FORWARDING           | True                          | 是否启用切换车牌转发                       |
| TSUGU_BIND_PLAYER                     | True                          | 是否启用绑定玩家                           |
| TSUGU_CHANGE_SERVER_LIST              | True                          | 是否启用更改服务器列表                     |
| TSUGU_PLAYER_STATUS                   | True                          | 是否启用玩家状态                           |
| TSUGU_HELP                            | True                          | 是否启用帮助                               |


## 鸣谢
- [tsugu-bangdream-bot](https://github.com/Yamamoto-2/tsugu-bangdream-bot) Tsugu 本体
- [tsugu-python-frontend](https://github.com/kumoSleeping/tsugu-python-frontend) Tsugu Python 前端库
- [nonebot-plugin-alconna](https://github.com/nonebot/plugin-alconna) 跨平台支持
- [nonebot-plugin-userinfo](https://github.com/noneplugin/nonebot-plugin-userinfo) 跨平台用户信息获取