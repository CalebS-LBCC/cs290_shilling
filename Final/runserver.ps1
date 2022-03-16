Remove-Item 'venv' -Recurse
python3 -m venv venv
venv\Scripts\activate
pip install flask
pip install flask_wtf
flask run
