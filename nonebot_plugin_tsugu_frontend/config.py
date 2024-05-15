from pydantic import BaseModel
from typing import List, Union, Optional


class Config(BaseModel):
    platform: str = "red"
    """
    用于绑定/获取玩家数据的平台, 一般 QQ 为 red, 其他平台可能需要根据 Koishi 适配器的具体实现来修改
    """

    tsugu_api_timeout: int = 10
    '''
    请求超时时间
    '''

    tsugu_api_proxy: str = ''
    '''
    代理地址
    '''

    tsugu_api_backend_url: str = 'http://tsugubot.com:8080'
    '''
    后端地址
    默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
    '''

    tsugu_api_backend_proxy: bool = True
    '''
    是否使用后端代理
    当设置代理地址后可修改此项以决定是否使用代理。
    默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
    '''

    tsugu_api_userdata_backend_url: str = 'http://tsugubot.com:8080'
    '''
    用户数据后端地址
    默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
    '''

    tsugu_api_userdata_backend_proxy: bool = True
    '''
    是否使用用户数据后端代理
    当设置代理地址后可修改此项以决定是否使用代理。
    默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
    '''

    tsugu_api_use_easy_bg: bool = True
    '''
    是否使用简易背景，使用可在降低背景质量的前提下加快响应速度。
    默认为 True，即使用简易背景。若不使用简易背景，可将此项设置为 False。
    '''

    tsugu_api_compress: bool = True
    '''
    是否压缩返回数据，压缩可减少返回数据大小。
    默认为 True，即压缩返回数据。若不压缩返回数据，可将此项设置为 False。
    '''

    tsugu_prefix: List[str] = ['/', '']
    '''
    命令前缀
    最后一个参数如果不是空字符串，则只有在命令前缀符合时才会触发命令。
    '''

    tsugu_allow_gap_less: bool = True
    '''
    是否允许命令与参数之间没有空格
    '''

    tsugu_get_remote_user_data_max_retry: int = 3
    '''
    获取远程用户数据最大重试次数
    '''

    tsugu_token_name: str = "Tsugu"
    '''
    bandori station token
    '''
    tsugu_bandori_station_token: str = "ZtV4EX2K9Onb"
    '''
    bandori station token
    '''

    tsugu_ban_gacha_simulate_group_data: List = []
    '''
    需要关闭模拟抽卡的群
    '''
