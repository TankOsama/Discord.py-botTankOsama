import discord#جلب مكتبة الديسكورد
from discord.ext import commands#جلب الكومندات
from discord.ext.commands import has_permissions, CheckFailure#جلب البرمشنز
import datetime#جلب مكتبة معرفة التاريخ والوقت
import random#جلب مكتبة راندوم
#################################################################################
client = commands.Bot(command_prefix = '.')#تعيين متغير للبوت كوماند البرفيكس
client.remove_command('help')#حذف كوماند هلب لاستبداله بكوماند اخر لللهب بشكل افضل
gg = (datetime.datetime.now())# متغير لمعرفة تاريخ اليوم والوقت

book_answer = ['ايه',"لا","ممكن","جرب بنفسك","ليش لا","ما اتوقع انك جاد","هل انت متأكد","هل انت مجنون؟","راجع نفسك","انظر ماذا سيقدم لك المستقبل",
"اظن انك على حق"]#اجوبة كتاب الاجابات
##################################################################################################
bad_words = [] #write your bad words اكتب كلمات وسخة لفلترتها
             


bott = ["bot",'يا بوت',"بوت","Bot"]


##################################################################################################
@client.event#صنع الايفنت
async def on_ready():#بناء الفنكشن
    print('bot is ready.')#المخرجات حينما يشتخل البوت
#################################################################################################
#كوماند إظهار بنق البوت

@client.command(pass_context=True)#صنع الكوماند
async def ping(ctx,message="hi"):#صنع الفنكشن
    embed1 = discord.Embed(#(الرسالة المنسقة)صنع الامبيد
        title="Ping",#العوان
        description=(f"{round(client.latency * 1000)}ms"),#الوصف
        colour= discord.Colour.orange()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await ctx.send(embed=embed1)#إرسال الامبيد
##################################################################################################
@client.command(pass_context=True)#صنع الامر
async def answer(ctx, *,message):# صنع الفكشن او الكوماند لكتاب الاجوابة
    embed1 = discord.Embed(#الامبيد
        title=f"سؤالك:{message}",#العنوان
        description=(f"الجواب:{random.choice(book_answer)}"),#الجواب
        colour= discord.Colour.orange()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    if any(bad_word in message for bad_word in bad_words) == False:#تصفية الكلام الوسخ
        await ctx.send(embed=embed1)#ارسال الامبيد في حالة عدم وجود سب
    else:#اذا وجد سب افعل
        await ctx.send('اتوقع انه ابوك')#ارسل الرد الواظح امامكم
##################################################################################################
@client.command(pass_context=True)#صنع كوماند المساعدة
async def help(ctx):#صنع الكوماند
    embed1 = discord.Embed(#الامبيد
        title="الاوامر",#العنوان
        description=('*.ping:لإظهار بنق البوت*\n\n'
                     '*.kick:إعطاء طرد بشرط امتلاك رتبة إدارة*\n\n'
                     '*.ban:تبنيد شخص بشرط إمتلاك رتبة ادارية*\n\n'
                     '*.unban:لفط الباند عن اي شخص بشرطة امتلاك رتبة إدارية*\n\n'
                     '*.clear:لحذف الرسائل بشرط إمتلاك رتبة أدارية تصل إلى 100 رسالة تستطيع حذفها*\n\n'#الوصف اللي هو وصف اوامر البوت
                     '*.say:لجعل البوت يكتب اي شي بشرط ان يكون لديك رتبة إدارية*\n\n'
                     '*.Time:لإظهار التاريخ والوقت ملاحظة:تـاريــخ مــدــيــنــة الريـــاض*\n\n'
                     '*.avatar:إظهار افاتر اي شخص*\n\n'
                     '*.answer:نفس فكرة كتاب الاجابات*\n\n'
                     '*.addallMemberrole:إعطاء الكل رتبة محددة*\n\n'
                     '*.removeallMemberrole:حذف من الكل رتبة محددة*\n\n'
                     '*للإقتراحات او الشكوى تواصل مع @TankOsama#1111*'),
        colour= discord.Colour.dark_grey()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await ctx.send(embed=embed1)#إرسال الامبيد


########################################################################################################
@client.command(pass_context=True)#الكوماند
async def Time(ctx):#صنع كوماند الوقت اللي هو يعطيك التاريخ والوقت
    embed1 = discord.Embed(#الامبيد
        title="الوقت الان",#العنوان
        description=(f"الوقت هو {gg}"),#الوقت
        colour= discord.Colour.orange()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await ctx.send(embed=embed1)#إرسال الامبيد

########################################################################################################
@client.command(pass_context=True)#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def say(ctx, *, message):# الكومان او الفنكشن وهو يجعل البوت يكتب اي شي يريده
    embed1 = discord.Embed(#الامبيد
        title=f"مرسل من قبل {ctx.author}",#العنوان
        description=(f"الرسالة هي:\n{message}"),#الوقت
        colour= discord.Colour.orange()#اللون
    )
    embed1.set_thumbnail(url=ctx.author.avatar_url)
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    if any(ws5 in message for ws5 in bad_words) == False:#فلترة السب
        await ctx.send(embed=embed1)#ارسال الرسالة بعد التحقق من عندم وجود سب
    else:#اذا وجد سب
        await ctx.send("تعذر إرسال الرسالة بسبب الالفاظ الخادشة")#إرسال هذه الرسالة في حال وجود سب
##################################################################################################

@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def kick(ctx, member : discord.Member, *,reason=None):#الكوماند او الفنكشون وهو طرد اي شخص اذا كانت لديك الصلاحية
    embed1 = discord.Embed(#الامبد
        title="طرد",#العنوان
        description=(f"تم طرد{member}"),#رسالة انه تم طرد شخص
        colour= discord.Colour.orange()#اللون


    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await member.kick(reason=reason)#طرد الشخص
    await ctx.send(embed=embed1)#ارسال انه تم طرد الشخص
####################################################################################################
@client.command()#الكوماند
async def avatar(ctx, member : discord.Member):#الفنشكشن او الكوماند وهو عبارة عن ارسال افتار اي شخص بالسيرفر
    embed1 = discord.Embed(#الامبيد
        title="Avatar",#العنوان
        description = f"تم الطلب من قبل {ctx.author}",#ارسال الافتار والطلب تم من من
        colour= discord.Colour.orange()#اللون


    )
    embed1.set_image(url=member.avatar_url)#وضع الصورة
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await ctx.send(embed=embed1)#ارسال الامبيد
######################################################################################################
def TankCommands(commandd):
    return commandd
@client.command()#الكوماند
async def python3(ctx,*,message):#الفنشكشن او الكوماند وهو عبارة عن ارسال افتار اي شخص بالسيرفر
    if __name__ == '__main__':
        TankCommands(message)
    if TankCommands(message) == None :
        await ctx.send(TankCommands(message))  # ارسال الامبيد
    else:
        print(TankCommands(message))
####################################################################################################
@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def ban(ctx, member : discord.Member, *,reason=None):#الدالة او الكوماند وهو تبنيد اي شخص في حال كانت لديك الصلاحية
    embed1 = discord.Embed(#الامبيد
        title="باند",#العنوان
        description=(f"تم تبنيد{member}"),#الوصف
        colour= discord.Colour.orange()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    await member.ban(reason=reason)#تبنيد الشخص المراد
    await ctx.send(embed=embed1)#ارسال الامبيد
###################################################################################################
@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def unban(ctx, *, member):#الدالة وهي فك الباند عن اي شخص مبند بشرط امتلاكك الصلاحية
    banned_users = await ctx.guild.bans()#الحصول على خائمة الاشخاص المبندين
    member_name, member_discriminator = member.split('#')#تعيين الشخص المبند
    embed1 = discord.Embed(#الامبيد
        title="فك الباند",#العنوان
        description=(f"تم فك الباند{member}"),#الوصف
        colour= discord.Colour.orange()#اللون
    )
    embed1.add_field(name="𝐁𝐨𝐭 𝐁𝐲 𝐓𝐚𝐧𝐤𝐎𝐬𝐚𝐦𝐚#𝟏𝟏𝟏𝟏", value="\u200b", inline=False)
    for ban_entry in banned_users:#الرجوع لكل قائمة الباند
        user = ban_entry.user##تعيين الشص المبند


        if (user.name, user.discriminator) == (member_name, member_discriminator):#شرط للتحقق ان الشخص الممنشن مبند
            await ctx.guild.unban(user)#فك الباند
            await ctx.send(embed=embed1)#إراسال الرسالة
            return#

####################################################################################################
@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def clear(ctx, amount=100):#صنع الدالة وهي حذف مقدار معين من الرسائل يصل إلى 100 اذا كانت لديك الصلاحية
    try:#محاولة لتجنب الاخطاء
        await ctx.channel.purge(limit=amount)#حذف الرسائل
    except:#اذا لم تنجح
        await ctx.send("هناك خطأ رجاء التواصل مع أسامة لمعرفة التفاصيل")#رسالة الخطأ
##########################################################################################################################
@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def addallMemberrole(ctx,*,role):#صنع الدالة وهي حذف مقدار معين من الرسائل يصل إلى 100 اذا كانت لديك الصلاحية
        for i in client.get_all_members():
            await i.add_roles(discord.utils.get(i.guild.roles, name=role))
###########################################################################################################################
@client.command()#الكوماند
@commands.has_permissions(administrator=True)#الصلاحية بحيث لا احد يمكنه استخدام الكوماند الا اذا كان عنده ادمنستريتور
async def removeallMemberrole(ctx,*,role):#صنع الدالة وهي حذف مقدار معين من الرسائل يصل إلى 100 اذا كانت لديك الصلاحية
        for i in client.get_all_members():
            await i.remove_roles(discord.utils.get(i.guild.roles, name=role))

##########################################################################################################################
@client.event#صنع الافينت
async def on_message(message):#الدالة وهي عند ارسال رسالة
    await client.process_commands(message)
    if message.content.find("السلام عليكم") != -1 or message.content.find("السلام عليكم ورحمة الله") != -1 or message.content.find("السلام عليكم ورحمة الله وبركاته") != -1:
        await message.channel.send("```وعليكم السلام ورحمة الله وبركاته```")
    elif message.content == "سكرين":
        await message.channel.send("""https://www.discordapp.com/channels/653286719025840158/655436097848999969""")                       #الرسالات والردون
    elif message.content == "!ping":
        await message.channel.send(f'بنقك هو {round(client.latency *1000)}ms')
    if any(bad_word in message.content.lower()  for bad_word in bad_words)and any(botcall in message.content.lower()  for botcall in bott) == False:
        await message.channel.send(f"{message.author.mention}الرجاء عدم السب")
    if any(bad_word in message.content.lower()  for bad_word in bad_words )and any(botcall in message.content.lower()  for botcall in bott):
        await message.channel.send(f"{message.author.mention}خير ان شاء الله")
#########################################################################################################################
client.run("YourToken")#تشغيل البوت
