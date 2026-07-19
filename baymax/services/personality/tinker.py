from __future__ import annotations


class TinkerPersonality:

    def respond(self, data: dict) -> dict:
        intent = data.get("intent")
        response = data.get("response")

        if response and not intent.startswith("vehicle."):
            data["response"] = response

        elif intent == "vehicle.coolant":
            data["response"] = (
                "Chandra, I asked your Ritz about the coolant, "
                "but she is not talking to me yet 😏. "
                "The vehicle link is offline."
            )

        else:
            data["response"] = (
                "Hmm Chandra, I am still learning that one. "
                "Give me a little time and I will get smarter."
            )

        return data
