import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from gif_find import gifs
import os

Bot = commands.Bot(command_prefix = '**')


arr_delete = ["!!!play", "!!!stop", "!!!Play", "!!!PLAY",
              "!!!Stop", "!!!STOP", "!!!CHOOSE", "!!!Choose",
              "!!!choose", "playing"]


@Bot.event
async def on_ready():
    print("Bot is online")


@Bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = "pirat")
    await Bot.add_roles(member, role)


@Bot.command(pass_context = True)
async def reaction(ctx):
    await Bot.add_reaction(ctx.message, "😯")


@Bot.command(pass_context = True)
async def gif(ctx):
    await Bot.say(gifs())


@Bot.event
async def on_message(msg):# функция удоляет сообщение если внем содержится слово из заданнаго массива в данном случае "arr_delete"
    for i in arr_delete:#каждый раз i принимает значение из массива
        if i in  msg.content:# проверяется есть ли значение i в сообщении если есть то -
            time.sleep(3)
            await Bot.delete_message(msg)# - удаляет это сообщение
    await Bot.process_commands(msg)


@Bot.command(pass_context = True)#BAN
async def ban(ctx, user: discord.Member):
    await Bot.ban(user)


@Bot.command(pass_context = True)
async def hello(ctx):#Приветствие
    await  Bot.say("Hello {}".format(ctx.message.author.mention))


@Bot.command(pass_context = True)#Что-то вроде структурированного списка или как СЕТ
async def info(ctx, user: discord.User):#принимает сообщение (команду info) и имя о ком нужна информация
    emb = discord.Embed(title = "Info about {}".format(user.name) , color = 0x39d0d6)#наиминование самого СЕТа, имя бота принявшего выполнение СЕТа, и цвет СЕТа
    emb.add_field(name = "Name", value = user.name)#Имя заданное в команде
    emb.add_field(name = "Joined at", value = str(user.joined_at)[:16])# время добавления указанного человека(срез строки с датой [:16])
    emb.add_field(name = "ID", value = user.id)#                                        его ID
    if user.game != None:# 2) если не играет то условие пропускается
        emb.add_field(name = "Game", value = user.game)# 1) игра в которую он играет на данный момент
    emb.set_thumbnail(url = user.avatar_url)# URL автора СЕТа
    emb.set_author(name = Bot.user.name, url = "https://discordapp.com/oauth2/authorize?client_id=557643334638764032&scope=bot&permissions=8")#Имя бота и его ссылка
    #emb_set_footer(text = "Вызвано: {}".format(user.name), icon_url = user.avatar_url)###НЕ РАБОТАЕТ!!!
    await Bot.say(embed = emb)#Бот пишет в чат заданный выше СЕТ
    await Bot.delete_message(ctx.message)#Бот удаляет сообщение с командой "info"


token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))

