import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import requests
import textwrap
client=commands.Bot(command_prefix="/")
@client.command()
async def makequote(ctx,cmd=None):
    msg=ctx.message.reference
    id=msg.message_id
    message=await ctx.fetch_message(id)
    ico=message.author.avatar_url
    url = ico
    file_name = "icon.jpeg"
    await ctx.reply("生成しています")

    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as aaa:
      aaa.write(image)
    if message.content.replace("\n","").isascii():
        para = textwrap.wrap(message.clean_content, width=26)
    else:
        para = textwrap.wrap(message.clean_content, width=13)
    icon=Image.open("icon.jpeg")
    haikei=Image.open("grad.jpeg")
    black=Image.open("black.jpeg")
    w,h=(680,370)
    w1,h1=icon.size
    haikei=haikei.resize((w,h))
    black=black.resize((w,h))
    icon=icon.resize((h,h))
    if cmd=="color":
      haikei=haikei.convert("L")
      new=Image.new(mode="RGBA",size=(w,h))
      icon=icon.convert("RGBA")
      black=black.convert("RGBA")
    if not cmd:
      haikei=haikei.convert("L")
      new=Image.new(mode="L",size=(w,h))
      icon=icon.convert("L")
      black=black.convert("L")
    icon=icon.crop((40,0,680,370))
    new.paste(icon)
    sa=Image.composite(new,black,haikei)
    draw = ImageDraw.Draw(sa)
    fnt = ImageFont.truetype('higashiume.ttf',28) 
    w2,h2=draw.textsize("a",font=fnt)
    i=(int(len(para)/2)*w2)+len(para)*5
    current_h, pad = 120-i, 0
    for line in para:
      if message.content.replace("\n","").isascii():
        w3,h3=draw.textsize(line.ljust(int(len(line)/2+11)," "),font=fnt)
        draw.text((11*(w - w3) / 13+10, current_h+h2), line.ljust(int(len(line)/2+11)," "), font=fnt,fill="#FFF")
      else:
        w3,h3=draw.textsize(line.ljust(int(len(line)/2+5),"　"),font=fnt)
        draw.text((11*(w - w3) / 13+10, current_h+h2), line.ljust(int(len(line)/2+5),"　"), font=fnt,fill="#FFF")
      current_h += h3 + pad
    dr=ImageDraw.Draw(sa)
    font = ImageFont.truetype('nijimi.otf',15)
    authorw,authorh=dr.textsize(f"-{str(message.author)}",font=font)
    dr.text((480-int(authorw/2),current_h+h2+10),f"-{str(message.author)}",font=font,fill="#FFF")
    sa.save("te.png")
    file=discord.File("te.png")
    await ctx.send(file=file)
