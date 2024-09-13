
from discord.ext import commands
from discord import app_commands
from discord import SyncWebhook # Import SyncWebhook

import asyncio
import random
import requests
import discord

import time

intents = discord.Intents.default()
intents.message_content = True

config = {
    'token': 'MTI4MzgzNDM5NDE1MDE3NDgyMA.GQD23U.qllCdqMAUyHXEK6PbqDZ5Fi8eXD0rrwPe6uJ7w',
    'prefix': '!',
}

bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.event
async def on_raw_reaction_add(payload):
    ourMessageID = 1283847141802119298 # айди сообщения (сначала создаем его командой !react, а потом копируем его айди и вписываем сюда)

    if ourMessageID == payload.message_id:
        member = payload.member # определяем юзера
        guild = member.guild # определяем сервер

        emoji = payload.emoji.name # эмоджи при нажатии на которое выдается роль
        if emoji == '🍕': # само эмоджи
            role = discord.utils.get(guild.roles, name="away") # определяем роль которую будем выдавать
            await member.add_roles(role) # выдаем рольку

@bot.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 1283847141802119298 # айди сообщения (сначала создаем его командой !react, а потом копируем его айди и вписываем сюда)

    if ourMessageID == payload.message_id:
        guild = await(bot.fetch_guild(payload.guild_id))
        emoji = payload.emoji.name # эмоджи при нажатии на которое выдается роль
        if emoji == '🍕': # само эмоджи
            role = discord.utils.get(guild.roles, name="away") # определяем роль которую будем выдавать

            member = await(guild.fetch_member(payload.user_id))
            if member is not None: # проверяем есть ли он на сервере
                await member.remove_roles(role) # забираем рольку
            else:
                print('not found')

@bot.command()
async def react(ctx):
    channel = bot.get_channel(1102507613717020722) # определяем канал, куда будет отправлено сообщение с эмбедом и реакциями
    embed=discord.Embed(title="Заголовок эмбеда", description="""Описание какое-то.""", color=0x5e7abd) # сам эмбед
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1545/1545324.png") # кортиночка
    embed.set_footer(text="ggdt.ru") # футер
    mojj = await channel.send(embed=embed)
    await mojj.add_reaction('🍕') # отправляем эмбед + добавляем реакцию

#конец клик-ролей

class SlashBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix="!", intents=discord.Intents.default())

    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
        await self.tree.sync()

bot = SlashBot()

@bot.tree.command(name="практич", description="Итоги практического экзамена кадета")
    
@app_commands.choices(result=[
     app_commands.Choice(name='Сдал', value=1),
     app_commands.Choice(name='Не сдал', value=2)
])
    
@app_commands.choices(count=[
     app_commands.Choice(name='Практика по Дорожному Кодексу', value=1),
     app_commands.Choice(name='Практика по Процессуальному Кодексу', value=2)
])    
#async def profile(interaction: discord.Interaction, command:str=None):
#async def _ping(interaction: discord.Interaction) -> None:
async def userping(interaction: discord.Interaction, member: str, cadet: str, result: app_commands.Choice[int], count: app_commands.Choice[int]):
    await interaction.response.send_message(f"Готово!")
 
    channel = bot.get_channel(1276841807954706443) # определяем канал, куда будет отправлено сообщение с эмбедом и реакциями
    embed = discord.Embed( 
    title="Итоги практического экзамена", 
    color= discord.Color.green ()  # Выбираем цвет 
    ) 
    embed.add_field( 
        name="Сотрудник PAI", 
        value=member, 
        inline=False
    )
    embed.add_field( 
        name="Кадет Police Academy", 
        value=cadet, 
        inline=False 
    ) 
    embed.add_field( 
        name="Тип экзамена", 
        value=count.name, 
        inline=False 
    ) 
    embed.add_field( 
        name="Итог экзамена", 
        value=result.name, 
        inline=False 
    ) 
    embed.set_footer(
    text="Create by Notoriuz Ottovietinghoff | razrabotchik5060",
    icon_url="https://media.discordapp.net/attachments/1090804007250968693/1102583237345284156/gata5rptokyo_online-video-cutter.com.gif?ex=66e43a28&is=66e2e8a8&hm=f48040e842d693f50a9f76c6e560ce7a616d9a75ebc1fed8667a3ccd17a7bfc3&",
)
    embed.set_thumbnail(url="https://i.postimg.cc/DzGhwQLY/1.png")
    mojj = await channel.send(embed=embed)
    await mojj.add_reaction('🍕') # отправляем эмбед + добавляем реакцию
    
    webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1266869765574623253/s9IA2yAUtH7zInjVD-6V4dEg4mBoiF2LgCBkPiXpqEIAFdJIAgicTHmuVVunBZOz0RWF') # lspd
    await webhook.send(embed=embed) # отправляем эмбед в канал где была прописана команда
 
bot.run(config['token'])