from jarvis.core.session import Session

llminput = input("Enter preferred LLM (gemini): ")

if llminput == "gemini":
    from jarvis.llm.gemini import GeminiProvider
    llm = GeminiProvider()
else:
    print("Invalid LLM provider. Exiting.")
    exit()

userinput = input()
session = Session(llm)

while(userinput!="exit"):
    response = session.send(userinput)
    print(response)
    userinput = input()