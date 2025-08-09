class Conversation:
    def __init__(self, system_prompt: str):
        self.system = {"role": "system", "content": system_prompt}
        self.messages = [self.system]

    def add_user(self, text: str):
        self.messages.append({"role": "user", "content": text})

    def add_assistant(self, text: str):
        self.messages.append({"role": "assistant", "content": text})

    def reset(self):
        self.messages = [self.system]

    def get(self):
        return self.messages
