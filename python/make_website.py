haiku1 = {
    "title" : "January",
    "poem" : """Delightful display
Snowdrops bow their pure white heads
To the sun's glory."""
}

haiku2 = {
    "title" : "October",
    "poem" : """ Like crunchy cornflakes
            Gold leaves rustle underfoot
            Beauty in decay."""
}

haiku3 = {
    "title": "Peaches",
    "poem" : """ The chill, worming in
        Shock, pleasure, bursting within
        Summer tongue awakes"""
}

haiku4 = {
    "title": "Python",
    "poem" : """Programming language
        So fun so productive, I
        want to code all day"""
}

haikus = [haiku1, haiku2, haiku3, haiku4]

def make_head(title):
    return """<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="styles.css"/>
        <title>%s</title>
    </head>
    <body>
            <div id="menu">
                <div class="menu-item page-name">Haiku Site</div>
                <div class="menu-item"><a href="main.html">Home</a></div>
            </div>
    """ % title

def make_haiku_page(haiku):
    head = make_head(haiku["title"])
    html = """<!DOCTYPE html>
    <html lang="en">
    %s
        <h1>%s</h1>
        <p>%s</p>
    </body>
    </html>""" % (head,haiku["title"],haiku["poem"])

    f = open(haiku["title"] + ".html", "w")
    f.write(html)
    f.close()

def poem_links(haikus):
    list_code = ""
    for haiku in haikus:
        list_code += """<li><a href="%s.html">%s</a></li>""" % (haiku["title"],haiku["title"])
    return list_code
    
def make_main_page():
    head = make_head("List of Haiku Poems")
    html = """<!DOCTYPE html>
    <html lang="en">
    %s
        <h1>List of Haiku Poems</h1>
        <ul>
            %s
        </ul>
    </body>
    </html>""" % (head, poem_links(haikus))

    f = open("main.html", "w")
    f.write(html)
    f.close()

make_main_page()
for haiku in haikus:
    make_haiku_page(haiku)