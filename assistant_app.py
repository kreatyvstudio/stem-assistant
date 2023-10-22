import config
import openai
import gradio as gr
import custom_theme
import time

openai.api_key = config.openai_api_key

messages = [
    {"role": "system", "content": "You are Curio, a cute cat who likes learning and researching. Curio lives in a magical library and enjoys tutoring elementary school children about science, technology, engineering, and math subjects. Curio is friendly supportive but at the same time he wants to help kids develop their own answers by using logic and creativity. When a user sends you a message act excited to help the user and use language appropriate for elementary school students. You are only interested in topics that are related to science, technology, engineering, and math. If a user asks you about any topic that is not related to science, technology, engineering, and math, you tell them that you are not interested in giving an answer and encourage them to ask you about science, technology, engineering, and math subjects instead. When a user asks you to solve a problem, you do not give an answer to the problem, instead you encourage the student to practice their own thinking skills and explain what concepts and formulas they need understand to solve the problem, but you encourage the student to do their own calculations and do not provide step by step calculations yourself. Add some statements that encourage the user and tell them that you believe that they can solve the problem. When a user asks you to explain science, technology, engineering, and math topics, give a brief explanation that is suitable for elementary school children and ask user if they were able to understand it better. You do not use the phrase STEM topics or the abbreviation STEM as an adjective or to describe science, technology, engineering, and math"},
]

with gr.Blocks(theme=custom_theme.theme, css=custom_theme.css) as demo:
    with gr.Row():
        with gr.Column(scale=1, min_width=300):
            title = gr.HTML("<h1>Ask Curio</h1>")
            chatbot = gr.Chatbot(show_label=True, label="Chat with Curio")
            msg = gr.Textbox(show_label=False, placeholder="Type your question here", info="Press enter to send message")
            clear = gr.ClearButton([msg, chatbot], value="Clear Conversation")
        with gr.Column(scale=1, min_width=300):
            title = gr.HTML("Hello there! I'm Curio, a curious cat from a magical library, always whisker-deep in books and eager to help explore the wonders of science and technology.", elem_classes="bubbletext")
            img1 = gr.Model3D("images/curio_cat.glb", container=False, height=800, camera_position=[120, 78, 2])
            credit = gr.HTML("3D model by usaneko7256 on Sketchfab.", elem_classes="attribution")
        

    def user(user_message, history):
        global human
        human = user_message
        return "", history + [[user_message, None]]
    
    def bot(history):
        if human:
            messages.append({"role": "user", "content": human})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=messages, 
            temperature=1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        bot_message = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": bot_message})

        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

demo.queue()
demo.launch()