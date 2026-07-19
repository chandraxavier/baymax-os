import asyncio
from pathlib import Path
from baymax.core.runtime.engine import RuntimeEngine

async def main():
    engine = RuntimeEngine(config_root=Path("config"))
    await engine.boot_async()

    voice = engine.context.service_manager.registry.get("voice")
    tts = engine.context.service_manager.registry.get("tts")

    print("\n🧚 Tinker console online. Type 'exit' to quit.\n")

    try:
        while True:
            text = input("You> ")
            if text.lower() in ("exit", "quit"):
                break

            result = await voice.process(text)
            print("Baymax>", result.get("response"))
            await tts.speak(result.get("response"))

    finally:
        await engine.shutdown_async()

asyncio.run(main())
