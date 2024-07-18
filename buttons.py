from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Kiyimlar"),
            KeyboardButton("Oziq ovqatlar"),
        ],
        [
            KeyboardButton("Tehnika"),
            KeyboardButton("Ichimliklar"),
        ],
    ]
,resize_keyboard=True)

kiyim = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton("krasovka"),
        KeyboardButton("futbolka")
    ],
    [
      KeyboardButton("palto"),
      KeyboardButton("shim"),
    ],
    [
        KeyboardButton("Back")
    ]
],resize_keyboard=True)


oziq_ovqatlar = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton("shashli"),
        KeyboardButton("manti")
    ],
    [
      KeyboardButton("lamon"),
      KeyboardButton("burgae"),
    ],
    [
        KeyboardButton("Back")
    ]
],resize_keyboard=True)

tehnika = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton("iphone 15 pro Max"),
        KeyboardButton("BMW M5")
    ],
    [
        KeyboardButton("Elektro samakat"),
        KeyboardButton("PlayStations 5")
    ],
    [
        KeyboardButton("Back")
    ]
    ],resize_keyboard=True)


ichimlik = ReplyKeyboardMarkup(
    keyboard=[
    [
        KeyboardButton("Cola"),
        KeyboardButton("Pepsi")
    ],
    [
        KeyboardButton("Fanta"),
        KeyboardButton("Sprite")
    ],
    [
        KeyboardButton("Back")
    ]
    ],resize_keyboard=True)




inline_buttons = InlineKeyboardMarkup(row_width=2)
inline_btn1 = InlineKeyboardButton("buy",callback_data="bu")
inline_btn2 = InlineKeyboardButton("canect",callback_data="can")
inline_buttons.add(inline_btn1,inline_btn2)