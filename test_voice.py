import asyncio
from baymax.runtime import BaymaxRuntime

async def main():
    runtime = BaymaxRuntime()
    await runtime.start()

    voice = runtime.context.service_manager.registry.get("voice")

    while True:
        text = input("You> ")
        if text.lower() in ("quit", "exit"):
            break
        result = await voice._manager.process(text)
        print("Baymax>", result)

    await runtime.stop()

asyncio.run(main())
