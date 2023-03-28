# glinda
quick and dirty script for doing multi-file exports using melt and ShotCut

ShotCut .mlt files are compatible with the melt renderer, but need extra
command line parameters.

This script takes (or finds) .mlt files under the current directory and then
renders .mp4 files into an existing `_rendered` directory.

The script is pretty fragigle and based on macOS. For other platforms, replace
the `MELT` global with the path to your `melt` executable that comes with
ShotCut.

For other argument sets, do an export inside of ShotCut with your desired
settings, then right click the job and "View XML". Save the XML and parse out
the `<consumer>` tag. Each key/value pair in `<consumer>` goes in the
`RENDER_ARGS` dictionary. Remove the `target` field from the dict.

If you're not producing an `.mp4` file, you'll also need to hack the `parms`
value near the bottom of the script to set the `avformat:` and output filename
to your desired extension.

Like I said, quick and dirty.
