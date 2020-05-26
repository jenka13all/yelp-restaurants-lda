#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:34:05 2020

@author: jennifer
"""
import os
import pickle
import gensim
import gensim.corpora

class SavedLdaModel:
    def __init__(self, top_dir, nr_samples, nr_topics):
        self.top_dir = top_dir
        self.nr_samples = nr_samples
        self.nr_topics = nr_topics
        
    def get_model_directory(self):
        return self.top_dir + '/samples_' + str(self.nr_samples) + '/topics_' + str(self.nr_topics) + '/'
    
    def get_model(self):
        dir_name = self.get_model_directory()
        
        if not os.path.exists(dir_name):
            print("There is no model yet for {0} samples with {1} topics.".format(self.nr_samples, self.nr_topics))
            print("To train a model like this, run the create_model_and_params({0}, {1}) command.".format(self.nr_samples, self.nr_topics))
            return
    
        model_file = dir_name + 'lda_model.model'
        
        return gensim.models.ldamodel.LdaModel.load(model_file)
    
    def get_corpus(self):
        dir_name = self.get_model_directory()
        corpus_file = open(dir_name + 'corpus.pickle', "rb")
    
        return pickle.load(corpus_file)
    
    def get_dict(self):
        dir_name = self.get_model_directory()
        id2word_file = dir_name + 'id2word.dct'
    
        return gensim.corpora.Dictionary.load(id2word_file)
        
        
        