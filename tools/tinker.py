#!/usr/bin/env python3
import asyncio
from baymax.services.voice.manager import VoiceManager

async def main():
    manager = VoiceManager()
    await manager.start()
    print("\n🧚 Tinker is online. Type 'exit' to quit.\n")
    while True:
        try:
            text = input("You> ").strip()
            if text.lower() in ("exit", "quit"):
                break
            result = await manager.process(text)
            print(f"Tinker> {result['response']}\n")
        except (KeyboardInterrupt, EOFError):
            break
    await manager.stop()
    print("\n👋 Tinker signing off.")

if __name__ == "__main__":
    asyncio.run(main())
