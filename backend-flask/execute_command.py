import subprocess

flask_command = 'flask run --host=0.0.0.0 --port=4567'

subprocess.run(flask_command, shell=True)
