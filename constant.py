info = {
    "Pronoun": "he",
    "Name": "Kshitij",
    "Full_Name": "Kshitij Yadav",
    "Intro": "Data-Driven Leader and Product Analytics Expert with a strong background in Machine Learning, Data Science, and Product Management.",
    "About": "Hello, I'm Kshitij Yadav. I excel in utilizing data-driven approaches to guide product development and enhance user experience. My expertise includes product analytics, machine learning, experimental design, and leading high-impact data science teams.",
    "City": "New York, United States",
    "Email": "kshitijyad@gmail.com"
}


embed_rss= {
    'rss':"""<div style="overflow-y: scroll; height:500px; background-color:white;"> <div id="retainable-rss-embed" 
        data-rss=""
        data-maxcols="3" 
        data-layout="grid"
        data-poststyle="inline" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="0"></div></div> <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js"></script>"""
}

import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
endorsements = {
    "img1": image_to_base64("images/recommendation1.png"),
    "img2": image_to_base64("images/recommendation2.png"),
    "img3": image_to_base64("images/recommendation3.png"),
    "img4": image_to_base64("images/recommendation4.png")
}
