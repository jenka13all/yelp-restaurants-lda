#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:51:36 2020

@author: jennifer
"""

from saved_lda_model import SavedLdaModel

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  

def get_visualization(top_dir, nr_samples, nr_topics):
    saved_model = SavedLdaModel(top_dir, nr_samples, nr_topics)
    
    lda_model = saved_model.get_model()
    corpus = saved_model.get_corpus()
    id2word = saved_model.get_dict()
    
    # Visualize the topic
    pyLDAvis.enable_notebook()
    vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word)
    
    return vis
    
def save_visualized_model(visualization, top_dir, nr_samples, nr_topics):
    saved_model = SavedLdaModel(top_dir, nr_samples, nr_topics)
    model_vis_file = saved_model.get_model_directory() + 'visualization.html'
    
    pyLDAvis.save_html(visualization, model_vis_file)
    
    print("Your model visualization was saved: {0}".format(model_vis_file))


top_dir = 'models_reduced_30'
   
#best topic clustering
nr_samples = 50000
nr_topics = 11  
vis = get_visualization(top_dir, nr_samples, nr_topics)
save_visualized_model(vis, top_dir, nr_samples, nr_topics)

#this will start an http server and open up the visualization in a browser
#you will have to interrupt the kernel in order to work further with this script
#pyLDAvis.show(vis)

#best coherency score
nr_samples = 50000
nr_topics = 15
vis = get_visualization(top_dir, nr_samples, nr_topics)
save_visualized_model(vis, top_dir, nr_samples, nr_topics)
#pyLDAvis.show(vis)

#poor model from unfiltered dict
top_dir = 'models'
nr_samples = 10000
nr_topics = 50
vis = get_visualization(top_dir, nr_samples, nr_topics)
save_visualized_model(vis, top_dir, nr_samples, nr_topics)
#pyLDAvis.show(vis)
