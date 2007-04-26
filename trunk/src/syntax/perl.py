###############################################################################
#    Copyright (C) 2007 Cody Precord                                          #
#    cprecord@editra.org                                                      #
#                                                                             #
#    This program is free software; you can redistribute it and#or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation; either version 2 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program; if not, write to the                            #
#    Free Software Foundation, Inc.,                                          #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.                #
###############################################################################

"""
#-----------------------------------------------------------------------------#
# FILE: perl.py                                                               #
# AUTHOR: Cody Precord                                                        #
#                                                                             #
# SUMMARY:                                                                    #
# Lexer configuration module for Perl.                                        #
#                                                                             #
# TODO:                                                                       #
#                                                                             #
#-----------------------------------------------------------------------------#
"""

__revision__ = "$Id: Exp $"

#-----------------------------------------------------------------------------#

#---- Keyword Specifications ----#

# Perl Keywords
perl_kw = (0, "if elseif unless else switch eq ne gt lt ge le cmp not and or "
              "xor while for foreach do until continue defined undef and or "
              "not bless ref BEGIN END my local our goto return last next redo "
              "chomp chop chr crypt index lc lcfirst length org pack reverse "
              "rindex sprintf substr uc ucfirst pos quotemet split study abs "
              "atan2 cos exp hex int log oct rand sin sqrt srand spice unshift "
              "shift push pop split join reverse grep map sort unpack each "
              "exists keys values tie tied untie carp confess croak dbmclose "
              "dbmopen die syscall binmode close closedir eof fileno getc "
              "lstat print printf readdir readline readpipe rewinddir select "
              "stat tell telldir write fcntl flock ioctl open opendir read "
              "seek seekdir sysopen sysread sysseek syswrite truncate pack vec "
              "chdir chmod chown chroot glob link mkdir readlink rename rmdir "
              "symlink umask ulink utime caller dump eval exit wanarray require "
              "import alarm exec fork getpgrp getppid getpriority kill pipe "
              "setpgrp setpriority sleep system times wait waitpid accept "
              "bind connect getpeername getsockname getsockopt listen recv "
              "send setsockopt shutdown socket socketpair msgctl msgget msgrcv "
              "msgsnd semctl semget semop shmctl shmget shmread shmwrite "
              "endhostent endnetent endprooent endservent gethostbyaddr "
              "gethostbyname gethostent getnetbyaddr getnetbyname getnetent "
              "getprotobyname getprotobynumber getprotoent getervbyname "
              "getservbyport getservent sethostent setnetent setprotoent "
              "setservent getpwuid getpwnam getpwent setpwent endpwent getgrent "
              "getgrgid getlogin getgrnam setgrent endgrent gtime localtime time "
              "times warn formline reset scalar delete prototype lock new "
              "NULL __FILE__ __LINE__ __PACKAGE__ __DATA__ __END__ AUTOLOAD "
              "BEGIN CORE DESTROY END EQ GE GT INIT LE LT NE CHECK use sub elsif")

#---- Syntax Style Specs ----#
syntax_items = [ ('STC_PL_DEFAULT', 'default_style'),
                 ('STC_PL_ARRAY', 'array_style'),
                 ('STC_PL_BACKTICKS', 'btick_style'),
                 ('STC_PL_CHARACTER', 'char_style'),
                 ('STC_PL_COMMENTLINE', 'comment_style'),
                 ('STC_PL_DATASECTION', 'default_style'), # STYLE ME
                 ('STC_PL_ERROR', 'error_style'),
                 ('STC_PL_HASH', 'global_style'),
                 ('STC_PL_HERE_DELIM', 'here_style'),
                 ('STC_PL_HERE_Q', 'here_style'),
                 ('STC_PL_HERE_QQ', 'here_style'),
                 ('STC_PL_HERE_QX', 'here_style'),
                 ('STC_PL_IDENTIFIER', 'default_style'),
                 ('STC_PL_LONGQUOTE', 'default_style'), # STYLE ME
                 ('STC_PL_NUMBER', 'number_style'),
                 ('STC_PL_OPERATOR', 'operator_style'),
                 ('STC_PL_POD', 'default_style'), #STYLE ME
                 ('STC_PL_PREPROCESSOR',  'pre_style' ),
                 ('STC_PL_PUNCTUATION', 'default_style'), # STYLE ME
                 ('STC_PL_REGEX', 'regex_style'),
                 ('STC_PL_REGSUBST', 'regex_style'),
                 ('STC_PL_SCALAR', 'scalar_style'),
                 ('STC_PL_STRING', 'string_style'),
                 ('STC_PL_STRING_Q', 'string_style'),
                 ('STC_PL_STRING_QQ', 'string_style'),
                 ('STC_PL_STRING_QR', 'string_style'),
                 ('STC_PL_STRING_QW', 'string_style'),
                 ('STC_PL_STRING_QX', 'string_style'),
                 ('STC_PL_SYMBOLTABLE', 'default_style'), # STYLE ME
                 ('STC_PL_WORD', 'keyword_style') ]

#---- Extra Properties ----#
fold = ("fold", "1")
fld_compact = ("fold.compact", "1")
fld_comment = ("fold.comment", "1")
fld_pod = ("fold.perl.pod", "1")
fld_pkg = ("fold.perl.package", "1")
#-----------------------------------------------------------------------------#

#---- Required Module Functions ----#
def Keywords(type=0):
    """Returns Keyword Specifications List"""
    KEYWORDS = [perl_kw]
    return KEYWORDS

def SyntaxSpec(type=0):
    """Syntax Specifications"""
    return syntax_items

def Properties(type=0):
    """Extra Properties"""
    return [ fold ]

def CommentPattern(type=0):
    """Returns a list of characters used to comment a block of code"""
    return [ u'#' ]
#---- End Required Module Functions ----#

#---- Syntax Modules Internal Functions ----#
def KeywordString(option=0):
    """Returns the keyword string"""
    return perl_kw[1]

#---- End Syntax Modules Internal Functions ----#

#-----------------------------------------------------------------------------#