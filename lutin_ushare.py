#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug
import os

def get_type():
	return "BINARY"

def get_name():
	return "micro-share"

def get_desc():
	return "UPNP server"

def get_licence():
	return "GPL-3"
#
#def get_compagny_type():
#	return "org"
#
#def get_compagny_name():
#	return ""
#
def get_maintainer():
	return ["Mr DUPIN Edouard <yui.heero@gmail.com>"]

def get_version():
	return [1,1,"dev"]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_extra_compile_flags()
	my_module.add_src_file([
		'src/http.c',
		'src/services.c',
		'src/ushare.c',
		'src/content.c',
		'src/trace.c',
		'src/cms.c',
		'src/redblack.c',
		'src/util_iconv.c',
		'src/osdep.c',
		'src/mime.c',
		'src/cfgparser.c',
		'src/metadata.c',
		'src/msr.c',
		'src/cds.c',
		'src/presentation.c',
		'src/buffer.c',
		'src/ctrl_telnet.c'
		])
	my_module.add_path(tools.get_current_path(__file__))
	my_module.compile_flags('c', [
		"-D_LARGEFILE_SOURCE",
		"-D_FILE_OFFSET_BITS=64",
		"-D_REENTRANT",
		"-D_GNU_SOURCE",
		"-DHAVE_SETLOCALE",
		"-DHAVE_IFADDRS_H",
		"-DHAVE_LANGINFO_CODESET",
		"-DHAVE_ICONV",
		"-pthread",
		"-I/usr/include/upnp"
		])
	my_module.compile_flags('link', [
		"-lixml",
		"-lthreadutil",
		"-lpthread",
		"-lupnp",
		"-pthread"
		])
	return my_module
