from aiogram import Bot,Dispatcher,executor,types
from buttons import main_menu,kiyim,oziq_ovqatlar,tehnika,ichimlik,inline_buttons


TOKEN = "7319580615:AAFGdJ--oQU3HqIhruxd6Ayklm03eFSVej0"

PROXY_URL = "http://proxy.server:3128"

bot = Bot(token=TOKEN,parse_mode="HTML",proxy=PROXY_URL)

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_handler(message:types.Message):
    name = message.from_user.first_name
    await message.answer (f"""<b>Assalom alaykum {name}
bizning bo'zimizga hush kelipsiz bu bo'ta narsa olsa bo'ladi.</b>
""",reply_markup=main_menu)
    
@dp.message_handler(text="Kiyimlar")
async def smoking_handler(message:types.Message):
    await message.answer("Kiyimlar",reply_markup=kiyim)

@dp.message_handler(text="krasovka")
async def buts_hendler(message:types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cksutqtennt861in9f10/original.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="futbolka")
async def futbolka_handler(message:types.Message):
    await message.answer_photo(photo='https://olcha.uz/image/400x400/products/2022-12-23/muzhskaya-futbolka-ol524684-belyy-52-185169-0.jpeg',reply_markup=inline_buttons)

@dp.message_handler(text="palto")
async def palto_hendler(message:types.Message):
    await message.answer_photo(photo='https://www.jackmenn.ru/wp-content/uploads/2021/12/kupit-muzhskoe-palto-679x1024.jpg.webp',reply_markup=inline_buttons)

@dp.message_handler(text="shim")
async def shim_handler(message:types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/civjohj6edfostijojqg/original.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="Oziq ovqatlar")
async def menu_handler(message:types.Message):
    await message.answer("Oziq ovqatlar",reply_markup=oziq_ovqatlar)

@dp.message_handler(text="shashli")
async def shashlik_handler(message:types.Message):
    await message.answer_photo(photo='https://butteroverbae.com/wp-content/uploads/2023/07/chicken-shashlik-dry-recipe-card.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="manti")
async def manti_handler(message:types.Message):
    await message.answer_photo(photo='https://static.toiimg.com/thumb/59969178.cms?imgsize=420553&width=800&height=800',reply_markup=inline_buttons)

@dp.message_handler(text="lamon")
async def lamon_handler(message:types.Message):
    await message.answer_photo(photo='https://t4.ftcdn.net/jpg/02/31/48/03/360_F_231480324_BqyB5EmbS8LQg2uPF9SZHLovPQK8MfuO.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="burgae")
async def burgae_handler(message:types.Message):
    await message.answer_photo(photo='https://assets.tmecosys.com/image/upload/t_web767x639/img/recipe/ras/Assets/102cf51c-9220-4278-8b63-2b9611ad275e/Derivates/3831dbe2-352e-4409-a2e2-fc87d11cab0a.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="Tehnika")
async def tehnika_holdler(message:types.Message):
    await message.answer("Tehnika",reply_markup=tehnika)

@dp.message_handler(text="iphone 15 pro Max")
async def iphone_handler(message:types.Message):
    await message.answer_photo(photo='https://olcha.uz/image/400x400/products/supplier/stores/1/2023-09-13/pQIvLk5PqlF9p4Wcobtd6rNjLTBo67eltmac4OoVMgVKa2X13vSXN9cITv77.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="BMW M5")
async def bmw_handler(message:types.Message):
    await message.answer_photo(photo='https://www.motortrend.com/uploads/2022/10/2023-BMW-M5-exterior-8.jpg?fit=around%7C551:374',reply_markup=inline_buttons)

@dp.message_handler(text="Elektro samakat")
async def samakat_handler(message:types.Message):
    await message.answer_photo(photo='https://devel.prom.uz/upload/product_logos/3b/92/3b92725198c26e36fd70a43bfedbadf0.jpeg',reply_markup=inline_buttons)

@dp.message_handler(text="PlayStations 5")  
async def ps_handler(message:types.Message):
    await message.answer_photo(photo='https://m.media-amazon.com/images/I/31JaiPXYI8L._AC_UF1000,1000_QL80_.jpg',reply_markup=inline_buttons)


@dp.message_handler(text="Ichimliklar")
async def drinks_holder(message:types.Message):
    await message.answer("Ichimliklar",reply_markup=ichimlik)

@dp.message_handler(text="Cola")
async def cola_handler(message:types.Message):
    await message.answer_photo(photo='https://rimibaltic-res.cloudinary.com/image/upload/b_white,c_limit,dpr_auto,f_auto,q_auto:low,w_auto/d_ecommerce:backend-fallback.png/MAT_1360568_PCE_LV',reply_markup=inline_buttons)

@dp.message_handler(text="Pepsi")
async def pepsi_handler(message:types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/cia47ib6edfostihhq40/original.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="Fanta")
async def fanta_handler(message:types.Message):
    await message.answer_photo(photo='https://images.uzum.uz/ce8a878v1htd23airm6g/original.jpg',reply_markup=inline_buttons)

@dp.message_handler(text="Sprite")  
async def sprite_handler(message:types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrfEdgbLxi9thdz5-xR4s2uKJMVHMHpGvR4Q&s',reply_markup=inline_buttons)

@dp.message_handler(text="Back")
async def back_holdler(message:types.Message):
    await message.answer("Back",reply_markup=main_menu)


@dp.callback_query_handler(text="bu")
async def get_inline(quare:types.CallbackQuery):
    await quare.message.answer("Harid uchun rahmat tez orada bog'lanamiz")

@dp.callback_query_handler(text="can")
async def get_inline_btn(quare:types.CallbackQuery):
    await quare.message.answer("Harid qabul qilinmadi")

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)