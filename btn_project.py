from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🙎🏻‍♂️ admin", url="https://t.me/xudoybergan0v"),
         InlineKeyboardButton(text="☑️ qatnashish", callback_data="start_qatnashish")]
    ]
)


jamoalar = ["🇪🇸 Barcelona", "🇪🇸 Real Madrid", "⛵️ Man City", "🔴 Liverpool", "🇫🇷 Paris SG",
    "👹 Man United", "🟣 Chelsea", "🇩🇪 Bavariya"]


go = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 orqaga", callback_data="go_orqaga"),
         InlineKeyboardButton(text="🎮 boshlash", callback_data="go_boshlash")]
    ]
)


komputer = ["👈 chap", "o`rta 👊", "o`ng 👉"]
variantlar = InlineKeyboardBuilder()
for komp in komputer:
    variantlar.add(InlineKeyboardButton(text=komp, callback_data=f"pen_{komp}"))
variantlar.adjust(3)


final = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔙 bosh menu", callback_data="final_bosh"),
         InlineKeyboardButton(text="🏆 final", callback_data="final_final")]
    ]
) 


