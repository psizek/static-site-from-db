#OVERVIEW:
This is a tool for generating a set of static website pages from a database. The static website would contain subdirectories for content and a subdirectory named 'all', which would function simlar to the other directories but contains data from each of them.
This specific implementation is for a 'webcomic' format pulling data from a SQLite database, although much of the code could be adapted for any site which publishes 'periodicals' (e.g. a blog), as the underlying principles remain the same.

I've not included/removed a number of test images and data, so if you want this to generate functional pages, you'll need to edit the html forms, or put in your own images. In the future I may update this with 'test' data, such that this generates something that's crudely functional.

#REQUIREMENTS:
python3.7, sqlite, bash (right now this looks for /bin/bash). I'm using pathlib, so this should work on Windows, but I've not tested it there - I've only run this on Linux.

#HOW TO USE (for this specific implementation):

##RE-GENERATE SITE:
run main_gen.sh sourced from the directory it is contained in.

##ADD NEW PAGE:
Put a new image file into content_staging named 'target.png'. Run add_page.sh, and follow the prompts


#FUTURE GOALS:
-fix css
-switch to Jinja2?
-include some 'test' data and images.
-build into more of a command line tool that'd have an 'initialization' option. Given the specifics of some of the code, I'd probably need to restructure a not insignificant portion first, or just use something like django-bakery, which might end up being a seperate project.

#HIGH LEVEL TECHNICAL OVERVIEW:

##FOLDERS:
scripts - contains the majority of scripts used to generate these pages.
forms - contains templates for the static webpages; see scripts/forget.py
main_gen.sh - shell script that generates the site based on a new page.
site_pages - contains the resulting generated site pages.
pregen_base - files that aren't content related which are eventually directly copied to site_pages. Used for things like css, etc.
pregen_content - files that ARE content related which are eventually directly copied to site_pages
pregen_pages - pages that will be directly copied to site_pages
data - contains 'site_data', the sqlite database.
content_staging - This is used by the 'add_page.py' script to rename and store images in the appropriate location.

##script overview:
add_page.py - adds page data to database, and moves content_staging to the appropriate location.
data_classes.py - contains data access classes. In the case of SQLite, each object is a single row.
get_data_fns - data retrieval from objects and the database.
page_gen_fns - generates static page strings.
update_rss.py - generates a new RSS feed.
main_gen.py - generates the site.
setup.py - commonly used strings (like a cursor object for sqlite)
forget.py - replaces tags in templates with strings.

##DB structure:
tblContent - contains data/metadata for site content.
tblFolders - contains metadata for site directories.
