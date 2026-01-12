from src import dp

from .base import InitMiddleware

dp.message.outer_middleware(InitMiddleware())
dp.pre_checkout_query.outer_middleware(InitMiddleware())
dp.callback_query.outer_middleware(InitMiddleware())