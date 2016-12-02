# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

''' this is a comment '''

potato = ('''

this is a multi-line string
	''')

import webapp2

class CustomPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write('<p><a href="http://google.com">Google</a> is a great place</p>')

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

class ManyDogPage(webapp2.RequestHandler):
	def get(self, number):
		self.response.headers['Content-Type'] = 'text/plain'
		woofs = int(number) * 'woof '
		self.response.write(woofs)

class SomeTextPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        s = open('sometext.txt').read( )
        self.response.write(s)

# app URL mapping dictionary
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/cs254', CustomPage),
    ('/dog/(\d+)', ManyDogPage),
    ('/txt', SomeTextPage)
], debug=True)
