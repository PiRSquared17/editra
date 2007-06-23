###############################################################################
#    Copyright (C) 2007 Cody Precord                                          #
#    staff@editra.org                                                         #
#                                                                             #
#    Editra is free software; you can redistribute it and#or modify           #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation; either version 2 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    Editra is distributed in the hope that it will be useful,                #
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
# FILE: fortran.py                                                            #
# AUTHOR: Cody Precord                                                        #
#                                                                             #
# SUMMARY:                                                                    #
# Lexer configuration module for Fortran f77 and f95                          #
#                                                                             #
# TODO:                                                                       #
#                                                                             #
#-----------------------------------------------------------------------------#
"""

__revision__ = "$Id: Exp $"

#-----------------------------------------------------------------------------#
import synglob

#-----------------------------------------------------------------------------#

#---- Keyword Definitions ----#
# Fortran F77 and F95 keywords
fort_keywords = (0, "access action advance allocatable allocate apostrophe "
                    "assign assignment associate asynchronous backspace bind "
                    "blank blockdata call case character class close common "
                    "complex contains continue cycle data deallocate decimal "
                    "delim default dimension direct do dowhile double "
                    "doubleprecision else elseif elsewhere encoding end "
                    "endassociate endblockdata enddo endfile endforall "
                    "endfunction endif endinterface endmodule endprogram "
                    "endselect endsubroutine endtype endwhere entry eor "
                    "equivalence err errmsg exist exit external file flush fmt "
                    "forall form format formatted function go goto id if "
                    "implicit in include inout integer inquire intent interface "
                    "intrinsic iomsg iolength iostat kind len logical module "
                    "name named namelist nextrec nml none nullify number only "
                    "open opened operator optional out pad parameter pass pause "
                    "pending pointer pos position precision print private "
                    "program protected public quote read readwrite real rec recl "
                    "recursive result return rewind save select selectcase "
                    "selecttype sequential sign size stat status stop stream "
                    "subroutine target then to type unformatted unit use value "
                    "volatile wait where while write")

# Fortran Functions
fort_func = (1, "abs achar acos acosd adjustl adjustr aimag aimax0 aimin0 aint "
                "ajmax0 ajmin0 akmax0 akmin0 all allocated alog alog10 amax0 "
                "amax1 amin0 amin1 amod anint any asin asind associated atan "
                "atan2 atan2d atand bitest bitl bitlr bitrl bjtest bit_size "
                "bktest break btest cabs ccos cdabs cdcos cdexp cdlog cdsin "
                "cdsqrt ceiling cexp char clog cmplx conjg cos cosd cosh count "
                "cpu_time cshift csin csqrt dabs dacos dacosd dasin dasind datan "
                "datan2 datan2d datand date date_and_time dble dcmplx dconjg "
                "dcos dcosd dcosh dcotan ddim dexp dfloat dflotk dfloti dflotj "
                "digits dim dimag dint dlog dlog10 dmax1 dmin1 dmod dnint "
                "dot_product dprod dreal dsign dsin dsind dsinh dsqrt dtan dtand "
                "dtanh eoshift epsilon errsns exp exponent float floati floatj "
                "floatk floor fraction free huge iabs iachar iand ibclr ibits "
                "ibset ichar idate idim idint idnint ieor ifix iiabs iiand iibclr "
                "iibits iibset iidim iidint iidnnt iieor iifix iint iior iiqint "
                "iiqnnt iishft iishftc iisign ilen imax0 imax1 imin0 imin1 imod "
                "index inint inot int int1 int2 int4 int8 iqint iqnint ior ishft "
                "ishftc isign isnan izext jiand jibclr jibits jibset jidim jidint "
                "jidnnt jieor jifix jint jior jiqint jiqnnt jishft jishftc jisign "
                "jmax0 jmax1 jmin0 jmin1 jmod jnint jnot jzext kiabs kiand kibclr "
                "kibits kibset kidim kidint kidnnt kieor kifix kind kint kior "
                "kishft kishftc kisign kmax0 kmax1 kmin0 kmin1 kmod knint knot "
                "kzext lbound leadz len len_trim lenlge lge lgt lle llt log log10 "
                "logical lshift malloc matmul max max0 max1 maxexponent maxloc "
                "maxval merge min min0 min1 minexponent minloc minval mod modulo "
                "mvbits nearest nint not nworkers number_of_processors pack popcnt "
                "poppar precision present product radix random random_number "
                "random_seed range real repeat reshape rrspacing rshift scale "
                "scan secnds selected_int_kind selected_real_kind set_exponent "
                "shape sign sin sind sinh size sizeof sngl snglq spacing spread "
                "sqrt sum system_clock tan tand tanh tiny transfer transpose trim "
                "ubound unpack verify")

# Fortran extended functions
fort_ext = (2, "cdabs cdcos cdexp cdlog cdsin cdsqrt cotan cotand dcmplx dconjg "
               "dcotan dcotand decode dimag dll_export dll_import doublecomplex "
               "dreal dvchk encode find flen flush getarg getcharqq getcl getdat "
               "getenv gettim hfix ibchng identifier imag int1 int2 int4 intc "
               "intrup invalop iostat_msg isha ishc ishl jfix lacfar locking "
               "locnear map nargs nbreak ndperr ndpexc offset ovefl peekcharqq "
               "precfill prompt qabs qacos qacosd qasin qasind qatan qatand "
               "qatan2 qcmplx qconjg qcos qcosd qcosh qdim qexp qext qextd qfloat "
               "qimag qlog qlog10 qmax1 qmin1 qmod qreal qsign qsin qsind qsinh "
               "qsqrt qtan qtand qtanh ran rand randu rewrite segment setdat "
               "settim system timer undfl unlock union val virtual volatile "
               "zabs zcos zexp zlog zsin zsqrt")

#---- End Keyword Definitions ----#

#---- Syntax Style Specs ----#
syntax_items = [('STC_F_COMMENT', 'comment_style'),
                ('STC_F_CONTINUATION', 'default_style'), # NEED STYLE
                ('STC_F_DEFAULT', 'default_style'),
                ('STC_F_IDENTIFIER', 'default_style'),
                ('STC_F_LABEL', 'number2_style'), # NEED STYLE
                ('STC_F_NUMBER', 'number_style'),
                ('STC_F_OPERATOR', 'operator_style'),
                ('STC_F_OPERATOR2', 'operator_style'), # NEED STYLE
                ('STC_F_PREPROCESSOR', 'pre_style'),
                ('STC_F_STRING1', 'string_style'),
                ('STC_F_STRING2', 'string_style'),
                ('STC_F_STRINGEOL', 'stringeol_style'),
                ('STC_F_WORD', 'keyword_style'),
                ('STC_F_WORD2', 'keyword3_style'),
                ('STC_F_WORD3', 'funct_style')]

#---- Extra Properties ----#
fold = ("fold", "1")
fold_comp = ("fold.compact", "1")
#-----------------------------------------------------------------------------#

#---- Required Module Functions ----#
def Keywords(type=0):
    """Returns Specified Keywords List"""
    KEYWORDS = [fort_keywords, fort_func, fort_ext]
    return KEYWORDS

def SyntaxSpec(type=0):
    """Syntax Specifications"""
    return syntax_items

def Properties(type=0):
    """Property Settings"""
    return [fold, fold_comp]

def CommentPattern(type=0):
    """Returns a list of characters used to comment a block of code"""
    if type == synglob.ID_LANG_F77:
        return ['*']
    elif type == synglob.ID_LANG_F95:
        return ['!']
    else:
        return list()

#---- End Required Module Functions ----#

#---- Syntax Modules Internal Functions ----#
def KeywordString():
    """Returns the specified Keyword String"""
    # Unused by this module, stubbed in for consistancy
    return None

#---- End Syntax Modules Internal Functions ----#