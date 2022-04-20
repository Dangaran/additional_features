#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Daniel García Angulo
"""

import pandas as pd
from plotnine import *

class preliminary_plots():
    '''
    Class to create preliminary plots for 2 variables.
    Input:
        - pandas_db: pandas dataframe with the variables to plot
        - x_axis: column name as string to plot in x axis
        - y_axis: column name as string to plot in y axis
    Output:
        - Plot from selected option
    
    Select option manual = True in each method to check the available options before using them
    '''
    
    
    def __init__(self, pandas_db, x_axis, y_axis):
        self.db = pandas_db
        self.x = x_axis
        self.y = y_axis
        
    @staticmethod
    def _replace_underscores(text):
        if text.find('_') != -1:
            text = text.replace('_', ' ')
        return text
        
    def scatterplot(self, title = None, manual = False):
        if manual:
            print('Available options:\n\t- title = str, title to show')
            pass
        else:
            p1 = ggplot(self.db, aes(x= self.x, y= self.y)) +\
                        geom_point() +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p1 = p1 + ggtitle(title)
            return p1
    
    def lineplot(self, x_string = False, title = None, manual = False):
        if manual:
            print('Available options:\n\t- x_string = bool, Default=False if x values are numbers | True=if x values are strings\n\t- title = str, title to show')
            pass
        else:
            if x_string:
                p2 = ggplot(self.db, aes(x= self.x, y= self.y, group = 1)) +\
                            geom_line() +\
                            labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                            theme_classic()
            else:
                p2 = ggplot(self.db, aes(x= self.x, y= self.y)) +\
                        geom_line() +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p2 = p2 + ggtitle(title)
            return p2
    
    def barplot(self, stat_value = 'identity', title = None, manual = False):
        if manual:
            print('Available options:\n\t- stat_value = str, Default="identity" | Modify stat option from geom_bar\n\t- title = str, title to show')
            pass
        else:
            p3 = ggplot(self.db, aes(x= self.x, y= self.y)) +\
                        geom_bar(stat = stat_value) +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p3 = p3 + ggtitle(title)                 
            return p3
    
    def densityplot(self, stat_value = 'identity', fill_col = '#0BCCCA', title = None, manual = False):
        if manual:
            print('Available options:\n\t- stat_value = str, Default="identity" | Modify stat option from geom_density\n\t- fill_col = str, Default="#0BCCCA" | Modify fill color option\n\t- title = str, title to show')
            pass
        else:
            p4 = ggplot(self.db, aes(x= self.x, y= self.y)) +\
                        geom_density(stat = stat_value, fill = fill_col) +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p4 = p4 + ggtitle(title)
            return p4
    
    def histogram(self, x = '', bins = 10, title = None, manual = False):
        if manual:
            print('Available options:\n\t- bins = int, Default=10 | Modify bins option from geom_histogram\n\t- title = str, title to show')
            pass
        else:
            if not x: x = self.x
            p5 = ggplot(self.db, aes(x= x)) +\
                        geom_histogram(bins = bins) +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p5 = p5 + ggtitle(title)
            return p5
    
    def boxplot(self, flip_coord = False, title = None, manual = False):
        if manual:
            print('Available options:\n\t- flip_coord = bool, Default=False | True=Flip x and y axis\n\t- title = str, title to show')
            pass
        else:
            db_boxplot = self.db
            db_boxplot[self.x] = db_boxplot[self.x].astype(str)
            p6 = ggplot(db_boxplot, aes(x= self.x, y= self.y)) +\
                        geom_boxplot() +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            if flip_coord: p6 = p6 + coord_flip()
            if title: p6 = p6 + ggtitle(title)
            return p6

    def countplot(self, title = None, manual = False):
        if manual:
            print('Available options:\n\t- title = str, title to show')
            pass
        else:
            p7 = ggplot(self.db, aes(x= self.x, y= self.y)) +\
                        geom_count() +\
                        labs(x = self._replace_underscores(self.x).title(), y = self._replace_underscores(self.y).title()) +\
                        theme_classic()
            
            if title: p7 = p7 + ggtitle(title)
            return p7
    

