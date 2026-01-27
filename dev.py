import os
import subprocess
import sys

env = os.environ.copy()
env["ENABLE_GIT_AUTHORS_SERVE"] = "false"
env["ENABLE_GIT_REVISION_DATE"] = "false"

# workaround to enable live reload
# see https://github.com/squidfunk/mkdocs-material/issues/8478
result = subprocess.run(
    ["uv", "run", "mkdocs", "serve", "--livereload"], env=env
)
sys.exit(result.returncode)
