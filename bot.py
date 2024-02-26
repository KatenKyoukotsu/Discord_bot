import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command('help')

# Words
hello_words = ['привет', 'hi', 'здарова', 'hello']
bad_words = ['бобры', 'быть бобром не круто',
             'ты не крутой бобер', 'бобры!',
             'быть бобром не круто!',
             'ты не крутой бобер!']


@client.event
async def on_ready():
    print('На месте!')


@client.event
async def on_member_join(member):
    channel = client.get_channel(your_token)
    role = discord.utils.get(member.guilds.roles, id=your_token)
    await member.add_roles(role)
    await channel.send('работает')

# !hello


@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Даю краба {author}')

# !test


@client.command()
async def test(ctx):
    await ctx.send('/tts Bitch \nlol')

# !echo


@client.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# !clear Чистка чата


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

# !kick кик игрока


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='Гнев Бога'):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'Бог в гневе и выкинул с олимпа { member.mention }')

# !ban Бан игрока


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason='Наверное ты и сам догадываешься'):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'О мой бог этот парень реально пререшел черту { member.mention }')

# !unban разбанить игрока


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Бог сегодня добрый , он простил {user.mention}')
        return

# !user_mute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.remove_roles(mute_role)
    await ctx.send(f'Бог забрал право голоса у {member.mention}')

# !user_unmute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.remove_roles(mute_role)
    await ctx.send(f'Бог вернул право голоса {member.mention}')

# !help Список команд


@client.command()
async def help(ctx):
    await ctx.send('Команды бота:\n'
                   '!hello - Поздороваться с ботом\n'
                   '!echo - эхо\n'
                   '!clear [количество сообщений+1] - Стереть сообщения\n'
                   '!kick - Кикнуть кого-либо (Использование только Администраторами)\n'
                   '!ban - Забанить кого-либо (Использование только Администраторами)\n'
                   '!unban - Разбанить кого-либо (Использование только Администраторами)\n'
                   '!user_mute - Замутить кого-либо (Использование только Администраторами)\n'
                   '!user_unmute - Размутить кого-либо (Использование только Администраторами)\n'
                   'А также 2 команды пасхалки!\n')

# !help_me Special for Lucky Stranger


@client.command()
async def help_me(ctx):
    await ctx.send('Help!')
    await ctx.send('I need somebody')
    await ctx.send('(Help!) not just anybody')
    await ctx.send('(Help!) you know I need someone')
    await ctx.send('Heeeeeeeeeeeelp!')
    await ctx.send('I never needed anybodys help in any way')
    await ctx.send('But now these days are gone, I am not so self assured (but now these days are gone)')
    await ctx.send('(And now I find) Now I find Ive changed my mind and opened up the doors')
    await ctx.send('Help me if you can, Im feeling down')
    await ctx.send('And I do appreciate you being round')
    await ctx.send('Help me get my feet back on the ground')
    await ctx.send('Wont you please, please help me?')
    await ctx.send('And now my life has changed in oh so many ways (and now my life has changed)')
    await ctx.send('My independence seems to vanish in the haze')
    await ctx.send('But every now and then I feel so insecure (I know that I)')
    await ctx.send('I know that I just need you like Ive never done before')
    await ctx.send('Help me if you can, Im feeling down')
    await ctx.send('And I do appreciate you being round')
    await ctx.send('Help me get my feet back on the ground')
    await ctx.send('Wont you please, please help me')
    await ctx.send('When I was younger, so much younger than today')
    await ctx.send('I never needed anybodys help in any way')
    await ctx.send('But now these days are gone, Im not so self assured (but now these days are gone)')
    await ctx.send('(And now I find) now I find I ve changed my mind and opened up the doors')
    await ctx.send('Help me if you can, Im feeling down')
    await ctx.send('And I do appreciate you being round')
    await ctx.send('Help me get my feet back on the ground')
    await ctx.send('Wont you please, please help me, help me, help me, ooh')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('↓')
    await ctx.send('Трек был подготовлен специально для человека судьбы...')
        


# Connect

token = open('token.txt', 'r').readline()

client.run(token)


# @client.event


# async def on_message( message ):
# msg = message.content.lower()
# if msg in hello_words:
# await message.channel.send( 'Здравствуй' )
