from taipy import Gui

def create_gui():
    my_page = """
    # Your ML Application

    <|{input_data}|input|>

    <|{output}|label|>
    """
    return Gui(page=my_page)
