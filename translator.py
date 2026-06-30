from deep_translator import GoogleTranslator

print("Language Translator")
print("Type 'exit' to quit")

while True:
    text = input("\nEnter English Text: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    translated = GoogleTranslator(
        source='en',
        target='te'
    ).translate(text)

    print("Telugu Translation:", translated)