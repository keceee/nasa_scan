import subprocess
import os

result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
print("PROCESSES:", result.stdout)

print("ENVIRON:", dict(os.environ))

import os
files = os.listdir('/')
print("ROOT:", files)