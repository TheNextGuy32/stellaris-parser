# Stellaris Parser

[![Build Status](https://travis-ci.com/RobRoseKnows/stellaris-parser.svg?branch=master)](https://travis-ci.com/RobRoseKnows/stellaris-parser)

Yeah this is a thing I'm making to help with another project I'm working on. This part is
open source because it's useful for others. WIP, does not work at this time. Pull requests
will likely auto-fail Travis due to the secret environment variables. Don't try anything at
this time.

## Uploading Game Files

I'm currently storing the game data files for testing in an S3 bucket so they can be used by
Travis CI. These are instructions for me, as well as anyone else who wants to roll their own,
to upload new datafiles.

1. Copypasta new game version into `game_files/`.
2. Add new version to frozenset `versions` in [aws_tools/common.py](aws_tools/common.py).
3. Run `python aws_tools/upload.py game_files/ <bucket-name> game_files/` from repo root.
4. You may want to pipe the output into a separate file because it'll print a lot of stuff.
5. You may need to move stuff around in S3 console as it doesn't always upload exactly where you'd like.