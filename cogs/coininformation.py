import discord
from discord.ext import commands as cmd
from pycoingecko import CoinGeckoAPI

gecko = CoinGeckoAPI()


class CoinInformation(cmd.Cog, name="Token Information "):

    def __init__(self, bot):
        self.client=bot
        
    #COINGECKO
    @cmd.command(brief="Give information about a coin from CoinGecko.")
    async def coin(self, ctx, apiid:str):
        coinInfo=gecko.get_coin_by_id(id=apiid)

        urlHomepage=coinInfo['links']['homepage'][0]
        urlCommunity=coinInfo['links']['chat_url'][0]

        embed=discord.Embed(title=apiid.upper(), url=urlHomepage)
        embed.set_thumbnail(url=coinInfo['image']['thumb'])

        embed.add_field(name="Rank :", value=f"`{coinInfo['market_cap_rank']}`", inline=True)
        embed.add_field(name=u"\u200B", value=u"\u200B", inline=True)
        embed.add_field(name="Price :", value=f"`{coinInfo['market_data']['current_price']['usd']}$` - `{coinInfo['market_data']['current_price']['eur']}€`", inline=True)


        embed.add_field(name="24h :", value=f"`{round(coinInfo['market_data']['price_change_percentage_24h'],2)}%`", inline=True)
        embed.add_field(name=u"\u200B", value=u"\u200B", inline=True)
        embed.add_field(name="7D :", value=f"`{round(coinInfo['market_data']['price_change_percentage_7d'],2)}%`", inline=True)

        embed.add_field(name="Market Capital :", value=f"`{coinInfo['market_data']['market_cap']['usd']}$`", inline=True)
        embed.add_field(name=u"\u200B", value=u"\u200B", inline=True)
        embed.add_field(name="Volume :", value=f"`{coinInfo['market_data']['total_volume']['usd']}$`", inline=True)

        if coinInfo['links']['homepage'][0]:
            embed.add_field(name="Website :", value=urlHomepage, inline=False)
        if coinInfo['links']['chat_url'][0]:
            embed.add_field(name="Community :", value=urlCommunity, inline=False)

        #embed.set_footer(text=f"{coinInfo['asset_platform_id']} - {coinInfo['contract_address']}")

        await ctx.send(embed=embed)

    #PRICE
    @cmd.command(brief="Give the price of a coin from CoinGecko.")
    async def price(self, ctx, apiid:str):
        priceData=gecko.get_price(ids=apiid, vs_currencies="usd,eur")
        coinInfo=gecko.get_coin_by_id(id=apiid)
        embed=discord.Embed(title=f"Price of {apiid.upper()} :", url=coinInfo['links']['homepage'][0], description=f"**{priceData[apiid]['usd']}$ - {priceData[apiid]['eur']}€**")
        embed.set_thumbnail(url=coinInfo['image']['large'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CoinInformation(bot))
