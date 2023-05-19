import pprint
import google.generativeai as palm

palm.configure(api_key="AIzaSyBpSCZziasgbYe_eVxJHfkbUhw1F8Ezfd8")

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)