import gradio as gr

def greet(name):
    return f"Hello {name}, Meridian Credit is running!"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text"
)

demo.launch()