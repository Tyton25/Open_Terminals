!#/usr/bin/python2


import csv, optparse, os, sys
from itertools import chain
from collections import OrderedDict

gnometerm = 'gnome-terminal '

options.parser = p.parser()
	add_options('t', '--terms',
		action='store',
		name='numterms',
		type='int',
		nargs=1,
		help='Enter the number of terminals to open.')
	add_option('n', '--numtabs',
		action='store',
		type='int',
		nargs=1,
		help='Enter the number of tabs to open.')
	add_options('-f', '--file',
		action='store',
		name='input_file',
		type='string',
		nargs=1,
		help='CSV file with tab titles and VMs.')

	(opts, args) = p.parse_args()
		if opts.numterms:
			terms = opts.numterms
			open_terms = gnometerm + '&'
			for i in terms:
				os.system(open_terms)
		if opts.numtabs:
			num_tabs = opts.numtabs
			tabs = ' --tabs;'
			open_tabs = gnometerm
			for i in num_tabs:
				open_tabs = open_tabs + tabs
			open_tabs = ope_tabs + ' &'
			os.system(open_tabs)
		if opts.input_file:
			infile = csv.reader(open(opts.input_file, 'rU'), delimiter = '\t')
			rows = list(opts.infile)
			open_terms_cmd = vm_login(rows)
			os.system(open_terms_cmd)

def vm_login(vm):
	gnome_terms = 'gnome-terminal'
	term_tabs = ' --tabs --title '

	for i in range(len(vm)):
		for j in range(len(vm[i])-1):
			vmi = vm[i][j]
			vmj = vm[i][1]
			vmssh = (" -e 'ssh -X %s'" % vmj)
			gnome_terms = gnome_terms + term_tabs + vmssh
		gnome_terms = gnome_terms + ' &'
	return gnome_terms

if __name__=='__main__':
	main()
