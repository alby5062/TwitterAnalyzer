import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def word_cloud(count_freq):
    with open("Messaggi_Twitter_Elaborati.json","w") as outfile:
        json.dump(count_freq,outfile)

    prova_file = 'Messaggi_Twitter_Elaborati.json'
    open_prova_file = open(prova_file,'r',encoding = 'utf8',errors = 'ignore')
    read_prova_file = open_prova_file.read()
    open_prova_file.close()

    My_Word_Cloud = WordCloud(width = 800,height = 800,background_color = 'white',min_font_size = 10).generate(
        read_prova_file)

    plt.figure(figsize = (8,8),facecolor = None).canvas.set_window_title('ciao')
    plt.imshow(My_Word_Cloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
