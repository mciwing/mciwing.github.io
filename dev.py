import os
import subprocess
import sys

env = os.environ.copy()
env["ENABLE_GIT_COMMITTERS"] = "false"
env["ENABLE_GIT_REVISION_DATE"] = "false"

result = subprocess.run(["uv", "run", "mkdocs", "serve"], env=env)
sys.exit(result.returncode)