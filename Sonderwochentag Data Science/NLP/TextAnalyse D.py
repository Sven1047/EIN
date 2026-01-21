# TEXTBLOB Bibliothek https://textblob-de.readthedocs.io/en/latest/readme.html

# CC Coordinating conjunction and, or, but
# CD Cardinal number 1, 2, 3
# DT Determiner the, a, an
# EX Existential there there
# FW Foreign word bonjour, hola
# IN Preposition/subordinating conjunction in, on, after
# JJ Adjective beautiful, happy
# JJR Adjective, comparative bigger, stronger
# JJS Adjective, superlative biggest, strongest
# LS List item marker 1, 2, 3
# MD Modal can, could, may
# NN Noun, singular or mass cat, dog, happiness
# NNS Noun, plural cats, dogs, books
# NNP Proper noun, singular John, London, Google
# NNPS Proper noun, plural Smiths, Apples, Microsoft
# PDT Predeterminer all, both, half
# POS Possessive ending 's, '
# PRP Personal pronoun I, you, he
# PRP$ Possessive pronoun my, your, his
# RB Adverb quickly, very
# RBR Adverb, comparative faster, stronger
# RBS Adverb, superlative fastest, strongest
# RP Particle up, off, down
# SYM Symbol $, %, +
# TO to to
# UH Interjection oh, wow, hey
# VB Verb, base form eat, run, play
# VBD Verb, past tense ate, ran, played
# VBG Verb, gerund or present participle eating, running, playing
# VBN Verb, past participle eaten, run, played
# VBP Verb, non-3rd person singular present eat, run, play
# VBZ Verb, 3rd person singular present eats, runs, plays
# WDT Wh-determiner which, what
# WP Wh-pronoun who, what, whom
# WP$ Possessive wh-pronoun whose
# WRB Wh-adverb where, when, ho

from textblob_de import TextBlobDE as TextBlob #2
import nltk
nltk.download('punkt')

text = "Meine Berliner und Berlinerinnen, ich bin stolz, heute in Ihre Stadt " \
+ "zu kommen als Gast Ihres hervorragenden Regierenden Bürgermeisters, der in allen " \
+ "Teilen der Welt als Symbol für den Kampf- und Widerstandsgeist West-Berlins gilt. Ich " \
+ "bin stolz, auf dieser Reise die Bundesrepublik Deutschland zusammen mit ihrem " \
+ "hervorragenden Herrn Bundeskanzler besucht zu haben, der während so langer Jahre die Politik " \
+ "der Bundesregierung bestimmt hat nach den Richtlinien der Demokratie, der Freiheit " \
+ "und des Fortschritts. Ich bin stolz darauf, heute in Ihre Stadt in der " \
+ "Gesellschaft eines amerikanischen Mitbürgers gekommen zu sein, General Clays, der hier in " \
+ "der Zeit der schwersten Krise tätig war, durch die diese Stadt gegangen ist, und " \
+ "der wieder nach Berlin kommen wird, wenn es notwendig werden sollte. Vor " \
+ "zweitausend Jahren war der stolzeste Satz, den ein Mensch sagen konnte, der: Ich bin ein " \
+ "Bürger Roms. Heute ist der stolzeste Satz, den jemand in der freien Welt sagen kann: " \
+ "Ich bin ein Berliner."

print("\n\n\n")
print("Satz für Satz:")

blob = TextBlob(text)
sentences = blob.sentences
for i in range(len(sentences)):
    print("Satz ", i , ":", sentences[i])
    
    
print("\n\n\n")
print("POS Tags:")
tags = blob.tags
for i in range(len(tags)):
    print("POS Tag ", i , ":", tags[i])

