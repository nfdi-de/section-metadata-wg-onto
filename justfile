format:
  npx prettier --prose-wrap always --write --check "**/*.md"

serve:
  # Note that the 4.2.0 tag is important - 4.2.2 (latest, released ~2022) does not work.
  docker run --rm --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve
