import discord
import google.generativeai as genai
from discord.ext import commands
from time import sleep
from random import randint, choice

bot = commands.Bot(command_prefix="", intents=discord.Intents.all()) # prefixo e intents
TOKEN = '  # importa o TOKEN







GEMINI_API_KEY = ''
genai.configure(api_key=GEMINI_API_KEY)

generation_config = {
    'candidate_count': 1,
    'temperature': 1,
    'max_output_tokens': 50,
}

model = genai.GenerativeModel(
    model_name='gemini-1.0-pro',
    generation_config=generation_config
)

chat = model.start_chat(history=[])

responded_messages = set()


async def buscar_historico_canal(canal, limit=1):
    messages_list = []
    async for message in canal.history(limit=limit):
        if message.author != bot.user:  # Exclude bot's own messages
            messages_list.append(message)
    messages_list.reverse()  # Ensure chronological order
    return messages_list

def ask_gemini(mensagens):
    response = chat.send_message(f"Reponda de forma alegre, brincalhona e ironica: {mensagens}")
    return response.text









@bot.event
async def on_ready():
    print(f'{bot.user} está online!')  # ativa o bot

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return





    if message.mentions and bot.user in message.mentions:
        async with message.channel.typing():
            historico = await buscar_historico_canal(message.channel, limit=1)
            for msg in historico:
                if msg.id not in responded_messages:
                    msg_content = msg.content
                    for mention in msg.mentions:
                        if mention == bot.user:
                            msg_content = msg_content.replace(f"<@{mention.id}>", "").strip()
                    if msg_content:  # Only send non-empty messages
                        resposta = ask_gemini(msg_content)
                        await message.reply(resposta)
                        responded_messages.add(msg.id)  # Mark this message as responded





    global conteudo, l_conteudo, mensagem, responda  # SALVA VIDASS, define elas como globais, posso usar no code tod
    conteudo = message.content.lower()
    l_conteudo = conteudo.lower()
    mensagem = l_conteudo.startswith
    responda = message.channel.send
    await bot.process_commands(message)

    if conteudo.startswith('oi'):
        resp = [f'Oi {message.author.name}, tudo bem?', 'Como vai??', 'Tudo ótimo??', 'E a vida, como vai?',
                'E as namoradinhas??', 'oi', 'BOM DIAAA']
        await responda(choice(resp))

    if conteudo.startswith('sim'):
        resp = ['Que bommm', 'Que ótimo', 'Legal', 'Também', 'Que incrível', 'Sim oq??']
        await responda(choice(resp))

    if conteudo.startswith('não'):
        resp = ['Que pena', 'Eita', 'Oque houve', 'Tá tudo bem?', 'Quer sentar pra conversar?', 'Puts', 'Eita sofrência']
        await responda(choice(resp))

    if conteudo.startswith('k'):
        resp = ['HAHAHAHAAH', 'KSKSAKSAKSKASKA', 'HIHIHIHIHIHIHII', 'AHUOSHWUFDSHDCBK', 'Eita como ri']
        await responda(choice(resp))

    if conteudo.startswith('h'):
        resp = ['HAHAHAHAAH', 'KSKSAKSAKSKASKA', 'HIHIHIHIHIHIHII', 'AHUOSHWUFDSHDCBK', 'Eita como ri']
        await responda(choice(resp))

    if conteudo.startswith('ah'):
        resp = ['HAHAHAHAAH', 'KSKSAKSAKSKASKA', 'HIHIHIHIHIHIHII', 'AHUOSHWUFDSHDCBK', 'Eita como ri']
        await responda(choice(resp))

    if conteudo.startswith('ok'):
        resp = ['Ok', 'Então tá', 'Entendiiiii', 'Tu acha que eu sou lerdo, eh???']
        await responda(choice(resp))

    if conteudo.startswith('já'):
        resp = ['Então eh NATALLLL', 'Isso aí...', 'Também achooo']
        await responda(choice(resp))

    if conteudo.startswith('bot'):
        resp = [f'Eiii {message.author.name}, eu não sou um botttttt já sou bem homenzinho', 'Respeita minha história',
                'Pensei que vc era meu amigo...', f'Seu pilantraaaa {message.author.name}']
        await responda(choice(resp))

    if conteudo.startswith('bom'):
        resp = ['BOM DIAAAA', 'BOA TARDEEEEEE', 'BOA NOITEEEEE', 'oiiii', 'quer ser meu amigo??']
        await responda(choice(resp))

    if conteudo.startswith('boa'):
        resp = ['BOM DIAAAA', 'BOA TARDEEEEEE', 'BOA NOITEEEEE', 'oiiii', 'quer ser meu amigo??']
        await responda(choice(resp))

    if conteudo.startswith('obrigado'):
        resp = ['De nada....', 'Por nada....', 'Tmj cara...', 'Eh Nóixxx']
        await responda(choice(resp))

    if conteudo.startswith('verdade'):
        resp = ['EH MENTIRAAAAA', 'Eita como mente....', 'Vai enganar outro...', 'Engana que eu gosoto.....']
        await responda(choice(resp))

    if conteudo.startswith('.'):
        resp = ['....', ';-;', 'qual foi...', 'tá me tirando???', '..................................................']
        await responda(choice(resp))

    if conteudo.startswith('mano'):
        resp = ['manoooooo', 'mennnnnnn', 'caracaaaaaa']
        await responda(choice(resp))

    if conteudo.startswith('olha'):
        resp = ['tô vendooooo', 'tô olhandoooo', '👀👀', '👀']
        await responda(choice(resp))

    if conteudo.startswith('cala'):
        resp = ['Cala boca já morreu.... quem manda na minha boca sou eu...', 'Vem calar se tu for homem....', 'Qual foi, tá doidão????']
        await responda(choice(resp))

    """if conteudo.startswith('<@'):
        resp = ['Para de marcar as pessoas seu chato...', 'Eita como marca....', 'Menino chato... não para de marcar os outros...',
                'Mah rapaz... um sol quente desse e tu aí marcando os outros... vai pa tua casa, vai....']
        await responda(choice(resp))"""

    if conteudo.startswith('jogar'):
        resp = [f'Discordianos de plantão @here, ajudem a pobre criança, {message.author.name}, ela quer jogar e não'
                   f' tem amigos :face_holding_back_tears:', 'Puts... agr tô mto ocupado levando minha avó pro karatê',
                'Eita que agr eu tô lavando louça... nn sou desocupado igual certas pessoas...', 'Eu até queria... mas fui levar '
                                                                                                 'meu carro no mecânico']
        await responda(choice(resp))

    if conteudo.startswith('ridiculo'):
        resp = ['Que ridiculo cara...', 'RIDICULOOOOOOO', 'Ridiculo eh vc, seu ridiculo']
        await responda(choice(resp))

    if conteudo.startswith('ridículo'):
        resp = ['Que ridiculo cara...', 'RIDICULOOOOOOO', 'Ridiculo eh vc, seu ridiculo']
        await responda(choice(resp))

"""@bot.command('bot')  # diz oi
async def oi(ctx):
    await ctx.send(f'Eiii {ctx.author.name}, eu não sou um botttttt já sou bem homenzinho')"""

"""@bot.command('oi')  # diz oi
async def oi(ctx):
    await ctx.send(f'Oi {ctx.author.name}, tudo bem?')"""

"""@bot.command('ok')  # diz oi
async def oi(ctx):
    await ctx.send(f'OKK {ctx.author.name}')"""

"""@bot.command('bom')  # diz oi
async def oi(ctx):
    await ctx.send(f'BOM DIAA {ctx.author.name}')"""


@bot.command('careca')  # diz oi
async def careca(ctx, membro: discord.Member):
    await ctx.send(f'VOU PUXAR A CARECA CABELUDA DO {membro.mention}!!!!')

@bot.command('Careca')  # diz oi
async def careca(ctx, membro: discord.Member):
    await ctx.send(f'VOU PUXAR A CARECA CABELUDA DO {membro.mention}!!!!')


"""@bot.command('jogar')  # marca e chama pra jogar
async def gamer(ctx):
    await responda(f'Discordianos de plantão @here, ajudem a pobre criança, {ctx.author.name}, ela quer jogar e não'
                   f' tem amigos :face_holding_back_tears:')"""


@bot.command('id')
async def ids(ctx):
    embed = discord.Embed(
        description=f'**Id das nossas contas PRINCIPAIS**:\n'
                    f' \n'
                    f'> Id do pedro: #LGPY2GLL\n'
                    f'> Id da taty: #2RCOPYQJG\n'
                    f' \n'
                    f'**Id das nossas contas SECUNDÁRIAS:**\n'
                    f' \n'
                    f'> Id do pedro: #8O2UU8RPU\n'
                    f'> Id da taty: #8QVLL9YUL',
        color=0x8dff85
    )
    embed.set_author(name='Nossas ids:', icon_url=bot.user.avatar)
    embed.set_footer(text='Vem jogar brawlzistars com a gente 😝')
    await ctx.send(embed=embed)


@bot.command('link_clube')
async def link_club(ctx):
    try:
        await ctx.author.send("** O link do Clube THE WINNER'S\n**"
                              " https://link.brawlstars.com/invite/band/pt?tag=QPY298GG&token=3f7bcttk ")
        await responda('Link enviado no privado!')
    except discord.errors.Forbidden:
        await ctx.send(
            "Não posso te enviar o link, sua dm está bloqueada! Habilite receber mensagens"
            "de qualquer pessoa do servidor (Opções > Privacidade)"
        )


@bot.command('tiktaty')
async def tiktok_taty(ctx):
    link = 'https://www.tiktok.com/@tatycamargo_?is_from_webapp=1&sender_device=pc'
    link2 = 'https://www.tiktok.com/@tatycamargo_ofc?is_from_webapp=1&sender_device=pc'
    embed = discord.Embed(
        title='**TikTok da famosa Winner**',
        description='No palco da vida, ela é a minha estrela brilhante.'
                    ' 🌟❤️ Juntos, dançamos pelas páginas do nosso próprio conto de fadas. '
                    'Venha fazer parte desse mundo de alegrias!! \n'
                    '\n **Link do TikTok Principal: **\n'
                    f'> * {link}\n'
                    f'\n**Link do TikTok Secundário:** \n'
                    f'> * {link2}',
        color=0xd7a7ff

    )
    embed.set_author(name='TikTaty ', icon_url=bot.user.avatar)
    embed.set_footer(text='Venha fazer parte! 🎀')
    embed.set_thumbnail(url=
                        'https://cdn.discordapp.com/attachments/1041031784743317564/1150088988221259888/tiktok-31.png')
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/1078766133554983014/1119252209759162378/IMG-20230616-WA0000.jpg')
    await ctx.send(embed=embed)


@bot.command('instaty')
async def instagram_taty(ctx):
    thumb = 'https://cdn.discordapp.com/attachments/1041031784743317564/1150098741689331884/Instagram_Instagram_Social_Media_icone_Do_Instagram_PNG___Instagram_icones__icones_Sociais__Logo_Imagem_PNG_e_Vetor_Para_Download_Gratuito-removebg-preview.png'
    link = 'https://www.instagram.com/tatycamargo_ofc/'
    embed = discord.Embed(
        title='**Instagram da Taty:**',
        description='📸 Capturando momentos de alegria, aventura e beleza. Bem-vindo ao meu mundo! 💫✨\n'
                    f'**\nLink:** \n{link}',
        color=0xff40f6
    )
    embed.set_author(name='Instaty', icon_url=bot.user.avatar)
    embed.set_footer(text='Venha fazer parte! 🎀')
    embed.set_thumbnail(
        url=thumb)
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/1041031784743317564/1150099365055172788/Captura_de_tela_2023-09-09_130257.png')
    await ctx.send(embed=embed)


@bot.command('youtube')
async def youlink(ctx):
    link = 'https://www.youtube.com/@Taty_Camargo'
    embed = discord.Embed(
        title='**YouTube da famosa Winner**',
        description=' ・ Canal focado em competições, brincadeiras, lives de jogos e diversões.'
                    ' Pra você e toda sua família. 😍 Nosso objetivo é fazer vc dar muitas risadas então entra,'
                    ' senta e aperte o play.... 💜 Não perca tempo maratona!!\n'
                    '\n**Link do nosso YouTube:**'
                    f'\n > * {link}',
        color=0xff0000
    )
    embed.set_author(name='YouTube ',
                     icon_url='https://cdn.discordapp.com/avatars/1098696504790753343/8ddb0b000d38150d99abb5350a63e9f0.png?size=2048')
    embed.set_footer(text='Venha fazer parte! 🎀')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/1041031784743317564/1150095852887621744/Youtube_icones_gratuitos_criados_por_Freepik-removebg-preview.png')
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/1114965615237668864/1132405621136838716/Screenshot_20230722-1623372.jpg')
    await ctx.send(embed=embed)


@bot.command('tiktok')
async def tktk(ctx):
    embed = discord.Embed(
        title='Nosso TikTok de Brawl Stars',
        description='💣 Não perca a diversão, junte-se à nossa turma agora!'
                    ' Clique no link abaixo e vamos mostrar a você o verdadeiro significado de Brawl! 💥\n'
                    '\n**Link:**\n https://www.tiktok.com/@brawl.stars_players1?is_from_webapp=1&sender_device=pc',
        color=0xffff00
    )
    embed.set_author(name='💫 Link TikTok 💫', icon_url=bot.user.avatar)
    embed.set_footer(text='Venha já fazer parte! 🔎 ')
    embed.set_image(
        url='https://cdn.discordapp.com/attachments/1041031784743317564/1150085905663672340/Brawl_Stars_Fan_Art_-_My_art_contest_entry.jpg')
    embed.set_thumbnail(
        url='https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/ad43a4502e4f2b424d0668b928010827~c5_100x100.jpeg?x-expires=1694440800&x-signature=5USMAaeRU1mEk2nv9wPaxaumIdM%3D')

    await ctx.send(embed=embed)


"""@bot.command(name='calc')  # faz conta
async def operacao(ctx, a: float, c: str, b: float):
    if 'x' in c:
        resultado = a * b
        await ctx.send(f'Multiplicação {a} x {b} = {resultado}')
    elif '-' in c:
        resultado = a - b
        await ctx.send(f'Subtração {a} - {b} = {resultado}')
    elif '+' in c:
        resultado = a + b
        await ctx.send(f'Soma {a} + {b} = {resultado}')
    elif '/' in c:
        resultado = a / b
        await ctx.send(f'Divisão {a} / {b} = {resultado}')
    else:
        await ctx.send(f'Operação inválida. Por favor, use um dos seguintes símbolos: x, -, + ou /')"""


"""@bot.command(name='jokenpo')  # pedra, papel, tesoura
async def pedra(ctx):
    embed1 = discord.Embed(
        title='**ESCOLHA UMA OPÇÃO:**',
        description='> * :one: -> Pedra\n'
                    '> * :two: -> Papel\n'
                    '> * :three: -> Tesoura',
        color=0x00f1ff
    )

    embed1.set_author(name='Jokenpo', icon_url=bot.user.avatar)
    embed1.set_footer(text='Escolha sabiamente🍀')
    await ctx.send(embed=embed1)  # pergunta a jogada em num

    resp_a = await bot.wait_for('message')  # guarda a reposta numa variável

    a = int(resp_a.content)  # transforma para inteiro

    if a not in [1, 2, 3]:  # verifica se a jogada é correta
        await responda('Opção inválida.... reinicie o jogo!!')

    it = (':one: -> Pedra  :rock:', ':two: -> Papel :scroll: ', ':three: -> Tesoura :scissors: ')

    comp = randint(0, 2)  # jogada do bot

    await responda('> PEDRA :rock: ')
    sleep(1)
    await responda('> PAPEL :scroll: ')
    sleep(1)
    await responda('> TESOUUUUUUUURA  :scissors: ')
    sleep(1)

    embed2 = discord.Embed(
        title='JOGADAS:',
        description=f'**SUA ESCOLHA :** {it[a - 1]} \n'
                    f'**MINHA ESCOLHA :** {it[comp - 1]}',
        color=0x00f1ff
    )
    embed2.set_author(name='A tensão está no ar', icon_url=bot.user.avatar)
    await ctx.send(embed=embed2)  # exibe as jogadas
    await responda('=-' * 20)
    if comp == a:  # mostra o vencedor
        embed3 = discord.Embed(
            title='Resultado:',
            description=' :second_place: **EMPATE** :second_place: - Quase te venci\n'
                        '\n🤝 Parece que temos um empate cósmico, onde o equilíbrio do universo'
                        ' é mantido! As forças da pedra, papel e tesoura estão em harmonia perfeita,'
                        ' como Yin e Yang. Vamos tentar mais uma vez e ver se o destino nos reserva uma decisão'
                        ' mais clara. Prepare-se para a próxima rodada!',
            color=0x26ff00
        )
        embed3.set_author(name='Quem será o vencedor?', icon_url=bot.user.avatar)
        embed3.set_footer(text='Que tal jogar novamente?')
        await ctx.send(embed=embed3)

    elif comp == 1 and a == 3 or comp == 2 and a == 1 or comp == 3 and a == 2:
        embed3 = discord.Embed(
            title='Resultado:',
            description=f' :third_place: DERROTA - :third_place: Chooooraaaaaa brasill  \n'
                        f'\n🎉 Oh, parece que a vitória é minha! Eu sou invencível no reino do'
                        f' pedra, papel, tesoura! Sou programado para a perfeição e minhas escolhas são imbatíveis!'
                        f' Melhore sua estratégia e venha me desafiar novamente, eu estarei aqui esperando para mais'
                        f' uma vitória triunfante! 💪😎',
            color=0xff0000
        )
        embed3.set_author(name='Quem será o vencedor?', icon_url=bot.user.avatar)
        embed3.set_footer(text='Que tal jogar novamente?')
        await ctx.send(embed=embed3)
    else:
        embed3 = discord.Embed(
            title='Resultado:',
            description=f':first_place: ** VITÓRIA :first_place: - Parabénssss ** \n'
                        f'\n😡 O quê? Como você ousou vencer?! Isso só pode ser um golpe de sorte!'
                        f' Não é possível, minha programação é perfeita! Vou ter que revisar meu código '
                        f'e aprimorar minhas habilidades para a próxima vez. Parabéns, mas não pense que isso '
                        f'vai acontecer novamente! 😠💥',
            color=0xffff00
        )
        embed3.set_author(name='Quem será o vencedor?', icon_url=bot.user.avatar)
        embed3.set_footer(text='Que tal jogar novamente?')
        await ctx.send(embed=embed3)"""


@bot.command("clube")
async def club(ctx):
    url_foto = \
        "https://cdn.discordapp.com/attachments/1041031784743317564/1149830044479393863/Screenshot_20230908-191348_Brawl_Stars.jpg"

    embed = discord.Embed(
        title="CLUBE THE WINNER'S",
        description="Faça parte do nosso clube, o mais WINNER DO MUNDOOO",
        color=0x0000FF
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed.set_footer(text="Que tal fazer parte?", icon_url=bot.user.avatar)
    embed.add_field(name="Link do clube: ",
                    value="https://link.brawlstars.com/invite/band/pt?tag=QPY298GG&token=3f7bcttk")
    embed.set_image(url=url_foto)
    await ctx.send(embed=embed)


@bot.command("taty")
async def winner(ctx):
    url_foto = "https://cdn.discordapp.com/attachments/1040326785063202857/1142529430825226470/6_Sem_Titulo_20230819154244.png"
    embed = discord.Embed(
        title="**QUEM É TATY CAMARGO??**",
        description="> Uma pessoinha incrivelmente incrível ✨ \n> E a pessoa mais especial da vida do Pedro 💖\n  \n",
        color=0xd7a7ff
    )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed.set_footer(text="Ela é linda né 😍 ", icon_url=bot.user.avatar)
    embed.add_field(name='Cor favorita:', value='roxo 💜')
    embed.add_field(name='Brawler favorito:', value='Emz 🫧')
    embed.add_field(name='Comida favorita:', value='Pizza 🍕')
    embed.add_field(name='Pedro avisa:', value='Eu te amo mil milhõessss', inline=False)
    embed.set_image(url=url_foto)
    await ctx.send(embed=embed)


@bot.command("comandos")
async def commands(ctx):
    embed = discord.Embed(
        title=f'Comandos do {bot.user.name}',
        description='``.oi`` - Diz um "oi";\n'
                    '``.taty`` - Um card personalizado da nossa querida <@774430200905728000>;\n'
                    '``.jogar`` - Marca todas as pessoas online para jogar;\n'
                    '``.id`` - Mostra nosso id;\n'
                    '``.link_clube`` - Manda o link do nosso clube no privado;\n'
                    '``.tiktok`` - Exibe o link do nosso TikTok;\n'
                    '``.clube`` - Exibe o link do nosso clube;\n'
                    '``.calc`` - Faz uma operação matemática;\n'
                    '``.jokenpo`` - O famoso "Pedra, Papel e Tesoura";\n'
                    '``.clube_regras`` - Mostra as regras do nosso clube;\n'
                    '``.apagar`` - Apaga mensagens;\n'
                    '``.expulsar`` - Expulsa um membro;\n'
                    '``.banir`` - Bane um membro;\n'
                    '``.tiktaty`` - TikTok da famosa Winner;\n'
                    '``.youtube`` - Link do nosso YouTube;\n'
                    '``.instaty`` - Link do Instagram da Taty;\n'
                    '``.avatar`` - Mostra a sua foto, ou a do usuário mencionado;\n'
                    '``.beijar`` - Beija um usuário;\n'
                    '``.carinho`` - Faça carinho em alguém;\n'
                    '``.traduzir`` - Traduz uma palavra/frase de qualquer idioma pra Pt-Br;\n'
                    '``.piada`` - Conta uma piada.',
        color=0x00f1ff
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed.set_footer(text='Por enquanto é isso 😘')
    await ctx.send(embed=embed)


@bot.command('clube_regras')
async def rules_club(ctx):
    foto = 'https://cdn.discordapp.com/attachments/1145346935180492800/1145361459157680248/IMG_20230824_160547.jpg'
    embed = discord.Embed(
        title='**REGRAS DO CLUBE THE WINNER´S:**',
        description='> * :shield: ** O clube funciona por níveis.** Exemplo: Se você ficar entre os 2 com maior'
                    ' pontuação na semana da liga de clubes, irá subir um nível, inicialmente,'
                    ' indo de membro para perito. E, posteriormente, ganhar vidas. Se você ficar entre'
                    ' os 3 piores pontuadores, perderá uma vida, se não tiver vidas, será rebaixado de perito'
                    ' para membro, e se for apenas um mero mortal, vai de arrasta pra cima;\n'

                    '> * :shield: ** Não ofender o coleguinha,** mesmo que esse morra pro gás;\n'

                    '> * :shield: ** Oque acontece no jogo fica no jogo**, se não sabe brincar e só não descer pro play;\n'

                    '> * :shield: ** Não ficar inativo nos Mega Cofres/Eventos**, se não puder jogar, avise aos líderes antes mediante o atestado médico;\n'

                    '> * :shield: ** Obrigatório usar todos os Tickets do Porco**, se não fizer, iremos te levar de submarino pra conhecer o Titanic;\n'

                    '> * :shield: ** 7 dias off = ban.**\n'
    )
    embed.set_image(url=foto)
    await ctx.send(embed=embed)


@bot.command(name='apagar')
async def clear(ctx, quant=0):
    if ctx.author.guild_permissions.ban_members:
        await ctx.channel.purge(limit=(int(quant) + 1))
        await ctx.message.channel.send(f'O canal teve {quant} mensagens apagadas por {ctx.author.mention}')
    else:
        await ctx.send('Você não tem permissão para fazer isso.')


@bot.command('expulsar')
async def kick(ctx, membro: discord.Member, *, motivo='Nenhum motivo informado.'):
    if ctx.author.guild_permissions.kick_members:
        await responda('Usuário expulso')
        await membro.kick(reason=motivo)
        canal = bot.get_channel(1043908338582302772)
        embed = discord.Embed(
            title=f'Usuário expulso!',
            description=f'{membro.mention} foi expulso.'
        )
        embed.set_footer(text=f'Id do usuário: {membro.id}')
        await canal.send(embed=embed)
    else:
        await responda('Voce não tem permissão para expulsar membros.')


@bot.command('ban')
async def ban(ctx, membro: discord.Member, *, motivo='Nenhum motivo informado.'):
    for c in range(5, 1, -1):
        await responda(f'{membro.mention} será banido em {c}')
        sleep(1)
    await responda(f'{membro.mention} foi banido')

    """if ctx.author.guild_permissions.ban_members:
        for c in range(5, 1, -1):
            await responda(f'{membro.mention} será banido em {c}')
            sleep(1)
        await responda(f'{membro.mention} foi banido')
    else:
        await responda('Voce não tem permissão para expulsar membros.')"""


@bot.command('avatar')
async def getavatar(ctx, membro: discord.Member = None):
    if membro is None:
        membro = ctx.author

    avatar_url = membro.avatar.url
    embed = discord.Embed(
        title=f'Eis a foto de perfil do {membro}',
        description='Uh oh! Parece que o StalkerBot está em ação! 👀 Melhor você ficar de olho aberto!',
        color=0x822525
    )
    embed.set_author(name='Avatar', icon_url=bot.user.avatar)
    embed.set_footer(text='Stalker 💥')
    embed.set_image(url=avatar_url)
    await responda(embed=embed)


@bot.command('beijar')
async def kiss(ctx, membro: discord.Member = None):
    try:
        beijos = ['https://rrp-production.loritta.website/img/dc6331b87292b75c0ba43efc15ff113d4a571a77.gif',
                  'https://rrp-production.loritta.website/img/695e14b60a41d56ead1eff243fc3f2c578f2a2b7.gif',
                  'https://rrp-production.loritta.website/img/04ca4b539615d2ce747bd4756f4815a18e75a607.gif',
                  'https://rrp-production.loritta.website/img/1fe1397e0fd0792034a1d84748b96a36cee643aa.gif',
                  'https://rrp-production.loritta.website/img/29c239652ced1d4abb8d4dee8171fe267b80d2e4.gif',
                  'https://cdn.weeb.sh/images/Skc42pdv-.gif',
                  'https://cdn.weeb.sh/images/Bkk_hpdv-.gif']

        mensagens_de_beijo = [
            f"<@{ctx.author.id}> beija suavemente <@{membro.id}> com carinho! 😘",
            f"<@{ctx.author.id}> dá um beijo suave em <@{membro.id}>. 💋",
            f"<@{ctx.author.id}> rouba um beijo de <@{membro.id}>! 😚",
            f"<@{ctx.author.id}> e <@{membro.id}> trocam um beijo apaixonado! 💏",
            f"Com um sorriso, <@{ctx.author.id}> beija suavemente <@{membro.id}>. 😊",
            f"<@{ctx.author.id}> inclina-se e beija <@{membro.id}> apaixonadamente. 💖",
            f"<@{ctx.author.id}> dá um beijo rápido em <@{membro.id}> e sai correndo! 😄",
            f"<@{ctx.author.id}> e <@{membro.id}> trocam beijos carinhosos sob as estrelas. 🌟💏",
            f"De repente, <@{ctx.author.id}> surpreende <@{membro.id}> com um beijo caloroso! 🔥💋",
            f"<@{ctx.author.id}> envia um beijo virtual para <@{membro.id}>! 😘💻",
            f"<@{ctx.author.id}> beija a bochecha de <@{membro.id}> com ternura. 😊💕",
            f"<@{ctx.author.id}> e <@{membro.id}> se abraçam e compartilham um beijo doce. 🤗💖",
            f"<@{ctx.author.id}> dá um beijo suave na testa de <@{membro.id}>. 🙇‍♀️💋",
            f"<@{ctx.author.id}> e <@{membro.id}> se beijam apaixonadamente no pôr do sol. 🌅💏"]

        escolha_imagem = choice(beijos)
        escolha_beijo = choice(mensagens_de_beijo)

        await responda(membro.mention)
        embed = discord.Embed(
            description=f'😍 **{escolha_beijo}**',
            color=0xf46868
        )
        embed.set_image(url=escolha_imagem)
        embed.set_author(name='Beijos ❤️')
        embed.set_footer(text='Lindo casal 😘🔥', icon_url=bot.user.avatar)
        await responda(embed=embed)
    except AttributeError:
        await responda(f'Oh-oh! Parece que <@{ctx.author.id}> está tentando dar um beijo no ar!'
                       ' 💋💨 Espero que o vento retribua o carinho! 🌬️😄\n'
                       f'<@{ctx.author.id}> Voce precisa menciona alguém!')


@bot.command('carinho')
async def cafune(ctx, membro: discord.Member = None):
    try:
        cafunes = [
            'https://cdn.weeb.sh/images/ByXs1AYKW.gif',
            'https://cdn.weeb.sh/images/B1Qb88XvW.gif',
            'https://cdn.weeb.sh/images/r1VzDkmjW.gif',
            'https://rrp-production.loritta.website/img/fe4f69d13d1ea05aa29699ef68ea6d4bb2dd251e.gif',
            'https://rrp-production.loritta.website/img/51b6f4c8cf8d32b2ded7b4617cf2be00d25e3994.gif',
            'https://rrp-production.loritta.website/img/72f21b39cacbb2702c461958d6e9fb599a11809a.gif',
            'https://rrp-production.loritta.website/img/97a6bc6994b8d37ef255c592aa8003fe956a350b.gif',
            'https://rrp-production.loritta.website/img/e97de066504a44aa7d1563bbed9404b34f38c04c.gif',
            'https://rrp-production.loritta.website/img/d0a9ef1555dcdb24e7d17087283c96822549ad79.gif']

        mesagem_cafune = [
            f"Com carinho, <@{ctx.author.id}> faz um cafuné suave na cabeça de <@{membro.id}>. 🐾💤",
            f"Sente só a suavidade desse cafuné de <@{ctx.author.id}> em <@{membro.id}>. 😊💆‍♀️",
            f"Os dedos mágicos de <@{ctx.author.id}> transformam um cafuné em uma experiência"
            f" celestial para <@{membro.id}>. ✨🐱",
            f"<@{ctx.author.id}> dá um cafuné relaxante em <@{membro.id}>, afastando qualquer estresse. 🌼🌸",
            f"Os cabelos de <@{ctx.author.id}> são perfeitos para um cafuné em <@{membro.id}>. 😄👐",
            f"Cafuné de <@{ctx.author.id}> em <@{membro.id}> é como uma poção mágica que acalma a alma. 🪄✨",
            f"O cafuné de <@{ctx.author.id}> é tão bom que <@{membro.id}> não quer que pare. 😍🐾",
            f"Sob o toque suave de <@{ctx.author.id}>, <@{membro.id}> sente um cafuné tão"
            f" relaxante que quase adormece. 💤😊",
            f"Os dedos habilidosos de <@{ctx.author.id}> fazem maravilhas em um cafuné para <@{membro.id}>. 🙌🐾",
            f"Ninguém faz um cafuné tão reconfortante quanto <@{ctx.author.id}>. <@{membro.id}> se sente"
            f" nas nuvens. ☁️💖"]

        escolha_cafune = choice(cafunes)
        escolha_mensagem = choice(mesagem_cafune)

        await responda(membro.mention)
        embed = discord.Embed(
            description=f' **{escolha_mensagem}**',
            color=0xf46868
        )
        embed.set_image(url=escolha_cafune)
        embed.set_author(name='Cafuné 😁️')
        embed.set_footer(text='Ameioooo 😇💕', icon_url=bot.user.avatar)
        await responda(embed=embed)

    except ValueError:
        await responda(f'Oh-oh! Parece que <@{ctx.author.id}> está tentando fazer carinho no ar! '
                       f'🌬️💨 Talvez o vento seja o único que receberá o cafuné hoje! 😄\n'
                       f'<@{ctx.author.id}> Voce precisa menciona alguém!')
    except AttributeError:
        await responda(f'Oh-oh! Parece que <@{ctx.author.id}> está tentando fazer carinho no ar! '
                       f'🌬️💨 Talvez o vento seja o único que receberá o cafuné hoje! 😄\n'
                       f'<@{ctx.author.id}> Voce precisa menciona alguém!')


"""@bot.command('traduzir')
async def translate(ctx, *, frase):
    translator = Translator()
    thumb = 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/1024px-Google_Translate_logo.svg.png'

    idioma_origem = translator.detect(frase).lang
    idioma_nome_completo = {
        'af': 'Africâner', 'sq': 'Albanês', 'am': 'Amárico', 'ar': 'Árabe',
        'hy': 'Armênio', 'az': 'Azerbaijano', 'eu': 'Basco', 'be': 'Bielorrusso',
        'bn': 'Bengali', 'bs': 'Bósnio', 'bg': 'Búlgaro', 'ca': 'Catalão', 'ceb': 'Cebuano', 'ny': 'Chichewa',
        'zh-CN': 'Chinês (simplificado)', 'zh-TW': 'Chinês (tradicional)', 'co': 'Córsico', 'hr': 'Croata',
        'cs': 'Tcheco', 'da': 'Dinamarquês', 'nl': 'Holandês', 'eo': 'Esperanto', 'et': 'Estoniano', 'tl': 'Filipino',
        'fi': 'Finlandês', 'fr': 'Francês', 'fy': 'Frísio', 'gl': 'Galego', 'ka': 'Georgiano', 'de': 'Alemão',
        'el': 'Grego', 'gu': 'Guzerate', 'ht': 'Haitiano', 'ha': 'Hauçá', 'haw': 'Havaiano', 'iw': 'Hebraico',
        'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Húngaro', 'is': 'Islandês', 'ig': 'Igbo', 'id': 'Indonésio',
        'ga': 'Irlandês', 'it': 'Italiano', 'ja': 'Japonês', 'jw': 'Javanês', 'kn': 'Canarim', 'kk': 'Cazaque',
        'km': 'Khmer', 'ky': 'Quirguiz', 'ko': 'Coreano', 'ku': 'Curdo', 'la': 'Latim', 'lv': 'Letão', 'lt': 'Lituano',
        'lb': 'Luxemburguês', 'mk': 'Macedônio', 'mg': 'Malgaxe', 'ms': 'Malaio', 'ml': 'Malaiala', 'mt': 'Maltês',
        'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongol', 'my': 'Birmanês', 'ne': 'Nepalês', 'no': 'Norueguês',
        'ps': 'Pachto', 'fa': 'Persa', 'pl': 'Polonês', 'pt': 'Português', 'pa': 'Punjabi', 'ro': 'Romeno',
        'ru': 'Russo', 'sm': 'Samoano', 'gd': 'Gaélico escocês', 'sr': 'Sérvio', 'st': 'Sesoto', 'sn': 'Shona',
        'sd': 'Sindi', 'si': 'Cingalês', 'sk': 'Eslovaco', 'sl': 'Esloveno', 'so': 'Somali', 'es': 'Espanhol',
        'su': 'Sundanês', 'sw': 'Suaíli', 'sv': 'Sueco', 'tg': 'Tadjique', 'ta': 'Tâmil', 'tt': 'Tártaro',
        'te': 'Telugu', 'th': 'Tailandês', 'tr': 'Turco', 'tk': 'Turcomano', 'uk': 'Ucraniano', 'ur': 'Urdu',
        'ug': 'Uigur', 'uz': 'Uzbeque', 'vi': 'Vietnamita', 'cy': 'Galês', 'xh': 'Xhosa', 'yi': 'Yiddish',
        'yo': 'Yoruba', 'zu': 'Zulu',
    }

    idioma_origem_nome_completo = idioma_nome_completo.get(idioma_origem, 'ingles')

    a = translator.translate(frase, dest='pt')
    embed = discord.Embed(
        title='**Tradutor PT-BR**',
        description=f'Desenvolvedor poliglota aqui! Meu código é tão esperto que até traduz para idiomas que ainda não'
                    f' foram inventados. Se você precisa de uma tradução para qualquer idioma existente ou imaginável,'
                    f' estou pronto para o desafio! 😉\n'
                    f'\n> * **Texto em {idioma_origem_nome_completo}:** *"{frase}"*\n'
                    f'\n> * **Traduzido para Pt-br:** *"{a.text}"*',
        color=0x85fff5
    )
    embed.set_footer(text='Obrigado e volte sempre 😇', icon_url=bot.user.avatar)
    embed.set_author(name='Abrindo o dicionário 📖🖋️')
    embed.set_thumbnail(url=thumb)
    await responda(embed=embed)"""


@bot.command('piada')
async def lol(ctx):
    piadas = [
        "O que a impressora disse para a outra? Essa folha é sua ou é uma impressão minha?",
        "Por que a galinha atravessou a estrada? Para chegar do outro lado!",
        "O que o zero disse para o oito? Bonito cinto!",
        "Qual é o animal mais antigo? A zebra, porque está sempre listada na história!",
        "O que um peixe disse para o outro? Nada, eles não podem falar, eles são peixes!",
        "Qual é o café mais perigoso do mundo? O ex-preso!",
        "O que o pente disse para o cabelo? Não se preocupe, eu vou passar por cada um de vocês!",
        "Qual é o contrário de volátil? Vem cá, sobrinho!",
        "Que raça de cachorro pula mais alto que um prédio? Qualquer uma, ué. Prédio não pula.",
        "Qual é o alimento mais sagrado que existe? O amém doím.",
        "Por que o arqueólogo escolheu essa profissão? Porque a carreira dele estava em ruínas.",
        "Por que os pássaros voam para o sul? Porque é muito longe para ir andando! ",
        "Todas as frutas foram passar as férias na montanha, menos o mamão. Porque o mamão foi papaia!",
        "Por que a Coca-Cola e a Fanta se dão muito bem? Porque se a Fanta quebra, a Coca, Cola!",
        "O que é um piolho na cabeça de um careca? Um sem terra!",
        "Por que o menino estava falando ao telefone deitado? Para não cair a ligação",
        "Era uma vez um pintinho que se chamava Relam. Toda vez que chovia, Relam piava!",
        "O que o tijolo falou para o outro? Há um ciumento entre nós",
        "Por que o Batman colocou o bat-móvel no seguro? Porque ele tem medo que Robin!",
        "Por que o policial não usa sabão? Porque ele prefere deter gente.",
        "O que é um pontinho preto no avião? Uma aeromosca.",
        "Qual é a galinha que cai no chão e surta? A galinha cai i pira.",
        "Qual é a diferença entre o lago e a padaria? No lago há sapinhos e na padaria assa pão.",
        "Qual é o melhor tratamento para pessoas que sofrem de queda constante? Para-quedismo",
        "Um tênis foi jogado ao mar e afundou. Qual o nome do filme? Titanike.",
        "Por que o livro de matemática ficou triste? Porque tinha muitos problemas.",
        "O que a fechadura falou para a chave? Vamos dar uma voltinha?",
        "Você já ouviu falar do cara que roubou o calendário? Ele pegou 12 meses!",
        'O que a parede disse para o teto? “Eu te cubro!”'
    ]
    escolher_piada = choice(piadas)

    embed = discord.Embed(
        title='Piada do Dia:  📨  ',
        description=escolher_piada,
        color=0xfbfbfb
    )
    embed.set_author(name='')
    embed.set_footer(text='- O único bot que nunca perde a piada! 🃏😄', icon_url=bot.user.avatar)
    await responda(embed=embed)

"""
@bot.command('mapas')
async def maps(ctx):
    mapas = [
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232480400740423/Screenshot_20231212-172232_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=484849aa0efd6a37dd28881fa69af18b60b24cd2967edd30088568c932f8771d&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232481378017353/Screenshot_20231212-172227_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=0b2dfabb2fce88a6943bf09d1a4e913322018b8a9b7513cd3a57c8fd1510e61b&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232481885519963/Screenshot_20231212-172223_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=f9457a2a58b659c9acae1b3418062d3114060fa6366560e06aca00fc1ed2dfec&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232482443366494/Screenshot_20231212-172217_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=53eb78270be2fb48719701f5b06455e320a155f1cf5187993f6ba11842539f9e&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232482753749074/Screenshot_20231212-172213_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=951db2641b980a9aee5da07f1114243a5aa49843eed5d44177e51402e69e8b51&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232483030564884/Screenshot_20231212-172208_Brawl_Stars.jpg?ex=658b3971&is=6578c471&hm=a8624837258f01bf0977228807b4516a9e2662152adfcc5e676a32f3f58c464f&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232483458392144/Screenshot_20231212-172202_Brawl_Stars.jpg?ex=658b3972&is=6578c472&hm=647352b24b577a091a5bc652831cb1e409b7ec33419f4471b61728a12f4f4cbb&',
        'https://cdn.discordapp.com/attachments/1183731371932385401/1184232483802316972/Screenshot_20231212-172158_Brawl_Stars.jpg?ex=658b3972&is=6578c472&hm=9fceff9f279323a09d902a0fb4cabd974b69b3a3ff756764410fe2afbfcea0a4&']

    for c in mapas:
        await responda(c)


@bot.command('sorteiom')
async def sort(ctx):
    mapas = ['ketchup',
             'understar',
             'ry_',
             'psiko',
             'gabr',
             'henri',
             'ronnie',
             'gustavo',
             'kaua']
    escolha = choice(mapas)
    embed = discord.Embed(
        title='Vamos sortear um vencedor pro evento de hoje',
        description=f'E a vencedor foi: {escolha}'
    )
    await responda(embed=embed)


@bot.command('times')
async def team(ctx):
    times = ['RKW', 'Las Patetas', 'Alcatraz', 'Alerguminos', 'Lobos das Trevas', 'GGG', 'Portuguesa Esports']
    for c in times:
        await responda(c)


@bot.command('surpresa1')
async def surprise(ctx):
    embed = discord.Embed(
        title='**SURPRESA 1/6**',
        description='Você acaba de ganhar 1 mês do Discord Nitro Advanced!! \n\nAmor, vc vai precisar usar um cartão'
                    'de crédito pra resgatar, o discord vai faazer uma cobrança, pra verificar se o cartão é válido, '
                    'e vai devolver o valor cobrado!!! \n\n**Te amoooooooooo**\n'
                    '\n https://discord.com/billing/partner-promotions/1180231712274387115/eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..8BzJB7V4wYKgQotE.m7lvt-06my5IAgdCmcDWe6V2AtVvn5sZgDDSWUjQ7OYwM7aqgP4bVEUcSd7lsiGRRAKTz8Ar9lbjbTz63bmI2k7yAnX2QK2pKEHmhRssnkcCMJnDvyIJMM3keN4TlqPvZHmSGrKW9zx1m7noUSPSnlXfrmMRUscZhT9YNRj47oZB5LmBrf0dSd7fGa3hCRpBEzmu-HRBV5K6Lun46Zub4phfVi83T4wCD-uKaSpHtPVG0OsgBQ.W1aK2dKBqzddUub1AcNqUg',
        color=0x7c2bc1
    )
    await responda(embed=embed)


@bot.command('chaves')
async def keys(ctx):
    times = ['Las Patetas', 'RKW', 'Lobos das Trebas', 'GGG', 'Portuguesa Esports', 'Alcatraz', 'Alerguminos']
    sorteio = choice(times)
    sorteio2 = choice(times)
    embed = discord.Embed(
        title='Chaveamento do Campeonato',
        description='Preparem-se para um chaveamento tão épico que até a Matemática vai ficar com inveja dos números!'
                    ' E lembrem-se, quem "sabe faz ao vivo, quem não sabe... assiste o replay! Boa sorte a todos e que'
                    ' a conexão com a sorte esteja a seu favor!'
    )
    await responda(embed=embed)
    sleep(1)
    await responda('**CONTAGEM REGRESSIVA**')
    sleep(1)
    await responda('3')
    sleep(1)
    await responda('2')
    sleep(1)
    await responda('1')
    sleep(1)
    await responda('É chegada a hora!!')
    sleep(1)
    embed2 = discord.Embed(
        title='Confronto: ',
        description=f'{sorteio} x {sorteio2}'
    )
    await responda(embed=embed2)


@bot.command('evento')
async def event(ctx):
    imagem = 'https://cdn.discordapp.com/attachments/843613946501136424/1216085137129869393/Imagem_do_WhatsApp_de_2024-03-09_as_15.07.33_2d15e99f.jpg?ex=65ff1a8a&is=65eca58a&hm=e89ace80bbf9ec8ff32db06d647981900c701a19b350e643ff6dee32f3a091a3&'
    embed = discord.Embed(
        title='Evento do Clube \n',
        description=('**ATENÇÃO CLUBE, É HORA DE MOSTRAR SUAS HABILIDADES!**\n'
                     '\nPreparem-se para o **Torneio de Troféus do Clube**! Uma competição épica de 1 mês de duração, onde apenas os membros do nosso clube podem participar. O objetivo é simples: **ganhar o máximo de troféus possível** e se tornar o **campeão supremo!**'
                     '\n'
                     '\n**Regras do Torneio:**\n'

                     '\n**Duração:** 1 mês (começa dia 10/03/2024 e termina dia 10/04/2024);'
                     '\n**Participantes:** Todos os membros do clube;'
                     '\n**Objetivo:** Ganhar o máximo de troféus;'
                     '\n**Sistema de Pontuação:**\n'
                     '\n> * Cada troféu conquistado vale 1 ponto;'
                     '\n> * Perder troféus subtrai pontos.\n'
                     '\n**Proibição:**\n'
                     '\n> * Usar exploits ou qualquer forma de trapaça;'
                     '\n> * Comportamentos antidesportivos.\n'
                     '\n**Premiação:**\n'

                     '\n**1º lugar:** Brawl Pass da Temporada Atual;'
                     '\n**2º lugar:** 50k de sonhos;'
                     '\n**3º lugar:** senta e chora.\n'
                     '\n**Como participar:**\n'

                     '\n> * Basta ser membro do nosso clube durante o período do torneio;'
                     '\n> * Jogue Brawl Stars e ganhe o máximo de troféus que conseguir;'
                     '\n> * Acompanhe a classificação no canal do Discord do clube;'
                     '\n> * Preparem seus brawlers, afiem suas habilidades e que vença o melhor!\n'

                     '\n**Dúvidas?**\n'

                     '\n*Consulte o canal de regras do Discord do clube ou envie uma mensagem privada para o Pedro no Discord*\n'
                     '\n**___Boa sorte a todos!___**'
                     ),
        color=0x9f9fff
    )
    embed.set_author(name='Evento', icon_url=bot.user.avatar)
    embed.set_footer(text='Já formem suas equipes e se preparem! ')
    embed.set_image(url=imagem)
    await responda(embed=embed)"""







"""@bot.command('mat')
async def math(ctx):
    continuar = ''
    pontos = 0
    while continuar != 0:
        class Calcular:

            def __init__(self, dificuldade):
                self.__dificuldade = dificuldade
                self.__valor1 = self._gerar_valor
                self.__valor2 = self._gerar_valor
                self.__operacao = randint(1, 3)
                self.__resultado = self._gerar_resultado

            @property
            def dificuldade(self):
                return self.__dificuldade

            @property
            def valor1(self):
                return self.__valor1

            @property
            def valor2(self):
                return self.__valor2

            @property
            def operacao(self):
                return self.__operacao

            @property
            def resultado(self):
                return self.__resultado

            def __str__(self):
                op = ''
                if operacao == 1:
                    op = 'somar'
                elif operacao == 2:
                    op = 'diminuir'
                elif operacao == 3:
                    op = 'multiplicar'
                else:
                    op = 'Operação desconhecida'
                return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

            @property
            def _gerar_valor(self):
                if self.dificuldade == 1:
                    return randint(0, 10)
                elif self.dificuldade == 2:
                    return randint(0, 100)
                elif self.dificuldade == 3:
                    return randint(0, 1000)
                elif self.dificuldade == 4:
                    return randint(0, 10000)
                else:
                    return randint(0, 100000)

            @property
            def _gerar_resultado(self):
                if self.operacao == 1:  # somar
                    return self.valor1 + self.valor2
                elif self.operacao == 2:  # diminuir
                    return self.valor1 - self.valor2
                else:
                    return self.valor1 * self.valor2

            @property
            def _op_simbolo(self):
                if self.operacao == 1:
                    return '+'
                elif self.operacao == 2:
                    return '-'
                else:
                    return 'x'

            def mostrar_operacao(self):
                return f'{self.valor1} {self._op_simbolo} {self.valor2} = ?'

        embed = discord.Embed(
            title='Informe o nível de difículdade desejado:',
            description=':one: -> Fácil\n:two: -> Médio\n:three: -> Difícil\n:four: -> Impossível'
        )
        embed.set_author(name='Dificuldade 🎈', icon_url=bot.user.avatar)
        embed.set_footer(text='Digite o número escolhido.')

        await responda(embed=embed)

        dificuldade_a = int(1)
        dificuldade_a = await bot.wait_for('message')
        dificuldade = int(dificuldade_a.content)

        calc = Calcular(dificuldade)

        embed2 = discord.Embed(
            title='Digite o resultado da seguinte operação:\n',
            description=f'> **{calc.mostrar_operacao()}**\n'
                        f'\n'
        )
        embed2.set_author(name='Operação ⌚', icon_url=bot.user.avatar)
        embed2.set_footer(text='⌛ Acerte a resposta.')

        await responda(embed=embed2)

        pontuacao = {}

        resultado = 0
        while calc.resultado != resultado:
            while resultado != int:
                try:
                    resultado_a = await bot.wait_for('message')
                    resultado = int(resultado_a.content)
                except ValueError:
                    resultado_a = await bot.wait_for('message')
                    resultado = int(resultado_a.content)
                if resultado == int:
                    break
                break

            if calc.resultado == resultado:
                embed_calc = discord.Embed(
                    title='✨ Resposta Correta!',
                    description=f'Parabéns, você é um gênio da matemática! 🎩✨ Sua resposta está correta e você está'
                                f' voando nas operações! Continue assim e você vai resolver todas as equações'
                                f' do universo. 🚀💯\n'
                                f'\nA resposta da operação: **{calc.valor1} {calc._op_simbolo} {calc.valor2} = {calc.resultado}**',
                    color=0x26ff00
                )
                embed_calc.set_author(name='Parabéns 🎉', icon_url=bot.user.avatar)
                embed_calc.set_footer(text='Vamos continuar?')
                await responda(embed=embed_calc)

                pontos += 1
                lista = []
                pontuacao[ctx.author.mention] = pontos
                for nome, pontos in pontuacao.items():
                    embed_pont = discord.Embed(
                        title='🏆 Pontuação',
                        description=f'{nome}: {pontos} pontos',
                        color=0xffff00
                    )
                    embed_pont.set_footer(text='Recomeço em 5 segundos ⏱️')
                    await responda(embed=embed_pont)
                break
            else:
                await responda('Resposta errada!')

        embed_fim = discord.Embed(
            title='Deseja continuar?',
            description=':one: -> Sim\n:zero: -> Não'
        )
        embed_fim.set_author(name='Fim', icon_url=bot.user.avatar)
        embed.set_footer(text='Digite a opção escolhida.')

        await responda(embed=embed_fim)
        continuar_a = await bot.wait_for('message')
        continuar = int(continuar_a.content)

        if continuar == 0:
            await responda(f'Você finalizou com {pontos} ponto(s).')
            await responda('Até a próxima!')
            break
"""






@bot.command('regras')
async def rules(ctx):
    embed = discord.Embed(
        title='',

        description=f'Aqui estão as regras do nosso servidor, não estão todas, mas em sua maioria. Contamos com'
                    f' a compreensão e ética de vcs para que não precisemos aumentar essa lista. Confio em vcs :wink:\n'
                    f'\n> *  :no_entry_sign: Palavrões são sim permitidos, desde que sejam usados de forma irônica ou'
                    f' sarcástica, não deixando membros ofendidos, tristes, contrangidos ou bravos;\n'
                    f'\n> *  :no_entry_sign: Use o canal certo para cada tipo de situação.\n'
                    f'\n> * :no_entry_sign: Respeite os outros de acordo com sua religião, ou escolhas, não julgue'
                    f' e nem ofenda;\n'
                    f'\n> * :no_entry_sign:Não faça nenhum spam/flood, seja de mensagens repetidas ou aleatórias,'
                    f' imagens, vídeos, gifs.... Não faça nada que polua o chat visualmente.;\n'
                    f'\n> * :no_entry_sign: Proibido link de divulgação sem permissão;\n'
                    f'\n> * :no_entry_sign: Fotos de conteúdo adulto não é permitido, e nem referências,'
                    f' por acaso se forem irônico ou sarcástico é permitido;\n'
                    f'\n> * :no_entry_sign: NÃO poste NSFW ou NSFL, mantenha o servidor seguro sem nada que comprometa'
                    f' a segurança do servidor, sem conteúdo +18, o linguajar inadequeado também conta.\n'
                    f'\n> * :no_entry_sign: Não será tolerado qualquer tipo de preconceito. Lembrando que isso inclui'
                    f' apologia a movimentos que tenham ideais racistas, homofóbicos ou de qualquer tipo de'
                    f' discriminação;\n'
                    f'\n> * :no_entry_sign: Não divulgue informações suas ou de outros membros, tais como nome, idade,'
                    f' id de usuário, sem o consentimento do membro em questão.\n'
                    f'\n> * :no_entry_sign: Reporte caso algo aconteça, e dê provas reais.\n'
        ,
        color=0xff0000
    )
    embed.set_author(name='Bem Vindo ao servidor The Winner´s', icon_url=bot.user.avatar)
    embed.set_footer(text='Atualizado em ・ 01/01/2024')
    await responda(embed=embed)


bot.run(TOKEN)