import discord

bot = discord.Bot()

@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    print(ctx)
    await ctx.respond(f"Hello {name}!")

@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")


bot.run("MTAwOTgzOTUzMjk5ODQwNjIzNA.Gt49Om.mjOL9st0iFsXDSjIelaQQXn9zrs0CZAhniz5tA")