#!/usr/bin/python
import argparse
def getArgs():
	p=argparse.ArgumentParser(
			description="Download a webcomic archive"
			)
	p.add_argument("url",
			help="the URL of the comic to start from"
			)
	'''
	p.add_argument("-i", "--interval",
			dest="interval",
			metavar="seconds",
			nargs=1,
			default=2,
			type=float,
			help="Minimal interval between downloading each comic, to reduce load on the comic server (not yet implemented)"
			)
	'''
	'''
	p.add_argument("-t", "--threads",
			dest="threads",
			metavar="n",
			nargs=1,
			default=1,
			type=int,
			help="Maximum number of simultaneous downloads (not yet implemented)"
			)
	'''
	p.add_argument("-n", "--max",
			dest="max",
			metavar="n",
			default=0,
			type=int,
			help="Maximum number of comics to download. 0 means unlimited"
			)
	p.add_argument("-o", "--out",
			dest="dir",
			metavar="dir",
			default="",
			help="Specify an output directory"
			)
	p.add_argument("-O", "--overwrite",
			dest="overwrite",
			action="store_true",
			help="Force overwriting of downloaded comics. By default, webcomic-dl will not overwrite already-downloaded comics."
			)
	p.add_argument("-f", "--file",
			dest="file",
			help="Specify where to save metadata. By default it is saved in <output_dir>/info.json",
			metavar="file"
			)
	p.add_argument("-m", "--metadata-only",
			dest="meta",
			action="store_true",
			help="Don't download comics, just metadata"
			)
	return p.parse_args()