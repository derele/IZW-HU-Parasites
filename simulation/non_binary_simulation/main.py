"""main method"""

from copy import deepcopy
from pprint import pprint

from Bio import Phylo

import buildTree
import Parsimony
import Parsimony_like
import Drawings

def main():
    """Main method"""
    number_trees = 1    # number of simulated trees
    number_leafnodes = 100
    percentage = 40   # percentage of parasites (percentage +-5%)
    binary_trees = []
    for _ in range(0, number_trees):
        result = buildTree.get_random_tagged_tree(number_leafnodes, percentage)
        current_tree = result[0]
        nodelist = result[1]
        binary_trees.append(current_tree)
        # pprint(nodelist)
        # Phylo.draw(current_tree)
        # ---------------- non-binary tree ----------------
        buildTree.get_non_binary_tree(current_tree.clade, nodelist)
        # Phylo.draw(current_tree)
        # # ---------------- parsimony ----------------
        parsimony_tree = deepcopy(current_tree)
        parsimony_nodelist = deepcopy(nodelist)
        Parsimony.parsimony(parsimony_tree.clade, parsimony_nodelist)
        # # ---------------- parsimony like ----------------
        # Parsimony_like.parsimony_like(current_tree.clade, nodelist)
        # # ---------------- drawings ----------------
        # do_some_drawings(current_tree, nodelist, parsimony_tree, parsimony_nodelist)

    # save treelist in a newick file
    # Phylo.write(binary_trees, 'originalTrees.tre', 'newick')
    return

def do_some_drawings(tree, nodelist, parsimony_tree, parsimony_nodelist):
    """seperated drawings"""
    tree.name = 'random tree'
    # Phylo.draw(tree)
    named_tree = deepcopy(tree)
    named_tree.name = 'tagged tree'
    Drawings.tag_names(named_tree.clade, nodelist, 1)
    Phylo.draw(named_tree)
    untagged_tree = deepcopy(tree)
    untagged_tree.name = 'untagged tree'
    Drawings.tag_leaf_names(untagged_tree.clade, nodelist)
    # Phylo.draw(untagged_tree)
    # tree.name = 'parsimony down'
    # Phylo.draw(tree)
    # tree.name = 'parsimony up'
    # Phylo.draw(tree)
    parsimony_tree.name = 'parsimonious solution tree'
    Drawings.tag_names(parsimony_tree.clade, parsimony_nodelist, 2)
    Phylo.draw(parsimony_tree)
    parsimony_like_tree = deepcopy(tree)
    parsimony_like_tree.name = 'parsimonious-like solution tree'
    Drawings.tag_names(parsimony_like_tree.clade, nodelist, 2)
    Phylo.draw(parsimony_like_tree)
    # Phylo.draw_graphviz(parsimony_tree)
    # pylab.show()

main()


# from rpy2 import robjects
# from rpy2.robjects import Formula, Environment
# from rpy2.robjects.vectors import IntVector, FloatVector
# from rpy2.robjects.lib import grid
# from rpy2.robjects.packages import importr, data
# from rpy2.rinterface import RRuntimeError
# import warnings

# # The R 'print' function
# rprint = robjects.globalenv.get("print")
# stats = importr('stats')
# grdevices = importr('grDevices')
# base = importr('base')
# datasets = importr('datasets')


# import math, datetime
# import rpy2.robjects.lib.ggplot2 as ggplot2
# import rpy2.robjects as ro
# from rpy2.robjects.packages import importr
# base = importr('base')

# mtcars = data(datasets).fetch('mtcars')['mtcars']

# pp = ggplot2.ggplot(mtcars) + \
#      ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
#      ggplot2.geom_point() + \
#      ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),
#                          method = 'lm')
# pp.plot()

# def main():
#     """Main method"""
#     number_leafnodes = 80
#     lower_range = 35
#     upper_range = 45
#     result = buildTree.get_random_tagged_tree(number_leafnodes, lower_range, upper_range)
#     tree = result[0]
#     nodelist = result[1]
#     tree.name = 'tree'
#     Phylo.draw(tree)
#     changed_tree = deepcopy(tree)
#     set_limits(changed_tree.clade, [], -1)
#     changed_tree.name = 'tree with limits'
#     Phylo.draw(changed_tree)
#     un_binary_tree(changed_tree.clade, 0.5)
#     changed_tree.name = 'not binary tree'
#     Phylo.draw(changed_tree)
#     return

