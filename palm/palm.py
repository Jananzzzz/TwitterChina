# use LLM for news generation

import pprint
import google.generativeai as palm
import config

palm.configure(api_key=config.palm_api)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)