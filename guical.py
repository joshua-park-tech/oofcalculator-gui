from appjar import gui

app = gui("calculator", "300x300")

app.setSticky("news")
app.setExpand("both")
app.setFont(20)

global operation
operation = []

def press(btn):

    operation.append(btn)
    ans = ""
    i = 0
    while i < len(operation):
        ans += operation[i]
        i += 1

    app.setLabel("t1", ans)
    app.playSound("roblox-death-sound-effect.wav")
    print(btn)

def answer(btn):
    i = 0
    ans = 0
    while i < len(operation):
        ans += int(operation[i])
        i += 1

    app.setLabel("t1", ans)

if __name__ == "__main__":
    app.addButton("=", answer, 8, 2)
    app.addButton("+", press, 8, 3)
    app.addButton("-", press, 6, 3)
    app.addButton("/", press, 4, 3)
    app.addButton("*", press, 0, 3)
    app.addButton("1", press, 6, 0)
    app.addButton("2", press, 6, 1)
    app.addButton("3", press, 6, 2)
    app.addButton("4", press, 4, 0)
    app.addButton("5", press, 4, 1)
    app.addButton("6", press, 4, 2)
    app.addButton("7", press, 0, 0)
    app.addButton("8", press, 0, 1)
    app.addButton("9", press, 0, 2)
    app.addButton("0", press, 8, 1)
    #app.addButton("del", press, 0, 3)
    app.addButton(".", press, 8, 0)
    app.addLabel("t1", "oof is great")
    app.go()