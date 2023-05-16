import json
import requests

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

from third_parties.linkedin import *
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


load_dotenv()

if __name__ == "__main__":
    print("Hello LangChain!")

    linkedin_profile_url = linkedin_lookup_agent(name="Caroline Moraes da Cruz")

    summary_template = """
        Given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # try:
    #     response = requests.get(linkedin_profile_url)
    #     if response.ok:
    #         linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    #         print("Profile found.")
    
    # except:
    #     "Profile not found."

    with open("third_parties/linkedin-carol.json", "r") as file:
        linkedin_data = clean_linkedin_json(json.load(file))

    print(chain.run(information=linkedin_data))
