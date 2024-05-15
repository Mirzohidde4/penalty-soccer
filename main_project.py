import asyncio, logging
from aiogram import Bot, Dispatcher, F,  html
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import CommandStart
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from random import choice
from config_project import TOKEN
from btn_project import *
from states_project import *


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    fullname = message.from_user.full_name
    await message.answer_photo(photo="https://bookmaker-ratings.ru/wp-content/uploads/2017/05/1111-3.jpg",
        caption=f"Assalomu Alaykum {html.bold(fullname)}\nxush kelibsiz 🥳\n\nhttps://t.me/piton_code_bot 👈",
        reply_markup=start)



@dp.callback_query(F.data == "start_qatnashish")
async def start_game(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    clubs = jamoalar.copy()
    verus = choice(clubs)
    clubs.remove(verus)
    final = choice(clubs)
    await state.update_data(
        {
            "final": final,
            "verus": verus
        }
    )
    await call.message.answer_photo(photo="https://bookmaker-ratings.ru/wp-content/uploads/2017/05/1111-3.jpg",
        caption=f"🇪🇺 Yarim final\n\n{verus} - 🙎🏻‍♂️ user",
        reply_markup=go)



@dp.callback_query(F.data.startswith("go_"))
async def Go(call: CallbackQuery, state: FSMContext):
    yonalish = call.data.split("_")
    soz = yonalish[1]
    
    if soz == "orqaga":
        await call.message.delete()
        await call.message.answer_photo(photo="https://bookmaker-ratings.ru/wp-content/uploads/2017/05/1111-3.jpg",
        caption=f"🔝 siz asosiy menyuga qaytdingiz\n\nhttps://t.me/piton_code_bot 👈",
        reply_markup=start)

    elif soz == "boshlash":
        await call.message.delete()
        await state.update_data(
            {
                "user": 0,
                "komputer": 0,
                "user_shot": "",
                "bot_shot": "",
                "user_pen": 0,
                "bot_pen": 0
            }
        )
        data = await state.get_data()
        verus = data.get("verus")
        ushot = data.get("user_shot")
        bshot = data.get("bot_shot")
        await call.message.answer_photo(photo="https://blog.eldorado.ru/storage/publication/Ki2swLj1frKUfFCCq0SO3CF6iGpe3iCl0t5fvW4r.jpeg",
            caption=f"{html.bold("oyin boshlandi")} ⏳\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot}\n{verus} : {bshot}\n\ntopni teping ⚽️",
            reply_markup=variantlar.as_markup())
        await state.set_state(KickPenalty.shot)



@dp.callback_query(F.data.startswith("pen_"), KickPenalty.shot)
async def bir(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    robot = choice(komputer)
    yonalish = call.data.split("_")
    soz = yonalish[1]
    
    data = await state.get_data()
    ushot = data.get("user_shot")
    user = data.get("user")
    penalty = data.get("user_pen")
    verus = data.get("verus")

    if robot == soz:
        await state.update_data(
            {
                "user_shot": ushot + "❌",
                "user_pen": penalty + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        penalty1 = data1.get("user_pen")
        komp = data1.get("komputer")
        user1 = data1.get("user")
        print(penalty1,"\n",user,komp)

        if penalty1 == 4:
            if (komp - user1) >= 2:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥉 siz yutqazdingiz",
                    reply_markup=start) 

            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepPenalty.kep)

        elif penalty1 >= 5:
            if (komp - user1) == 1:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥉 siz yutqazdingiz",
                    reply_markup=start) 

            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepPenalty.kep)    
        
        else:        
            await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                reply_markup=variantlar.as_markup())
            await state.set_state(KeepPenalty.kep)    

    else:
        await state.update_data(
            {
                "user": user + 1,
                "user_shot": ushot + "✅",
                "user_pen": penalty + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        penalty1 = data1.get("user_pen")
        komp = data1.get("komputer")
        user1 = data1.get("user")
        print(penalty1,"\n",user1,komp)

        if penalty1 == 4:
            if (user1 - komp) == 3:
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Goool")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🏆 siz finalga chiqtingiz",
                    reply_markup=final)                      

            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepPenalty.kep)

        elif penalty1 >= 5:    
            if (user1 - komp) == 2:    
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Goool")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🏆 siz finalga chiqtingiz",
                    reply_markup=final)                      

            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepPenalty.kep)
        
        else:
            await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                reply_markup=variantlar.as_markup())
            await state.set_state(KeepPenalty.kep)



@dp.callback_query(F.data.startswith("pen_"), KeepPenalty.kep)
async def bir1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    robot = choice(komputer)
    yonalish = call.data.split("_")
    soz = yonalish[1]

    data = await state.get_data()
    bshot = data.get("bot_shot")
    komp = data.get("komputer")
    pen = data.get("bot_pen")
    verus = data.get("verus")
    
    if robot == soz:
        await state.update_data(
            {
                "bot_shot": bshot + "❌",
                "bot_pen": pen + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        pen1 = data1.get("bot_pen")
        user = data1.get("user")
        komp1 = data1.get("komputer")
        print(pen1,"\n",user,komp)

        if pen1 == 3:
            if (user - komp1) == 3:
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🏆 siz finalga chiqtingiz",
                    reply_markup=final)    
        
            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot) 

        elif pen1 == 4:
            if (user - komp1) == 2:   
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🏆 siz finalga chiqtingiz",
                    reply_markup=final) 
            
            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot) 

        elif pen1 >= 5:
            if user > komp1:
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🏆 siz finalga chiqtingiz",
                    reply_markup=final) 
            
            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot)
        
        else:        
            await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                reply_markup=variantlar.as_markup())
            await state.set_state(KickPenalty.shot)

    else:
        await state.update_data(
            {
                "komputer": komp + 1,
                "bot_shot": bshot + "✅",
                "bot_pen": pen + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        pen1 = data1.get("bot_pen")
        user = data1.get("user")
        komp1 = data1.get("komputer")
        print(pen1,"\n",user,komp1)

        if pen1 == 3:
            if (komp1 - user) == 3:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥉 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot)

        elif pen1 == 4:
            if (komp1 - user) == 2:  
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥉 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot)      

        elif pen1 >= 5:
            if komp1 > user:    
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥉 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickPenalty.shot)    
        
        else:
            await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Yarim-final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                reply_markup=variantlar.as_markup())
            await state.set_state(KickPenalty.shot)



@dp.callback_query(F.data.startswith("final_"))
async def Final(call: CallbackQuery, state: FSMContext):
    yonalish = call.data.split("_")
    soz = yonalish[1]

    if soz == "bosh":
        await call.message.delete()
        await call.message.answer_photo(photo="https://bookmaker-ratings.ru/wp-content/uploads/2017/05/1111-3.jpg",
        caption=f"🔝 siz asosiy menyuga qaytdingiz\n\nhttps://t.me/piton_code_bot 👈",
        reply_markup=start)

    elif soz == "final":
        await call.message.delete()
        await state.update_data(
            {
                "user": 0,
                "komputer": 0,
                "user_shot": "",
                "bot_shot": "",
                "user_pen": 0,
                "bot_pen": 0
            }
        )
        data = await state.get_data()
        verus = data.get("final")
        ushot = data.get("user_shot")
        bshot = data.get("bot_shot")
        await call.message.answer_photo(photo="https://blog.eldorado.ru/storage/publication/Ki2swLj1frKUfFCCq0SO3CF6iGpe3iCl0t5fvW4r.jpeg",
            caption=f"{html.bold("oyin boshlandi")} ⏳\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot}\n{verus} : {bshot}\n\ntopni teping ⚽️",
            reply_markup=variantlar.as_markup())
        await state.set_state(KickFinal.shot)



@dp.callback_query(F.data.startswith("pen_"), KickFinal.shot)
async def ikki(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    robot = choice(komputer)
    yonalish = call.data.split("_")
    soz = yonalish[1]
    
    data = await state.get_data()
    ushot = data.get("user_shot")
    user = data.get("user")
    penalty = data.get("user_pen")
    verus = data.get("final")

    if robot == soz:
        await state.update_data(
            {
                "user_shot": ushot + "❌",
                "user_pen": penalty + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        penalty1 = data1.get("user_pen")
        komp = data1.get("komputer")
        user1 = data1.get("user")
        print(penalty1,"\n",user,komp)

        if penalty1 == 4:
            if komp - user1 >= 2:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥈 siz yutqazdingiz",
                    reply_markup=start) 

            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepFinal.kep)

        elif penalty1 >= 5:
            if komp - user1 == 1:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥈 siz yutqazdingiz",
                    reply_markup=start) 

            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepFinal.kep)    
        
        else:        
            await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                reply_markup=variantlar.as_markup())
            await state.set_state(KeepFinal.kep)    

    else:
        await state.update_data(
            {
                "user": user + 1,
                "user_shot": ushot + "✅",
                "user_pen": penalty + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        penalty1 = data1.get("user_pen")
        komp = data1.get("komputer")
        user1 = data1.get("user")
        print(penalty1,"\n",user1,komp)

        if penalty1 == 4:
            if user1 - komp == 3:
                await call.message.answer_photo(photo="https://static.tildacdn.com/tild3031-3937-4039-a233-336134383131/trophy-scaled.jpeg",
                    caption=f"{html.bold("Goool")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥇 siz chempion boldingingiz",
                    reply_markup=start)                      

            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepFinal.kep)

        elif penalty1 >= 5:    
            if user1 - komp == 2:    
                await call.message.answer_photo(photo="https://static.tildacdn.com/tild3031-3937-4039-a233-336134383131/trophy-scaled.jpeg",
                    caption=f"{html.bold("Goool")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user1}-{komp}\n🥇 siz chempion boldingingiz",
                    reply_markup=start)                      

            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KeepFinal.kep)
        
        else:
            await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni qaytaring 🧤",
                reply_markup=variantlar.as_markup())
            await state.set_state(KeepFinal.kep)



@dp.callback_query(F.data.startswith("pen_"), KeepFinal.kep)
async def iki1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    robot = choice(komputer)
    yonalish = call.data.split("_")
    soz = yonalish[1]

    data = await state.get_data()
    bshot = data.get("bot_shot")
    komp = data.get("komputer")
    pen = data.get("bot_pen")
    verus = data.get("final")
    
    if robot == soz:
        await state.update_data(
            {
                "bot_shot": bshot + "❌",
                "bot_pen": pen + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        pen1 = data1.get("bot_pen")
        user = data1.get("user")
        komp1 = data1.get("komputer")
        print(pen1,"\n",user,komp)

        if pen1 == 3:
            if user - komp1 == 3:
                await call.message.answer_photo(photo="https://static.tildacdn.com/tild3031-3937-4039-a233-336134383131/trophy-scaled.jpeg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥇 siz chempion boldingingiz",
                    reply_markup=start)    
        
            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot) 

        elif pen1 == 4:
            if user - komp1 == 2:   
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥇 siz chempion boldingingiz",
                    reply_markup=start) 
            
            else:        
                await call.message.answer_photo(photo="https://static.tildacdn.com/tild3031-3937-4039-a233-336134383131/trophy-scaled.jpeg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot) 

        elif pen1 >= 5:
            if user > komp1:
                await call.message.answer_photo(photo="https://static.tildacdn.com/tild3031-3937-4039-a233-336134383131/trophy-scaled.jpeg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥇 siz chempion boldingingiz",
                    reply_markup=start) 
            
            else:        
                await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                    caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot)
        
        else:        
            await call.message.answer_photo(photo="https://wallpapercave.com/wp/wp2515770.jpg",
                caption=f"{html.bold("Gol emas")} ❗️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                reply_markup=variantlar.as_markup())
            await state.set_state(KickFinal.shot)

    else:
        await state.update_data(
            {
                "komputer": komp + 1,
                "bot_shot": bshot + "✅",
                "bot_pen": pen + 1
            }
        )
        data1 = await state.get_data()
        ushot1 = data1.get("user_shot")
        bshot1 = data1.get("bot_shot")
        pen1 = data1.get("bot_pen")
        user = data1.get("user")
        komp1 = data1.get("komputer")
        print(pen1,"\n",user,komp1)

        if pen1 == 3:
            if komp1 - user == 3:
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥈 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot)

        elif pen1 == 4:
            if komp1 - user == 2:  
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥈 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot)      

        elif pen1 >= 5:
            if komp1 > user:    
                await call.message.answer_photo(photo="https://static.seekingalpha.com/uploads/2018/4/18/8476581-15240913408095038_origin.png",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\n⚠️ {html.bold("oyin tugadi")}\n📌 hisob: {user}-{komp1}\n🥈 siz yutqazdingiz",
                    reply_markup=start)    
            
            else:
                await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                    caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                    reply_markup=variantlar.as_markup())
                await state.set_state(KickFinal.shot)    
        
        else:
            await call.message.answer_photo(photo="https://wallpapers.com/images/hd/cool-soccer-ball-goal-shot-6mzthep8me8z4dz6.jpg",
                caption=f"{html.bold("Goool")} ☄️\n\n  🇪🇺 Final\n🙎🏻‍♂️ user          : {ushot1}\n{verus} : {bshot1}\n\ntopni teping ⚽️",
                reply_markup=variantlar.as_markup())
            await state.set_state(KickFinal.shot)            


@dp.message(F.text)
async def restart(message: Message):
    await message.reply("botni qayta ishga tushirish uchun /start ni boshing")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("bot o`chdi")        