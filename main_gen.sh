#!/bin/bash
#NOTE: this requires that we're running this from its own directory.

#migrate pregen files and overwrite
rm -r site_pages/
rm -r pregen_pages/

mkdir pregen_pages
mkdir site_pages/

cp -R pregen_base/* pregen_pages/
cp -R pregen_content/* pregen_pages/

#run python script
cp -R pregen_pages/* site_pages/
python3 scripts/main_gen.py

python3 scripts/update_rss.py

#git commit
#git checkout content_update
#git add pregen_pages
#git add site_pages
#git commit
