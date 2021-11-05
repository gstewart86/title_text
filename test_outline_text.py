from outline_text import outline, outline_numpy

def test_outline_text():
    assert outline("YES") == ['#        #', '#   YES  #', '#        #']
    outline("YES", width=3) == ['#   #', '#YES#', '#   #']
    outline("YES", width=41) == ['#                                         #', '#                   YES                   #', '#                                         #']
    outline("YES", header=True, footer=True) == ['##########', '#   YES  #', '##########']

def test_outline_numpy():
    outline_numpy("YES")
