import discord
import asyncio
from discord.ext import commands
import requests

amego = commands.Bot(command_prefix="$")



@amego.command()
async def covid(ctx, *, countryName = None):
        try:
            if countryName is None:
                embed=discord.Embed(title="This command is used like this: ```covid [country]```", colour=0xff0000, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)


            else:
                url = f"https://coronavirus-19-api.herokuapp.com/countries/{countryName}"
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                active = json_stats["active"]
                critical = json_stats["critical"]
                casesPerOneMillion = json_stats["casesPerOneMillion"]
                deathsPerOneMillion = json_stats["deathsPerOneMillion"]
                totalTests = json_stats["totalTests"]
                testsPerOneMillion = json_stats["testsPerOneMillion"]

                amego = discord.Embed(title=f"**COVID-19 Status Of {country}**!", description="This Information Isn't Live Always, Hence It May Not Be Accurate!", colour=0x0000ff, timestamp=ctx.message.created_at)
                amego.add_field(name="**Total Cases**", value=totalCases, inline=True)
                amego.add_field(name="**Today Cases**", value=todayCases, inline=True)
                amego.add_field(name="**Total Deaths**", value=totalDeaths, inline=True)
                amego.add_field(name="**Today Deaths**", value=todayDeaths, inline=True)
                amego.add_field(name="**Recovered**", value=recovered, inline=True)
                amego.add_field(name="**Active**", value=active, inline=True)
                amego.add_field(name="**Critical**", value=critical, inline=True)
                amego.add_field(name="**Cases Per One Million**", value=casesPerOneMillion, inline=True)
                amego.add_field(name="**Deaths Per One Million**", value=deathsPerOneMillion, inline=True)
                amego.add_field(name="**Total Tests**", value=totalTests, inline=True)
                amego.add_field(name="**Tests Per One Million**", value=testsPerOneMillion, inline=True)

                amego.set_thumbnail(url="https://cdn.discordapp.com/emojis/850736267905728582.png?v=1")
                await ctx.send(embed=amego)

        except:
            embed3 = discord.Embed(title="Invalid Country Name Or API Error! Try Again..!", colour=0xff0000, timestamp=ctx.message.created_at)
            embed3.set_author(name="Error!")
            await ctx.send(embed=embed3)

amego.run("توكن")
