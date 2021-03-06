#! /usr/bin/env python3
# coding: utf-8

"""
============================================
  Analyse Woman / Man balance in Politics
============================================
"""
import argparse
import logging as lg
import re

import analysis.csv as c_an
import analysis.xml as x_an

LOG = lg.getLogger('Noemie_ici')
LOG.setLevel(lg.DEBUG)
#lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
    """ Get arguments from the command line
    to get different results according to our needs.
    """
    parser = argparse.ArgumentParser()
    #parser.add_argument("-e", "--extension",
                        # help="""Type of file to analyse. Is it a CSV or an XML ?""")
    parser.add_argument("-d", "--datafile",
                        help="""CSV file containing pieces of information
                        about the members of parliament""")
    #parser.add_argument("-v", "--verdose", action='store_true',
                        # help="""Make the application talk!""")
    parser.add_argument("-i", "--info", action='store_true',
                        help="""information about the file""")
    parser.add_argument("-p", "--byparty", action='store_true',
                        help="""displays a graph for each political party""")
    parser.add_argument("-n", "--displaynames", action='store_true',
                        help="""displays the names of all the mps""")
    parser.add_argument("-s", "--searchname", help="""search for a mp name""")
    parser.add_argument("-I", "--index", help="""displays information about th Ith mp""")
    parser.add_argument("-g", "--groupfirst",
                        help="""displays a graph groupping all the 'g' biggest political parties""")
    parser.add_argument("-a", "--byage",
                        help="""displays a graph for the MPs splitted between those who are over and
                        those who are under the value of --byage""")

    return parser.parse_args()

def main():
    """
    Main instructions to run
    """
    args = parse_arguments()
    #if args.verdose:
    #    lg.basicConfig(level=lg.DEBUG)
    try:
        datafile = args.datafile
        if datafile is None:
            raise Warning('You must indicate a datafile!')
    except Warning as exception:
        lg.warning(exception)
    else:
        res = re.search(r'^.+\.(\D{3})$', args.datafile)
        extension = res.group(1)
        if extension == 'csv':
            c_an.launch_analysis(datafile, \
                args.byparty, args.info, args.displaynames, \
                args.searchname, args.index, args.groupfirst, \
                args.byage)
        elif extension == 'xml':
            x_an.launch_analysis(datafile)
    finally:
        lg.info('###################### Analysis is over ###################')
    #import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()
