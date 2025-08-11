from config import MODEL_REGISTRY, SYSTEM_PROMPT, GEN_KWARGS, DTYPE
from conversation import Conversation
from backends import LocalBackend, OpenAIBackend

def main():
    print("* Models:", ", ".join(MODEL_REGISTRY))
    key = input("\nEnter model key (or HF repo id): ").strip()
    model_id = MODEL_REGISTRY.get(key, key)

    if model_id == "gpt-5":
        if OpenAIBackend is None:
            print("OpenAI SDK not installed. Run: pip install openai")
            return
        api_key = input("Enter OpenAI API key: ").strip()
        backend = OpenAIBackend("gpt-5", max_tokens=GEN_KWARGS["max_new_tokens"], api_key=api_key)
        print("Loaded gpt-5.")
    else:
        backend = LocalBackend(model_id, GEN_KWARGS, dtype=DTYPE)
        print("Loaded local model.")

    convo = Conversation(SYSTEM_PROMPT)
    print('\nType your message. Use "/reset" or "/quit".')

    while True:
        msg = input("\n> ").strip()
        if not msg: continue
        if msg.lower() == "/quit": print("Bye."); break
        if msg.lower() == "/reset": convo.reset(); print("Reset."); continue

        convo.add_user(msg)
        print("\nGenerating...")
        ans = backend.generate(convo.get())
        convo.add_assistant(ans)
        print("\nAssistant:\n" + ans)

if __name__ == "__main__":
    main()
