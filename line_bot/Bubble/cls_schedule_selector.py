import global_variable as gv
from linebot import LineBotApi
from linebot.models import ImagemapSendMessage, ImagemapArea, BaseSize, MessageImagemapAction


line_bot_api = LineBotApi(gv.LINE_CHANNEL.ACCESS_TOKEN)

imagemap_message = ImagemapSendMessage(
    base_url=f"{gv.URL}cls_schedule",
    alt_text="選擇上課時段",
    base_size=BaseSize(height=1160, width=1040),
    actions=[
        MessageImagemapAction(
            text="1-12",
            area=ImagemapArea(x=320, y=307, width=95, height=95)
        ),
        MessageImagemapAction(
            text="1-34",
            area=ImagemapArea(x=320, y=423, width=95, height=95)
        ),
        MessageImagemapAction(
            text="1-56",
            area=ImagemapArea(x=320, y=536, width=95, height=95)
        ),
        MessageImagemapAction(
            text="1-78",
            area=ImagemapArea(x=320, y=650, width=95, height=95)
        ),
        MessageImagemapAction(
            text="1-CD",
            area=ImagemapArea(x=320, y=780, width=95, height=95)
        ),
        MessageImagemapAction(
            text="1-EF",
            area=ImagemapArea(x=320, y=895, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-12",
            area=ImagemapArea(x=435, y=307, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-34",
            area=ImagemapArea(x=435, y=423, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-56",
            area=ImagemapArea(x=435, y=536, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-78",
            area=ImagemapArea(x=435, y=650, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-CD",
            area=ImagemapArea(x=435, y=780, width=95, height=95)
        ),
        MessageImagemapAction(
            text="2-EF",
            area=ImagemapArea(x=435, y=895, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-12",
            area=ImagemapArea(x=553, y=307, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-34",
            area=ImagemapArea(x=553, y=423, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-56",
            area=ImagemapArea(x=553, y=536, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-78",
            area=ImagemapArea(x=553, y=650, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-CD",
            area=ImagemapArea(x=553, y=780, width=95, height=95)
        ),
        MessageImagemapAction(
            text="3-EF",
            area=ImagemapArea(x=553, y=895, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-12",
            area=ImagemapArea(x=670, y=307, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-34",
            area=ImagemapArea(x=670, y=423, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-56",
            area=ImagemapArea(x=670, y=536, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-78",
            area=ImagemapArea(x=670, y=650, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-CD",
            area=ImagemapArea(x=670, y=780, width=95, height=95)
        ),
        MessageImagemapAction(
            text="4-EF",
            area=ImagemapArea(x=670, y=895, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-12",
            area=ImagemapArea(x=790, y=307, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-34",
            area=ImagemapArea(x=790, y=423, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-56",
            area=ImagemapArea(x=790, y=536, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-78",
            area=ImagemapArea(x=790, y=650, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-CD",
            area=ImagemapArea(x=790, y=780, width=95, height=95)
        ),
        MessageImagemapAction(
            text="5-EF",
            area=ImagemapArea(x=790, y=895, width=95, height=95)
        ),

    ]
)
