from __future__ import annotations

from typing import Any


class UserMessage:
    def __init__(self, text: str):
        self.text = text


class TextDelta:
    def __init__(self, content: str):
        self.content = content


class StreamDone:
    pass


class LlmChat:
    def __init__(self, api_key: str | None = None, session_id: str | None = None, system_message: str | None = None):
        self.api_key = api_key
        self.session_id = session_id
        self.system_message = system_message
        self.provider = None
        self.model_id = None
        self.params: dict[str, Any] | None = None

    def with_model(self, provider: str, model_id: str):
        self.provider = provider
        self.model_id = model_id
        return self

    def with_params(self, **params):
        self.params = params
        return self

    async def stream_message(self, message: UserMessage):
        yield TextDelta("AI responses are unavailable in this local environment.")
        yield StreamDone()

    async def send_message_multimodal_response(self, message: UserMessage):
        return "", []
