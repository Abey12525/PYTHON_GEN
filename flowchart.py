"""
Simple parser to compile "flowchart language" into dot.
- All lines starting with # are ignored. 
- Each line is of the form.
"""

import pprint
import re


# B : Start : A
# A : Input something : C
# C : Is input > 10?
#   D:Yes
#   E:No
# E : print "More than 10" : D
# D : Stop 

LINE_RE = re.compile(r"""
(?P<indent>^\s*)             # Indent
(?P<id>[^:]+):               # The id
(?P<label>[^:]+)             # The label
(:\s*)?(?P<target>[^:]+)?       # The target
""", re.X)

def interpret(boxes):
    ret = ['digraph flow {']
    for node,info in boxes.iteritems():
        if "start" in info['label'].lower() or "stop" in info['label'].lower():
            ret.append('   %s [label = "%s"];'%(info['id'], info['label']))
            if info['target']:
                ret.append('   %s -> %s;'%(info['id'], info['target']))
        elif isinstance(info['target'], list):
            ret.append('   %s [shape=diamond, label="%s"] ;'%(info['id'], info['label']))
            for port, target in zip(['e','s'], info['target']):
                ret.append('   %s:%s -> %s [label="%s"];'%(info['id'].strip(), port, target['target'], target['label']))
        else:
            ret.append('   %s [label = "%s", shape=box];'%(info['id'], info['label']))
            ret.append('   %s -> %s;'%(info['id'], info['target']))
    ret.append('}')
    return ret
            

            
        


def parse(input_file):
    boxes = dict()
    with open(input_file) as f:
        decision_box = False
        for line in f:
            if line.startswith("#") or not line.strip():
               continue
            m = LINE_RE.match(line.rstrip())
            if not m:
                raise SyntaxError("Couldn't parse '%s'"%line)

            d = m.groupdict()

            if d["indent"]:
                if not decision_box:
                    raise SyntaxError("Branching without previous decision box at '%s'"%line)
                else:
                    if boxes[decision_box]['target'] is None:
                        boxes[decision_box]['target'] = []
                    boxes[decision_box]['target'].append(dict(label = d['label'],
                                                              target =d['id']))
            elif not d['target']: # We have just looked at a decision box now
                decision_box = d['id']
                boxes[d['id']] = d
            else:
                boxes[d['id']] = d
                decision_box = False

    return boxes
            

def main(input_file):
    tree = parse(input_file)
    output = interpret(tree)
    for i in output:
        print i


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
    
