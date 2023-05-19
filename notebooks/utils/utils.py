import base64, io, IPython
from PIL import Image as PILImage
def image_export_to_html(filepath: str, width: int, height: int):
    """
    Quick hack to enable image export to html
    """
    
    image = PILImage.open(filepath)
    output = io.BytesIO()
    image.save(output, format='PNG')
    encoded_string = base64.b64encode(output.getvalue()).decode()

    html = '<img src="data:image/png;base64,{}" width={} height={}/>'.format(encoded_string, width, height)

    return html