#!/bin/bash
#NOTE: this requires that we're running this from its own directory.

#migrate pregen files and overwrite
rm -r site_pages/
rm -r pregen_pages/

cp -R pregen_base/* pregen_pages/
cp -R pregen_content/* pregen_pages/

#run python script
python3 scripts/main_gen.py

python3 scripts/update_rss.py

#potentially track different page states with 'content_update' if you want to be able to restore site to a previous state.
#it's a better idea to store this stuff in a seperate repo, FYI.
#git commit
#git checkout content_update
#git add pregen_pages
#git add site_pages
#git commit
