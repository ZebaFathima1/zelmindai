from __future__ import annotations


class OpenAISpeechToText:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    async def transcribe(self, **kwargs):
        return {"text": ""}


class OpenAITextToSpeech:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    async def generate_speech(self, **kwargs):
        return b""
