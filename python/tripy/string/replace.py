'''
Created on May 22, 2012

@author: cgibson
'''

def replaceWithDict(text, replacements, pattern_block=("${{","}}")):
    
    for k, v in replacements.iteritems():
        replString = "%s%s%s" % (pattern_block[0], k, pattern_block[1])
        text = text.replace(replString, v)
    
    return text