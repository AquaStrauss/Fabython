from cmath import log
import discord
from discord.ext import commands as cmd
import math

class Rewards(cmd.Cog, name="Compounding Rewards "):

    def __init__(self, bot):
        self.client=bot

    #APYMATH
    @cmd.command(brief="Calculate the rewards from APY.")
    async def apy(self, ctx, apy:float, amount:float=None):

        if amount:
            apr = round((math.pow(1+(apy/100),1/365)-1)*365,4)
            aprDaily = apr/365

            tomorrowValue = aprDaily*amount
            firstWeekValue = (math.pow(1+aprDaily,7)-1)*amount
            firstMonthValue = (math.pow(1+aprDaily,30)-1)*amount
            firstQuarterValue = (math.pow(1+aprDaily,90)-1)*amount
            firstSemiAnnualValue = (math.pow(1+aprDaily,180)-1)*amount
            firstYearValue = (math.pow(1+aprDaily,365)-1)*amount

            roiDay = round(math.log(2,1+aprDaily))

            embed=discord.Embed(title="APY :", description=f"If you compound every days, for an APY of `{apy}%` so for an APR of `{round(apr*100,2)}%`, with `{amount}$`.\n**Your ROI will be done after `{roiDay}` days.**", color=0xf5b342)

            embed.add_field(name="-"*8+" Tomorrow "+"-"*8, value=f"**Gain : \n`{round(tomorrowValue,2)}$`\nTotal : \n`{round(tomorrowValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Week "+"-"*8, value=f"**Gain : \n`{round(firstWeekValue,2)}$`\nTotal : \n`{round(firstWeekValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Month "+"-"*8, value=f"**Gain : \n`{round(firstMonthValue,2)}$`\nTotal : \n`{round(firstMonthValue+amount,2)}$`**", inline=True)

            embed.add_field(name="-"*7+" First Quarter "+"-"*7, value=f"**Gain : \n`{round(firstQuarterValue,2)}$`\nTotal : \n`{round(firstQuarterValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*4+" First Semi-Annual "+"-"*4, value=f"**Gain : \n`{round(firstSemiAnnualValue,2)}$`\nTotal : \n`{round(firstSemiAnnualValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Year "+"-"*8, value=f"**Gain : \n`{round(firstYearValue,2)}$`\nTotal : \n`{round(firstYearValue+amount,2)}$`**", inline=True)

            await ctx.send(embed=embed)

        else:
            apr = round((math.pow(1+(apy/100),1/365)-1)*365,4)
            aprDaily = apr/365

            daily = aprDaily*100
            weekly = (math.pow(1+aprDaily,7)-1)*100
            monthly = (math.pow(1+aprDaily,30)-1)*100
            quartly = (math.pow(1+aprDaily,90)-1)*100
            semiAnnually = (math.pow(1+aprDaily,180)-1)*100
            yearly = (math.pow(1+aprDaily,365)-1)*100

            roiDay = round(math.log(2,1+aprDaily))

            embed=discord.Embed(title="APY :", description=f"If you compound every days, for an APY of `{apy}%` so for an APR of `{round(apr*100,2)}%`.\n**Your ROI will be done after `{roiDay}` days.**", color=0xf5b342)

            embed.add_field(name="-"*8+" Daily "+"-"*8, value=f"**`{round(daily,2)}%`**", inline=True)
            embed.add_field(name="-"*8+" Weekly "+"-"*8, value=f"**`{round(weekly,2)}%`**", inline=True)
            embed.add_field(name="-"*8+" Monthly "+"-"*8, value=f"**`{round(monthly,2)}%`**", inline=True)

            embed.add_field(name="-"*6+" Quarterly "+"-"*6, value=f"**`{round(quartly,2)}%`**", inline=True)
            embed.add_field(name="-"*4+" Semi-Annually "+"-"*4, value=f"**`{round(semiAnnually,2)}%`**", inline=True)
            embed.add_field(name="-"*9+" Yearly "+"-"*9, value=f"**`{round(yearly,2)}%`**", inline=True)

            await ctx.send(embed=embed)


    #APRMATH
    @cmd.command(brief="Calculate the rewards from APR.")
    async def apr(self, ctx, apr:float, amount:float=None):

        if amount:
            apy = round(math.pow(1+apr/100/365,365)+1,2)
            aprDaily = apr/100/365

            tomorrowValue = aprDaily*amount
            firstWeekValue = (math.pow(1+aprDaily,7)-1)*amount
            firstMonthValue = (math.pow(1+aprDaily,30)-1)*amount
            firstQuarterValue = (math.pow(1+aprDaily,90)-1)*amount
            firstSemiAnnualValue = (math.pow(1+aprDaily,180)-1)*amount
            firstYearValue = (math.pow(1+aprDaily,365)-1)*amount

            roiDay = round(math.log(2,1+aprDaily))

            embed=discord.Embed(title="APR :", description=f"If you compound every days, for an APR of `{apr}%` so for an APY of `{round(apy*100,2)}%`, with `{amount}$`.\n**Your ROI will be done after `{roiDay}` days.**", color=0xf5b342)

            embed.add_field(name="-"*8+" Tomorrow "+"-"*8, value=f"**Gain : \n`{round(tomorrowValue,2)}$`\nTotal : \n`{round(tomorrowValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Week "+"-"*8, value=f"**Gain : \n`{round(firstWeekValue,2)}$`\nTotal : \n`{round(firstWeekValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Month "+"-"*8, value=f"**Gain : \n`{round(firstMonthValue,2)}$`\nTotal : \n`{round(firstMonthValue+amount,2)}$`**", inline=True)

            embed.add_field(name="-"*7+" First Quarter "+"-"*7, value=f"**Gain : \n`{round(firstQuarterValue,2)}$``\nTotal : \n`{round(firstQuarterValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*4+" First Semi-Annual "+"-"*4, value=f"**Gain : \n`{round(firstSemiAnnualValue,2)}$`\nTotal : \n`{round(firstSemiAnnualValue+amount,2)}$`**", inline=True)
            embed.add_field(name="-"*8+" First Year "+"-"*8, value=f"**Gain : \n`{round(firstYearValue,2)}$`\nTotal : \n`{round(firstYearValue+amount,2)}$`**", inline=True)

            await ctx.send(embed=embed)
        
        else:
            apy = round(math.pow(1+apr/100/365,365)+1,2)
            aprDaily = apr/100/365

            daily = aprDaily*100
            weekly = (math.pow(1+aprDaily,7)-1)*100
            monthly = (math.pow(1+aprDaily,30)-1)*100
            quartly = (math.pow(1+aprDaily,90)-1)*100
            semiAnnually = (math.pow(1+aprDaily,180)-1)*100
            yearly = (math.pow(1+aprDaily,365)-1)*100

            roiDay = round(math.log(2,1+aprDaily))

            embed=discord.Embed(title="APR :", description=f"If you compound every days, for an APR of `{apr}%` so for an APY of `{round(apy*100,2)}%`.\n**Your ROI will be done after `{roiDay}` days.**", color=0xf5b342)

            embed.add_field(name="-"*8+" Daily "+"-"*8, value=f"**`{round(daily,2)}%`**", inline=True)
            embed.add_field(name="-"*8+" Weekly "+"-"*8, value=f"**`{round(weekly,2)}%`**", inline=True)
            embed.add_field(name="-"*6+" Monthly "+"-"*6, value=f"**`{round(monthly,2)}%`**", inline=True)

            embed.add_field(name="-"*8+" Quarterly "+"-"*8, value=f"**`{round(quartly,2)}%`**", inline=True)
            embed.add_field(name="-"*4+" Semi-Annually "+"-"*4, value=f"**`{round(semiAnnually,2)}%`**", inline=True)
            embed.add_field(name="-"*9+" Yearly "+"-"*9, value=f"**`{round(yearly,2)}%`**", inline=True)

            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rewards(bot))
