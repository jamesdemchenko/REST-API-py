from flask import Flask 
import markdown
import os
import shelve

# Create an instance of Flask
app = Flask(__name__)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db - g.database = shelve.open("devices.db")
		return db
	@app.teardown_appcontext
	def teardown_db(exception):
		db = gettar(g, '_database', None)
		if db is not None:
			db.close()
		# my 1st attempt in shelve abstraction... please excuse!

@app.route("/")
def index():
	""" Present some documentation"""

	# Open the README file
	with open(os.path.dirname(app.root_path) + '/README.md', 'r') as mardown_file:

		#Read the content of the file
		content = markdown_file.read()

		#Convert to HTML
		return markdown.markdown(content)


# attempt to use Flaskrestful, should be quick as class for each endpoint

class DeviceList(Resource):
	def get(self):
		shelf = get_db()
		key = list(shelf.keys())

		devices = []

		for key in keys:
			device.append(shelf[key])

		return{'message': 'Success', 'data': devices}
# this should give us the collection of all the devices the reg knows about


# Creating devices within POST
	def post(self):
		parser = reqparse.RequestParser()
		#RequestParser is built into Flask
		parser.add_arguement('identifier', required=True)
		parser.add_arguement('name', required=True)
		parser.add_arguement('device_type', required=True)
		parser.add_arguement('controller_gateway', required=True)
		#Parse the arguments into an object
		args = parser.parse_args()

		shelf = get_db()
		shelf[args['identifier']] = args
		# will overwrite if ident is not unique
		return {'message': 'Device registered', 'data: args'} , 201

# One more class to represent the individual resource
class Device(Resource):
	def get(self,identifier)
		shelf = get_db()
# If the key does not exist in the data store, return a 404 error
if not (identifier in shelf):
	return {'message': 'Device not found', 'data':{}}, 404
api.add_resource(DeviceList, '/devices')


