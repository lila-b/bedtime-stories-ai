"""
UI for the Winnie the Pooh Story Generator
Using Gradio and custom theme
Placeholder function will be updated with actual story generation code once completed.
"""
import gradio as gr
from theme_violet_amber import theme as violet_amber

# Placeholder function - TO BE UPDATED
def story_placeholder(character, story_prompt):
    # INSERT CODE HERE
    full = "I will write you a story centered around " + character + ". The story will be about: " + story_prompt
    return full

# Gradio UI
with gr.Blocks(theme=violet_amber) as demo:
    gr.Markdown(
    """
    # Winnie the Pooh Story Generator
    *Simply enter a character name and setting, then I will write a story from the Hundred Acre Woods for you!*
    """)
    textbox = gr.Textbox(label="Character Name")
    textbox2 = gr.Textbox(label="Story Setting")
    
    with gr.Row():
        button = gr.Button("Submit", variant="primary")
        clear = gr.Button('Clear')
    
    output = gr.Textbox(label="A story for you... ")
    
    button.click(story_placeholder, [textbox, textbox2], output)

demo.launch()
