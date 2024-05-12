from pydantic import BaseModel


class Config(BaseModel):
    tsugu_backend: str = "http://tsugubot.com:8080"
    """Tsugu 后端地址"""
    tsugu_user_data_backend: str = "http://tsugubot.com:8080"
    """Tsugu 用户数据后端地址"""
    tsugu_backend_use_proxy: bool = False
    """是否使用代理访问 Tsugu 后端"""
    tsugu_user_data_backend_use_proxy: bool = False
    """是否使用代理访问 Tsugu 用户数据后端"""
    tsugu_submit_car_number_use_proxy: bool = False
    """是否使用代理提交车牌号"""
    tsugu_verify_player_bind_use_proxy: bool = False
    """是否使用代理验证玩家绑定, 取决于对 Bestdori 的访问性"""
    tsugu_proxy_url: str = "http://localhost:7890"
    """代理地址"""
    tsugu_token_name: str = "Tsugu"
    """车站 Token 名称"""
    tsugu_bandori_station_token: str = "ZtV4EX2K9Onb"
    """车站 Token"""

    tsugu_use_easy_bg: bool = True
    """是否使用简易背景"""
    tsugu_compress: bool = True
    """是否压缩图片"""
    tsugu_platform: str = "red"
    """用于绑定/获取玩家数据的平台, 一般 QQ 为 red, 其他平台可能需要根据 Koishi 适配器的具体实现来修改"""

    tsugu_ban_gacha_simulate_group_data: list = []
    """禁止模拟抽卡的群 ID"""

    tsugu_car_number_forwarding: bool = True
    """是否启用车牌转发"""
    tsugu_change_main_server: bool = True
    """是否启用更改主服务器"""
    tsugu_switch_car_forwarding: bool = True
    """是否启用切换车牌转发"""
    tsugu_bind_player: bool = True
    """是否启用绑定玩家"""
    tsugu_change_server_list: bool = True
    """是否启用更改服务器列表"""
    tsugu_player_status: bool = True
    """是否启用玩家状态"""
    tsugu_help: bool = True
    """是否启用帮助"""
