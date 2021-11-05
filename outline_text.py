from typing import Optional


def outline(phrase, width: Optional[int] = None, height: Optional[int] = 3, filler: Optional[str] = " ", frame: Optional[str] = "#", header = False, footer = False, print_output: Optional[bool] = False):

    def _empty_line(filler, icon, width):
        line_fill=""
        for i in range(1,width-2):
            line_fill += filler
        return f"{icon}{line_fill}{icon}"

    # Check inputs and supply defaults
    if width:
        if width < len(phrase):
            raise ValueError("width cannot be less than the length of phrase")
    else:
        width = len(phrase) + 5

    outline = []
    min_length = len(phrase)
    total_width = int(min_length + width)

    # header
    outline.append(_empty_line(frame if header else filler, frame, total_width))

    # empty lines between header and phrase
    for _ in range(1,int(height-3/2)):
        outline.append(_empty_line(" ", frame, total_width))

    # Center phrase
    phrase_filler = ""
    phrase_fillter_length = int((total_width-min_length)/2)
    for _ in range(1, phrase_fillter_length):
        phrase_filler += filler
    if width % 2 == 0:
        outline.append(f"{frame}{phrase_filler}{phrase}{phrase_filler[:-1]}{frame}")
    else:
        outline.append(f"{frame}{phrase_filler}{phrase}{phrase_filler}{frame}")

    # empty lines between phrase and footer
    for _ in range(1,int(height-3/2)):
        outline.append(_empty_line(" ", frame, total_width))

    # footer
    outline.append(_empty_line(frame if footer else filler, frame, total_width))

    if print_output:
        for i in outline:
            print(i)
    else:
        return outline


def outline_numpy(phrase, width = 40, height = 5, filler = " ", frame = "#", header = False, footer = False):
    from numpy import chararray
    Matrix = chararray((5,5))
    for d,y in enumerate(Matrix):
        for dd,x in enumerate(Matrix):
            if d == 0:
                if header:
                    Matrix[d][dd] = frame
            if dd == 0 or dd == int(5-1):
                Matrix[d][dd] = frame
            if d == int(5-1):
                if footer:
                    Matrix[d][dd] = frame



