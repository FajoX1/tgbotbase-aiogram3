from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text

from src import config

class Banner(Text):
    def __init__(
        self, 
        banner_name: str, 
        when: WhenCondition = None
    ):
        super().__init__(when)
        self.banner_name = banner_name

    async def _render_text(
        self, 
        data: dict, 
        dialog_manager: DialogManager
    ) -> str:
        
        return get_url(
            file_name=self.banner_name,
        )

def get_url(file_name: str):
    return f"{config.BANNERS_URL}/{file_name}"