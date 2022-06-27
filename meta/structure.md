# Directory Structure &mdash; Pok&eacute;mon Standards Committee

## `spec/`

All of the standards, in Markdown form. There is YAML metadata for the
information at the top of each file. These are `identifier` (the ID of the
document), `title` (the title of the document), `version` (the version of the
document as `[major, minor, patch]`), and `status` (the status of the document
as a string).

## `meta/`

These documents describe the internal processes of the PSC.

## `tool/`

Scripts to assist with the specifications. Presently, the only script that
exists is `spec2json.py`, a script that converts the specifications to JSON
files.
