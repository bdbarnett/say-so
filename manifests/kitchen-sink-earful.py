# The PyDevices kitchen sink, earful (a Spotify Connect speaker), and sayso
# with the remote, frozen: one standalone micropython.exe (or board image)
# that is both the remote and the speaker. Assumes the workspace layout:
# ~/gh/pydevices/micropython and ~/gh/bdbarnett/{earful,sayso}.
#   make ... FROZEN_MANIFEST=/home/brad/gh/bdbarnett/sayso/manifests/kitchen-sink-earful.py
include("$(MPY_DIR)/../../bdbarnett/earful/manifests/kitchen-sink.py")
include("../manifest.py")
