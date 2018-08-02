import datetime
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY,TA_LEFT,TA_RIGHT
from reportlab.lib.pagesizes import landscape,letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def printTopdf(name,course):
    fileName="../Course_completion_Certificate_"+name+".pdf"
    doc = SimpleDocTemplate(fileName,pagesize=landscape(letter))
    pdfmetrics.registerFont(TTFont('chsFont', 'ALGER.TTF'))
    pdfmetrics.registerFont(TTFont('conFont', 'BRADHITC.TTF'))
    #pdfmetrics.registerFont(TTFont('tnFont', 'times.TTF'))
    Story=[]
    logo = "logo.jpg"
    im = Image(logo, 4*inch, 2*inch)
    Story.append(im)
    line1="CERTIFICATE OF COMPLETION"
    Story.append(Spacer(1,12))

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    pltext = '<font size=34>%s</font>' % line1
    ptext = '<font name="chsFont">%s</font>' % pltext
    Story.append(Paragraph(ptext, styles["Center"]))

    Story.append(Spacer(1,72))
    firstLine="This Certificate is Presented to "+"  \""+name.upper()+"\""
    if (len(firstLine)<72):
        for i in range(72-len(firstLine)):
            firstLine+=" "
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    pltext = '<font size=16>%s</font>' % firstLine
    ptext = '<font name="conFont">%s</font>' % pltext
    Story.append(Paragraph(ptext, styles["Center"]))

    Story.append(Spacer(1,42))

    secondLine="For Sucessfully Completing the "+"     \""+course.upper()+"\""
    if (len(secondLine)<72):
        for i in range(72-len(secondLine)):

            secondLine+=" "
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    pltext = '<font size=16>%s</font>' % secondLine
    ptext = '<font name="conFont">%s</font>' % pltext
    Story.append(Paragraph(ptext, styles["Center"]))
    Story.append(Spacer(1,42))
    Story.append(Spacer(1,42))

    d=str(datetime.datetime.now())
    date="Date: "+d[:10]

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_LEFT))
    pltext = '<font size=14>%s</font>' % date
    ptext = '<font name="conFont">%s</font>' % pltext
    Story.append(Paragraph(ptext, styles["Center"]))


    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_RIGHT))
    pltext = '<font size=14>%s</font>' % "Signature"
    ptext = '<font name="conFont">%s</font>' % pltext
    Story.append(Paragraph(ptext, styles["Center"]))
    doc.build(Story)
