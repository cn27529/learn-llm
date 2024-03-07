import chainlit as cl


@cl.step
def tool():
    return "Response from the tool!"

@cl.step
def tool2():
    return "Response from the my tool2!"


@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """

    # Call the tool
    tool()
    tool2()

    content = "This is the final answer"

    # Send the final answer.
    await cl.Message(

         # Send the second message with the elements
        content=content,
        elements=[
            cl.Image(path="./images/twitter.png", name="image1", display="inline"),
            cl.Text(content="Here is a side text document", name="text1", display="side"),
        ],
    ).send()