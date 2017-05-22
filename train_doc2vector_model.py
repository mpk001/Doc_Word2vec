#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import multiprocessing

from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedLineDocument

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 4:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]

    model = Doc2Vec(TaggedLineDocument(inp), size=200, window=5, min_count=5, workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)#save dov2vec
    model.save_word2vec_format(outp2, binary=False)#save word2vec