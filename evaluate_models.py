#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:31:44 2020

@author: jennifer
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def create_coherence_score_comparison(models_dir):
    #compile coherence scores for different models
    rows_list = []
    
    for top_dir, sub_dirs, files in os.walk(models_dir):
        if(len(files) > 1):
            #get nr_samples, nr_topics, and coherence_score file
            paths = top_dir.split('/')
            nr_samples = paths[1].split('_')[1]
            nr_topics = paths[2].split('_')[1]
            
            coherence_file = top_dir + '/coherence_score.txt'
    
            #get coherence score
            with open(coherence_file, 'r') as f:
                for score in f.readlines():
                    coherence_score = score
                    
            #add a row to the dictionary
            dict1 = {}
            dict1.update({
                'nr_samples': nr_samples,
                'nr_topics': nr_topics,
                'c_score': coherence_score
            })
            rows_list.append(dict1)    
            
    df = pd.DataFrame(rows_list) 
    
    #write the data frame to csv so we can use it later without recomputing
    coherence_compare_file = models_dir + '/coherence_scores.csv'
    df.to_csv(coherence_compare_file, sep="\t", index=False)
    
    print("Your coherence score comparison data was written to {0}".format(coherence_compare_file))

def create_and_save_plot(models_dir):
    #have we already computed the coherence score file?
    coherence_compare_file = models_dir + '/coherence_scores.csv'
    if not os.path.isfile(coherence_compare_file):
        create_coherence_score_comparison(models_dir) 
        
    #read out the file into a data frame
    scores = pd.read_csv(coherence_compare_file, sep="\t", index_col=None)

    #plot coherence scores for the different models
    data_samples = scores.sort_values('nr_topics')
    plt.plot('nr_topics', 'c_score', data=data_samples)
    
    plt.title('Coherency scores for ' + models_dir)    
    plt.xlabel('Nr. of Topics')
    plt.ylabel('Coherency Score')
    
    #save the image to file
    coherence_score_img = models_dir + '/coherence_scores.png'
    plt.savefig(coherence_score_img)
    
    print("Your coherence score plot for {0} was written to {1}".format(models_dir, coherence_score_img))

#models_dir = 'models_cheap'
models_dir = 'models_exp'
create_and_save_plot(models_dir)
  

