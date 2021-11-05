# title_text
Center and outline some text with a given character
```
❯ ./outline.py "test message"
#                          #
#       test message       #
#                          #
❯ ./outline.py "test message" --height 5
#                          #
#                          #
#                          #
#       test message       #
#                          #
#                          #
#                          #
❯ ./outline.py "test message" --width 40
#                                                 #
#                   test message                  #
#                                                 #
#-------test message-------#
############################
```
