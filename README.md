# Simple Chatbot

<pre>
pip3 install virtualenv
virtualenv venv
source venv/bin/activate

pip3 install -r requirements.txt

flask run
</pre>

* Use curl to make a POST request to <HOST>/chatbot with the following request body: {'prompt' : 'Hello, how are you today?'}

<pre>
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Hello, how are you today?"}' 127.0.0.1:5000/chatbot
</pre>
