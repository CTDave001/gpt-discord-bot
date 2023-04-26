import asyncio
from secrets import DISCORD_SECRET, the_id_of_your_guild
import interactions
from gpt_bot import gpt_bot as ai_answer

bot = interactions.Client(token=DISCORD_SECRET)

async def async_ai_answer(text: str, context: str, model: str):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, ai_answer, text, context, model)
    return response

async def show_typing_indicator(msg: interactions.Message):
    rotating_emoji = "⚙️"
    while msg.content.startswith("Chemistry Bot is thinking"):
        typing_message = f"Chemistry Bot is thinking {rotating_emoji}"
        await msg.edit(content=typing_message)
        await asyncio.sleep(0.7)
        rotating_emoji = rotating_emoji[-1:] + rotating_emoji[:-1]
    return

@bot.command(
    name="chem",
    description="Your personalized chemistry tutor bot",
    scope=the_id_of_your_guild,
    options=[
        interactions.Option(
            name="text",
            description="Type in a chemistry related question or problem",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def my_first_command(ctx: interactions.CommandContext, text: str):
    placeholder_msg = await ctx.send("Chemistry Bot is thinking ⚙️")
    asyncio.ensure_future(show_typing_indicator(placeholder_msg))
    response = await async_ai_answer(text, 'chem', 'gpt-4')
    await placeholder_msg.edit(content=response)

bot.start()
