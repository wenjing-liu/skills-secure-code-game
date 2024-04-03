# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_prof_picture(self, path=None):
        if not path:
            return None

        safe_path = self._sanitize_path(path)
        if not safe_path:
            return None

        return safe_path

    def get_tax_form_attachment(self, path=None):
        if not path:
            raise ValueError("Tax form path is required")

        safe_path = self._sanitize_path(path)
        if not safe_path:
            return None

        return safe_path

    def _sanitize_path(self, path):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        safe_path = os.path.normpath(os.path.join(base_dir, path))

        if not os.path.commonpath([base_dir, safe_path]) == base_dir:
            return None

        return safe_path

    def _read_file(self, path):
        try:
            with open(path, 'rb') as file:
                return bytearray(file.read())
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error reading file: {e}")
            return None