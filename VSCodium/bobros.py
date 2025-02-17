import graphics as gr


def start():
    win = gr.GraphWin('gimme ram mmmfghhh v2.4ghz 5g editoin', 700, 500)
    win.setBackground('teal')

    tittle = gr.Text(gr.Point(290, 30), "FR33 R4M G3NER3T0r v100gbs")
    tittle.setSize(28)
    tittle.draw(win)

    lineBg = gr.Line(gr.Point(198, 100), gr.Point(502, 100))
    lineBg.setFill('white')
    lineBg.setWidth(22)
    lineBg.draw(win)



    buton = gr.Image(gr.Point(350, 220), 'get.png')
    buton.draw(win)

    win.getMouse()
    buton.undraw()

    lineIn = gr.Line(gr.Point(200, 100), gr.Point(240, 100)) #max at 500
    lineIn.setFill('green')
    lineIn.setWidth(18)
    lineIn.draw(win)

    bil = gr.Image(gr.Point(100, 220), "GAte.png")
    bil.draw(win)

    quote1 = gr.Image(gr.Point(350, 220), "billium.png")
    quote1.draw(win)

    for i in range(2):
        # <drawing commands for ith frame>
        gr.update(1)

    lineIn.undraw()
    lineIn = gr.Line(gr.Point(200, 100), gr.Point(300, 100)) #max at 500
    lineIn.setFill('green')
    lineIn.setWidth(18)
    lineIn.draw(win)

    win2 = gr.GraphWin('LOONA WORTHYNESS TESST', 500, 400)
    win2.setBackground('pink')

    loona = gr.Image(gr.Point(160, 250), "loona.png")
    loona.draw(win2)

    loonaPic = gr.Image(gr.Point(220, 70), 'loonaText.png')
    loonaPic.draw(win2)

    loonatic = gr.Text(gr.Point(320, 140), '<i>Talk to our experts')
    loonatic.setSize(20)
    loonatic.setFill('red')
    loonatic.draw(win2)

    loonatic2 = gr.Text(gr.Point(320, 165), 'at r/Losercity!<i')
    loonatic2.setSize(20)
    loonatic2.setFill('red')
    loonatic2.draw(win2)


    for i in range(5):
        # <drawing commands for ith frame>
        gr.update(1)

    lineIn.undraw()
    lineIn = gr.Line(gr.Point(200, 100), gr.Point(412, 100)) #max at 500
    lineIn.setFill('green')
    lineIn.setWidth(18)
    lineIn.draw(win)
    
    win3 = gr.GraphWin('BUY NOW ON Ji-BUY!', 500, 500)
    win3.setBackground('white')

    whatsapp = gr.Image(gr.Point(250, 200), "whatsappperf.png")
    whatsapp.draw(win3)

    whatext = gr.Text(gr.Point(110, 450), 'wasapp perfum')
    whatext.setSize(22)
    whatext.draw(win3)

    costsw = gr.Text(gr.Point(280, 450), '10.97$')
    costsw.setSize(24)
    costsw.draw(win3)

    for i in range(3):
        # <drawing commands for ith frame>
        gr.update(2)

        ad = gr.GraphWin('cat :33', 800, 500)
        ad.setBackground('teal')

        cat = gr.Image(gr.Point(400, 250), "finn.png")
        cat.draw(ad)

    lineIn.undraw()
    lineIn = gr.Line(gr.Point(200, 100), gr.Point(460, 100)) #max at 500
    lineIn.setFill('green')
    lineIn.setWidth(18)
    lineIn.draw(win)

    win4 = gr.GraphWin('find more GORDON x LOONA fan strips NOW', 400, 600)

    gordon = gr.Image(gr.Point(200, 260), 'corny.png')
    gordon.draw(win4)

    goron = gr.Text(gr.Point(243, 540), 'find this AND more at gordonxloo.na !')
    goron.setSize(20)
    goron.draw(win4)


    for i in range(4):
        # <drawing commands for ith frame>
        gr.update(1)

    lineIn.undraw()
    lineIn = gr.Line(gr.Point(200, 100), gr.Point(480, 100)) #max at 500
    lineIn.setFill('green')
    lineIn.setWidth(18)
    lineIn.draw(win)


    win5 = gr.GraphWin('i am he who is clamming', 500, 600)
    win5.setBackground('white')

    chad = gr.Image(gr.Point(250, 260), "chad.png")
    chad.draw(win5)

    chudjak = gr.Text(gr.Point(240, 540), 'LEARN HOW TO BE A CHAD LIKE HIM')
    chudjak.setSize(20)
    chudjak.draw(win5)

    chudjak2 = gr.Text(gr.Point(240, 565), 'AND NOT A CHUD LIKE "THEM"')
    chudjak2.setSize(20)
    chudjak2.draw(win5)



    for i in range(4):
        # <drawing commands for ith frame>
        gr.update(1)

    win6 = gr.GraphWin('FINISH COMPROMISE', 800, 500)
    win6.setBackground('teal')

    finish = gr.Image(gr.Point(400, 250), "finn.png")
    finish.draw(win6)

    finnish = gr.Text(gr.Point(300, 200), 'FINISH!!!')
    finnish.setSize(30)
    finnish.setFill('white')
    finnish.draw(win6)

    for i in range(6):
        # <drawing commands for ith frame>
        gr.update(1)

    win.close

start()
