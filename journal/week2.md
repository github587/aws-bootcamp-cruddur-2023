## HONEYCOMB

login to honeycomb
create a new envieonment called bootcamp (choose purple)
get eh API KEy fror botcamp

4npqlMeqSQZv2Hsiq3PMRF

export HONEYCOMB_API_KEY="4npqlMeqSQZv2Hsiq3PMRF"
gp env HONEYCOMB_API_KEY="4npqlMeqSQZv2Hsiq3PMRF"

1.export makes it avaialnel for any subcommand getting its own sub shell
2. so both export and gp env are needed.

check using env | grep HONEY

3. In docker compose.yml , set each service its own OTEL_SERVICE_NAME:
for backend-flask it is set in environmetnt:
OTEL_SERVICE_NAME: 'backend-flask'

4. open requirements.txt and  add the following to install the following
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests

5. on the terminal, execute the following
pip install -r requirements.txt

6. add initializers as follows to app.pyS
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

7. add iniitialize tracing and exporter as follows to app.py
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

OLTPSPANEXPorter reads the configuration to see where to send the scans. YOu could pass in the endpoint as a param as well.

8. cd to frontend-react-js and run npm i.
9. right click on docker-compose.yml and compose up to bring up the containers.
10. to make the port uncloeked by default whent he container is up and running, add the following to gitpod.yml
ports:
  - name: frontend
    port: 3000
    onOpen: open-browser
    visibility: public
  - name: backend
    port: 4567
    visibility: public
  - name: xray-daemon
    port: 2000
    visibility: public

10. Encountered a failure to export batch node 401 error.
Troubleshooted with docker compose up -d on terminal and figure dthe HONEYCOMB_API_KEY went missing. Set that up and ran docker compose up -d again and got the scans on the logs aand on honeycomb UI as dataset.



11. to createa  span around the section of the flow, to introduce a story, add a trace around where needed using:

from opentelemetry import trace
tracer = trace.get_tracer("home.activities")

12. to pass custom variable values, use "app." such as in

  span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      


## AWS X-RAY:
1. Similar to honey comb, when using lambda, EBS easier to configure , with ECS containers it is harder.Instrumenting is harder.


X-RAY 

for it to work, must to have a x-ray daemon - another container/app that runs alongside the app to send the data to , collects , batches and sends to xray api.

Added npm i as a command task 

Install aws sdk
(a) add aws-xray-sd command to requiremtns.txt
(b) on the terminal, cd to backend-flask and run
pip install -r requirements.txt

  ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
  ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


## CLOUDWATCH

install watchtower for python

add to requiemts.txt watchtower
cd to backednd-flask
pip install requiremtns.txt


1. add to app.py the follwoing to import logger, declare and instantitate.

In app.py, Modify the run call to pass in logger habandle.

In homeactiivites.py, modify the run call to take in logger as a parameter and log a custom message at teh start of the run call.

3. Docker compose up to deply the changes and verify the home backend url to log a custom in home activiites message.

5. Login to Cloidwatch logs, go to log groups, select "Cruddur" and then make sure the log traces containt the log messges added to the code.




## ROLLBAR
1. Add to requirements.txt
blinker
rollbar

install dependencies using pip install requirements.txt

pip install -r requirements.txt


get teh access token from rollbar "Integrate sdk" section when logged in,

and set gp env ROLLBAR_ACCESS_TOKEN=""

impotrt rollbasr to app.py, add a method to initialize rollbar with the rollbartoken.
add an endpoint called test to app.py  to test rollbar.


  ![rollbar_error_return_issue]("/assets/rollbar_error_return_issue_proof.png")
  ![Rollbar_screen_proof]("rollbar_screen_proof/assets/.png")






