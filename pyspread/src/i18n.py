# -*- coding: utf-8 -*-

import os
import locale
import gettext
import sys

#  The translation files will be under
#  @LOCALE_DIR@/@LANGUAGE@/LC_MESSAGES/@APP_NAME@.mo
APP_NAME = "pyspread"

# This is ok for maemo. Not sure in a regular desktop:
APP_DIR = os.path.join(sys.prefix, 'share')

# .mo files will then be located in APP_Dir/i18n/LANGUAGECODE/LC_MESSAGES/
LOCALE_DIR = os.path.join(APP_DIR, 'i18n')


# Now we need to choose the language. We will provide a list, and gettext
# will use the first translation available in the list
DEFAULT_LANGUAGES = os.environ.get('LANGUAGES', '').split(':')
DEFAULT_LANGUAGES += ['en_US']

lc, encoding = locale.getdefaultlocale()
if lc:
    languages = [lc]

# Concat all languages (env + default locale),
#  and here we have the languages and location of the translations
languages += DEFAULT_LANGUAGES
mo_location = LOCALE_DIR

# Lets tell those details to gettext
gettext.install(True, localedir=None, unicode=1)

gettext.find(APP_NAME, mo_location)

gettext.textdomain(APP_NAME)

gettext.bind_textdomain_codeset(APP_NAME, "UTF-8")

language = gettext.translation(APP_NAME, mo_location, languages=languages,
                               fallback=True)