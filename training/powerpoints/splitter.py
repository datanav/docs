from pptx import Presentation
from pptx.shapes.autoshape import Shape
import copy

prs = Presentation('splitme.pptx')
print(prs)
text_runs = []

text_box = None
for slide in prs.slides:
    for shape in slide.shapes:
        print('#')
        print(type(shape))
        print(shape)
        if not shape.has_text_frame:
            continue
        if type(shape) == Shape:
            text_box = shape
        for paragraph in shape.text_frame.paragraphs:
            print('##')
            print(paragraph)
            for run in paragraph.runs:
                print('###')
                print(run)
                print(run.text)


def replace_paragraph_text_retaining_initial_formatting(paragraph, new_text):
    p = paragraph._p  # the lxml element containing the `<a:p>` paragraph element
    # remove all but the first run
    print(f'For paragraph {paragraph} with runs "{paragraph.runs}" adding text {new_text}')
    for idx, run in enumerate(paragraph.runs):
        if idx == 0:
            continue
        p.remove(run._r)
    paragraph.runs[0].text = new_text

s = prs.slides[0]


replace_paragraph_text_retaining_initial_formatting(s.shapes.title.text_frame.paragraphs[0], 'Hello world')

print('##########')
print(text_box)
writethis = """One
Two
Three
Four
Five
"""


def copy_run(run_from, run_to):
    r_to = run_to._r
    r_to.addnext(copy.deepcopy(run_from._r))
    r_to.getparent().remove(r_to)

def copy_paragraph(paragraph_from, paragraph_to):
    p_to = paragraph_to._p
    p_to.addnext(copy.deepcopy(paragraph_from._p))
    p_to.getparent().remove(p_to)

def replaceBulletPoints(textframe, text):
    first_paragraph = textframe.paragraphs[0]
    #first_run = textframe.paragraphs[0].runs[0]
    for i, line in enumerate(text.split('\n')):
        if len(textframe.paragraphs) < i + 1:
            p = textframe.add_paragraph()
            copy_paragraph(paragraph_from=first_paragraph, paragraph_to=p)
            #r = p.add_run()
            #copy_run(run_from=first_run, run_to=r)
        print(len(textframe.paragraphs))
        print(i + 1)
        replace_paragraph_text_retaining_initial_formatting(textframe.paragraphs[i], line)


#replace_paragraph_text_retaining_initial_formatting(text_box.text_frame.paragraphs[0], 'YO WAZZUP')


replaceBulletPoints(text_box.text_frame, writethis)
#print(text_box.text_frame.paragraphs)
#for x in text_box.text_frame.paragraphs:
#    print(x)

#for shape in s.placeholders:
#    print('%d %s' % (shape.placeholder_format.idx, shape.name))

textbox = None
for shape in slide.shapes:
    if shape.is_placeholder:
        phf = shape.placeholder_format
        print('%d, %s' % (phf.idx, phf.type))
#    print('%s' % shape.shape_type)

prs.save('tmp_output.pptx')