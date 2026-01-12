from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text

class Func(Text):
    def __init__(
        self,
        func,
        when: WhenCondition = None,
        **kwargs
    ):
        super().__init__(when=when)
        self.func = func
        self.kwargs = kwargs

    async def _render_text(
        self,
        data: dict,
        dialog_manager: DialogManager
    ) -> str:
        if callable(self.func):
            result = self.func(**self.kwargs)
            if hasattr(result, "__await__"):
                return await result
            return result
        
        return str(self.func)
