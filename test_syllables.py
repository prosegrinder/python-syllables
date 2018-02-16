# Adapted from: http://www.onebloke.com/2011/06/counting-syllables-accurately-in-python-on-google-app-engine/
import re

import cmudict

# Rapid test of syllable estimations
# Will eventually become a unit test.

def main():
    hits = []
    misses = []

    for line in cmudict.stream():
        line = line.decode('utf-8').strip()
        word, phones = line.split(" ", 1)
        # Strip out the alternate designation and test anyhow
        word = re.sub(r"\(\d+\)+", '', word)
        stresses = re.sub(r"[^012]", "", phones)
        cmudict_syllables = len(stresses)
        estimated_syllables = estimate_syllables(word)
        if cmudict_syllables == estimated_syllables:
            hits.append(word)
        else:
            misses.append(word)
            # print(word)

    hit = len(hits)
    miss = len(misses)
    total = hit + miss
    print("Hits: {0}, Miss: {1}, Accuracy: {2}".format(hit, miss, hit / total))

# Estimation stuff here

subSyllables = [
    'cial',
    'tia',
    'cius',
    'cious',
    'uiet',
    'gious',
    'geous',
    'priest',
    'giu',
    'dge',
    'ion',
    'iou',
    'sia$',
    '.che$',
    '.ched$',
    '.abe$',
    '.ace$',
    '.ade$',
    '.age$',
    '.aged$',
    '.ake$',
    '.ale$',
    '.aled$',
    '.ales$',
    '.ane$',
    '.ame$',
    '.ape$',
    '.are$',
    '.ase$',
    '.ashed$',
    '.asque$',
    '.ate$',
    '.ave$',
    '.azed$',
    '.awe$',
    '.aze$',
    '.aped$',
    '.athe$',
    '.athes$',
    '.ece$',
    '.ese$',
    '.esque$',
    '.esques$',
    '.eze$',
    '.gue$',
    '.ibe$',
    '.ice$',
    '.ide$',
    '.ife$',
    '.ike$',
    '.ile$',
    '.ime$',
    '.ine$',
    '.ipe$',
    '.iped$',
    '.ire$',
    '.ise$',
    '.ished$',
    '.ite$',
    '.ive$',
    '.ize$',
    '.obe$',
    '.ode$',
    '.oke$',
    '.ole$',
    '.ome$',
    '.one$',
    '.ope$',
    '.oque$',
    '.ore$',
    '.ose$',
    '.osque$',
    '.osques$',
    '.ote$',
    '.ove$',
    '.pped$',
    '.sse$',
    '.ssed$',
    '.ste$',
    '.ube$',
    '.uce$',
    '.ude$',
    '.uge$',
    '.uke$',
    '.ule$',
    '.ules$',
    '.uled$',
    '.ume$',
    '.une$',
    '.upe$',
    '.ure$',
    '.use$',
    '.ushed$',
    '.ute$',
    '.ved$',
    '.we$',
    '.wes$',
    '.wed$',
    '.yse$',
    '.yze$',
    '.rse$',
    '.red$',
    '.rce$',
    '.rde$',
    '.ily$',
    '.ely$',
    '.des$',
    '.gged$',
    '.kes$',
    '.ced$',
    '.ked$',
    '.med$',
    '.mes$',
    '.ned$',
    '.[sz]ed$',
    '.nce$',
    '.rles$',
    '.nes$',
    '.pes$',
    '.tes$',
    '.res$',
    '.ves$',
    'ere$'
]

addSyllables = [
    'ia',
    'riet',
    'dien',
    'ien',
    'iet',
    'iu',
    'iest',
    'io',
    'ii',
    'ily',
    '.oala$',
    '.iara$',
    '.ying$',
    '.earest',
    '.arer',
    '.aress',
    '.eate$',
    '.eation$',
    '[aeiouym]bl$',
    '[aeiou]{3}',
    '^mc', 'ism',
    '^mc', 'asm',
    '([^aeiouy])1l$',
    '[^l]lien',
    '^coa[dglx].',
    '[^gq]ua[^auieo]',
    'dnt$'
]

re_subsyllables = []
for s in subSyllables:
    re_subsyllables.append(re.compile(s))

re_addsyllables = []
for s in addSyllables:
    re_addsyllables.append(re.compile(s))


def estimate_syllables(word):
    parts = re.split(r'[^aeiouy]+', word)
    valid_parts = []

    for part in parts:
        if part != '':
            valid_parts.append(part)

    syllables = 0

    for p in re_subsyllables:
        if p.match(word):
            syllables -= 1

    for p in re_addsyllables:
        if p.match(word):
            syllables += 1

    syllables += len(valid_parts)

    if syllables <= 0:
        syllables = 1

    return syllables

if __name__ == "__main__":
    main()
