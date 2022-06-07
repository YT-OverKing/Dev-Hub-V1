# รันโมดูล

import discord
from termcolor import colored
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
import os


prefix = ("!") # ใส่ PREFIX
token = os.environ['TOKEN'] # ใส่ TOKEN ใน Secret Environment เเถบข้าง

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="เทสคาสิโน", color=255, description=f"**{prefix}start**\ncasino , with , cf , dep.\n\n**{prefix}stop**\nstop casino.")
  embed.set_thumbnail(url="https://discord.gg/unicommunity")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)

async def start(ctx):
	await ctx.message.delete()
	await ctx.send('**Zachary.exe Online**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(0.2) # รีเฟรชเรต
			await ctx.send('! -Wit-h All') # เปลี่ยนวิทเอาเอง จวยป้อน
			print(f"{Fore.BLACK}วิท")
			await asyncio.sleep(0.2)
			await ctx.send(' -Coc-K-Fig-Ht All')
			print(f"{Fore.RED}ตีไก่")
			await asyncio.sleep(0.2)
			await ctx.send('! -De-P All')
			print(f"{Fore.BLACK}เดปสำเร็จ")
			await asyncio.sleep(0.2)
			await ctx.send('! -De-P All')
			print(f"{Fore.BLACK}เดปสำเร็จ")
			await asyncio.sleep(6)


@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  activity = discord.Game(name="# NotZachary", type=4)
  await bot.change_presence(status=discord.Status.online, activity=activity)
  print(f'''{Fore.RED}
▀█ ▄▀█ █▀▀ █░█ ▄▀█ █▀█ █▄█
█▄ █▀█ █▄▄ █▀█ █▀█ █▀▄ ░█░
{Fore.YELLOW}
    Zachary.exe
{Fore.LIGHTBLUE_EX}
        Nothing Here!!
''')
  
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

for color in colors:  
  print(colored('▀█ ▄▀█ █▀▀ █░█ ▄▀█ █▀█ █▄██▄ █▀█ █▄▄ █▀█ █▀█ █▀▄ ░█░', color), end="")
print()


bot.run(token, bot=False)
