#!/bin/bash
bundle exec jekyll build
git checkout gh-pages
cp -r _site/* .
git add -u
git add *
git commit -m 'update site'
git push origin gh-pages
git checkout main
