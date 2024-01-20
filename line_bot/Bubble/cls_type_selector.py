import global_variable as gv
from linebot import LineBotApi
from linebot.models import ImagemapSendMessage, ImagemapArea, BaseSize, MessageImagemapAction



line_bot_api = LineBotApi(gv.LINE_CHANNEL.ACCESS_TOKEN)

imagemap_message = ImagemapSendMessage(
    base_url=f"{gv.URL}cls_type",
    alt_text="請選擇課程類別",
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        MessageImagemapAction(
            text="天",
            area=ImagemapArea(x=143, y=235, width=165, height=147)
        ),
        MessageImagemapAction(
            text="人",
            area=ImagemapArea(x=340, y=235, width=165, height=147)
        ),
        MessageImagemapAction(
            text="物",
            area=ImagemapArea(x=535, y=235, width=165, height=147)
        ),
        MessageImagemapAction(
            text="我",
            area=ImagemapArea(x=730, y=235, width=165, height=147)
        ),
        MessageImagemapAction(
            text="宗哲",
            area=ImagemapArea(x=143, y=443, width=165, height=147)
        ),
        MessageImagemapAction(
            text="人哲",
            area=ImagemapArea(x=340, y=443, width=165, height=147)
        ),
        MessageImagemapAction(
            text="公民",
            area=ImagemapArea(x=535, y=443, width=165, height=147)
        ),
        MessageImagemapAction(
            text="歷史",
            area=ImagemapArea(x=730, y=443, width=165, height=147)
        ),
        MessageImagemapAction(
            text="體育",
            area=ImagemapArea(x=143, y=662, width=165, height=147)
        ),
        MessageImagemapAction(
            text="英聽",
            area=ImagemapArea(x=340, y=662, width=165, height=147)
        ),
        MessageImagemapAction(
            text="修辭",
            area=ImagemapArea(x=535, y=662, width=165, height=147)
        ),
        MessageImagemapAction(
            text="軍訓",
            area=ImagemapArea(x=730, y=662, width=165, height=147)
        ),
    ]
)

