
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
import speech_recognition as sr
import pyttsx3

# === Voice Engine Setup ===
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "API unavailable."

# === Reminder Tool ===
def set_reminder(task: str):
    with open("data/reminders.txt", "a") as f:
        f.write(f"{task}\n")
    return f"Reminder set for: {task}"

reminder_tool = Tool(
    name="SetReminder",
    func=set_reminder,
    description="Use this to set medication or appointment reminders for the elderly user."
)

# === Emergency Tool ===
def trigger_alert(symptom: str):
    return f"Emergency alert triggered for: {symptom}. Notifying caregiver..."

emergency_tool = Tool(
    name="EmergencyAlert",
    func=trigger_alert,
    description="Triggers emergency alert if abnormal conditions detected (e.g., fall, chest pain)."
)

# === Companion Tool ===
def companion_chat(message: str):
    return f"That's interesting! Let's talk more about it."

companion_tool = Tool(
    name="CompanionChat",
    func=companion_chat,
    description="Provides empathetic and friendly conversation with elderly users."
)

# === Agent Factory ===
def create_agent(tools: list):
    llm = ChatOpenAI(temperature=0.7)
    memory = ConversationBufferMemory(memory_key="chat_history")
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="chat-conversational-react-description",
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )

# === Create Agents ===
reminder_agent = create_agent([reminder_tool])
emergency_agent = create_agent([emergency_tool])
companion_agent = create_agent([companion_tool])

# === FastAPI App ===
app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/reminder/")
def reminder(query: Query):
    response = reminder_agent.run(query.user_input)
    speak(response)
    return {"response": response}

@app.post("/emergency/")
def emergency(query: Query):
    response = emergency_agent.run(query.user_input)
    speak(response)
    return {"response": response}

@app.post("/companion/")
def companion(query: Query):
    response = companion_agent.run(query.user_input)
    speak(response)
    return {"response": response}

# Optional CLI trigger for voice interaction
def voice_interaction():
    user_input = listen()
    response = companion_agent.run(user_input)
    speak(response)

# Uncomment to test in terminal
# voice_interaction()
