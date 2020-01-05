def makebold(fn,something):
    def wrapped():
        return f"<{something}>" + fn() + f"<{something}>"
    return wrapped


@makebold("Alex")
def get_text(text='I code with PyBites'):
    return text

print(get_text())
