#!/usr/bin/python

# $Id: setup.py,v 1.9 2011/10/19 22:06:00 offlinehacker Exp $
# $Log: setup.py,v $
# Revision 1.9  2010/01/28 22:04:00  Paul Hummer
# Fixed tabs in C code. Ew.
# Revision 1.7  2005/01/06 18:27:44  mccabe
# applied patch from Soenke Schwardt, prepared for new version
#
# Revision 1.6  2003/03/30 06:23:11  mccabe
# new release
#
# Revision 1.5  2002/12/21 22:11:37  mccabe
# updated docs
#
# Revision 1.4  2002/12/21 20:30:26  mccabe
# Added id and log entries to most files
#


from distutils.core import setup, Extension

module1 = Extension('pylircmodule',
                    sources = ['pylircmodule.c'],
                    libraries = ['lirc_client'])

setup (name = 'pylirc2',
       version = '0.1',
       author = 'Linus McCabe and Paul Hummer',
       author_email = 'Linus@McCabe.nu',
       license = 'lgpl',
       description = 'Python lirc module. See http://www.lirc.org for more info on lirc and https://launchpad.net/pylirc2 for up-to-date code',
       ext_modules = [module1])
