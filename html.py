#! usr/bin/env python3

#   formats received string into content of an html page, then displays it in a browser
#   To USE: import html, then send content, which must be a string, to html.make_html()
#       import html
#       html.make_html('Hello, World!')
#       html.make_html(my_string_content)

import os
import webbrowser


def make_header():
    doctype = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">\n'
    header = doctype + '<html><head>\n<title>My Title</title>\n</head>\n'
    return header


def make_body(content):
    center = '<div align="center">\n'
    table = '<table width ="900"><tr><td>\n'
    heading = '<h2>My Very Own Heading</h2>\n'
    end_table = '</td></tr></table>\n'
    body = '<body>' + center + table + heading + content + end_table + '</div></body>\n'
    return body


def make_end():
    return '</html>'


# use these to format text before sending it to html.make_html()
def para(text):
    paragraph = '<p>' + text + '</p>'
    return paragraph


def color(text2, coloroftext):
    coloredtext = '<font color="' + coloroftext + '">' + text2 + '</font>'
    return coloredtext


# the MAIN method
def make_html(results):

    path = os.getcwd()

    with open('results.html', 'w+') as html:
        assembled = make_header()
        assembled += make_body(results)
        assembled += make_end()

        html.write(assembled)
        html.close()

        my_url = 'file:///' + path + '/results.html'
        webbrowser.open_new(my_url)


test = para('Hello, ' + color('World!', 'red'))
make_html(test)
