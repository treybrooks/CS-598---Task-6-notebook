import itertools
import numpy as np
import matplotlib.pyplot as plt
import re


weird_stuff = {
    '&#160;': {'readable': '\xa0', 'replace': ' '},
    '&#161;': {'readable': '¡', 'replace': '!'},
    '&#162;': {'readable': '¢', 'replace': '$'},
    '&#163;': {'readable': '£', 'replace': '$'},
    '&#173;': {'readable': '\xad', 'replace': ' '},
    '&#174;': {'readable': '®', 'replace': ''},
    '&#176;': {'readable': '°', 'replace': ''},
    '&#186;': {'readable': 'º', 'replace': ''},
    '&#191;': {'readable': '¿', 'replace': '?'},
    '&#192;': {'readable': 'À', 'replace': 'A'},
    '&#200;': {'readable': 'È', 'replace': 'E'},
    '&#201;': {'readable': 'É', 'replace': 'E'},
    '&#209;': {'readable': 'Ñ', 'replace': 'N'},
    '&#219;': {'readable': 'Û', 'replace': 'U'},
    '&#220;': {'readable': 'Ü', 'replace': 'U'},
    '&#223;': {'readable': 'ß', 'replace': 'B'},
    '&#224;': {'readable': 'à', 'replace': 'a'},
    '&#225;': {'readable': 'á', 'replace': 'a'},
    '&#226;': {'readable': 'â', 'replace': 'a'},
    '&#227;': {'readable': 'ã', 'replace': 'a'},
    '&#228;': {'readable': 'ä', 'replace': 'a'},
    '&#229;': {'readable': 'å', 'replace': 'a'},
    '&#230;': {'readable': 'æ', 'replace': 'ae'},
    '&#231;': {'readable': 'ç', 'replace': 'c'},
    '&#232;': {'readable': 'è', 'replace': 'e'},
    '&#233;': {'readable': 'é', 'replace': 'e'},
    '&#234;': {'readable': 'ê', 'replace': 'e'},
    '&#235;': {'readable': 'ë', 'replace': 'e'},
    '&#236;': {'readable': 'ì', 'replace': 'i'},
    '&#237;': {'readable': 'í', 'replace': 'i'},
    '&#238;': {'readable': 'î', 'replace': 'i'},
    '&#239;': {'readable': 'ï', 'replace': 'i'},
    '&#241;': {'readable': 'ñ', 'replace': 'n'},
    '&#242;': {'readable': 'ò', 'replace': 'o'},
    '&#243;': {'readable': 'ó', 'replace': 'o'},
    '&#244;': {'readable': 'ô', 'replace': 'o'},
    '&#246;': {'readable': 'ö', 'replace': 'o'},
    '&#249;': {'readable': 'ù', 'replace': 'u'},
    '&#250;': {'readable': 'ú', 'replace': 'u'},
    '&#251;': {'readable': 'û', 'replace': 'u'},
    '&#252;': {'readable': 'ü', 'replace': 'u'},
    '&#333;': {'readable': 'ō', 'replace': 'o'},
    '&#338;': {'readable': 'Œ', 'replace': ''},
    '&#339;': {'readable': 'œ', 'replace': 'oe'},
    '&#8230;': {'readable': '…', 'replace': '...'},
    '&#8482;': {'readable': '™', 'replace': ''}
}


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def convert_html_entities(s):
    matches = re.findall("&#\d+;", s)
    if len(matches) > 0:
        hits = set(matches)
        for hit in hits:
            name = hit[2:-1]
            try:
                entnum = int(name)
                s = s.replace(hit, chr(entnum))
            except ValueError:
                pass

    matches = re.findall("&#[xX][0-9a-fA-F]+;", s)
    if len(matches) > 0:
        hits = set(matches)
        for hit in hits:
            hex = hit[3:-1]
            try:
                entnum = int(hex, 16)
                s = s.replace(hit, chr(entnum))
            except ValueError:
                pass

    matches = re.findall("&\w+;", s)
    hits = set(matches)
    amp = "&amp;"
    if amp in hits:
        hits.remove(amp)
    for hit in hits:
        name = hit[1:-1]
        if htmlentitydefs.name2codepoint.has_key(name):
            s = s.replace(hit, chr(htmlentitydefs.name2codepoint[name]))
    s = s.replace(amp, "&")
    return s
