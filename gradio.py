import gradio as gr
from utils import get_predit # predt function

# Define example URLs
example_url_1 = 'https://medium.com'
example_url_2 = 'http://google.com-redirect@valimail.com'
example_url_3 = 'https://a101-nisan-kampanyalari.com'

# Create the Gradio interface
demo = gr.Interface(
    fn=get_predit,
    inputs=gr.components.Textbox(label='Input', placeholder='Enter URL here...'),
    outputs=gr.components.Label(label='Predictions', num_top_classes=5),
    title='kmack/malicious-url-detection',
    description='Detects whether a given URL is benign or potentially malicious.',
    examples=[[example_url_1], [example_url_2], [example_url_3]],
    allow_flagging='never'
)

