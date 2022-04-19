import discord
from discord.ext import commands
client=commands.Bot(command_prefix="/")
@client.command()
async def reply(ctx):
    msg=ctx.message.reference
    id=msg.message_id
    message=await ctx.fetch_message(id)
    ico=message.author.avatar_url
    url = ico
    file_name = "icon.jpeg"
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as aaa:
      aaa.write(image)
    def adjust(content):
      msg=""
      for con in content:
        if len(msg)%9==8:
          msg+="\n"
        msg+=con
      return msg
    icon=Image.open("icon.jpeg")
    haikei=Image.open("grad.jpeg")
    black=Image.open("black.jpeg")
    w,h=(680,370)
    haikei=haikei.convert("L")
    haikei=haikei.resize((w,h))
    black=black.resize((w,h))
    new=Image.new(mode="L",size=(w,h))
    icon=icon.resize((h,h))
    icon=icon.crop((40,0,680,370))
    icon=icon.convert("L")
    new.paste(icon)
    black=black.convert("L")
    sa=Image.composite(new,black,haikei)
    draw = ImageDraw.Draw(sa)# im上のImageDrawインスタンスを作る
    fnt = ImageFont.truetype('nijimi.otf',40)
    cont=message.content
    author=message.author
    draw.text((350,120),adjust(cont),font=fnt,fill='#FFF') #fontを指定
    dr=ImageDraw.Draw(sa)
    font = ImageFont.truetype('nijimi.otf',25)
    dr.text((400,300),str(author),font=font,fill="#FFF")
    sa.save("te.png")
    file=discord.File("te.png")
    await ctx.send(file=file)
