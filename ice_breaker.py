import json

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

from third_parties.linkedin import *


load_dotenv()

information = """
Elon Reeve Musk FRS (Pretória, 28 de junho de 1971) é um empreendedor,[2] empresário e filantropo sul-africano-canadense, naturalizado norte-americano. Ele é o fundador, diretor executivo e diretor técnico da SpaceX; CEO da Tesla, Inc.; vice-presidente da OpenAI, fundador e CEO da Neuralink; cofundador, presidente da SolarCity e proprietário do Twitter. Em dezembro de 2022, tinha uma fortuna avaliada em US$ 139 bilhões de dólares, tornou-se a segunda pessoa mais rica do mundo, de acordo com a Bloomberg, atrás apenas do empresário Jeff Bezos.[3][4][5]

Musk demonstrou publicamente preocupações com a extinção humana[6] e também propôs soluções, das quais algumas são o objetivo principal de suas empresas e já estão sendo feitas na prática. Entre elas, a redução do aquecimento global, através do uso de energias renováveis, um projeto multiplanetário, mais especificamente a colonização de Marte,[7] e o desenvolvimento seguro da inteligência artificial.

Em janeiro de 2011, uma de suas empresas, a SpaceX, tornou-se a primeira empresa no mundo a vender um voo comercial à Lua. A missão, marcada para 2013, foi contratada pela empresa Astrobotic Technology, tendo como objectivo colocar um pequeno jipe na superfície lunar, o que não aconteceu. Em 2012, encerrou o projeto do Tesla Roadster, o primeiro modelo da sua autoria, um carro totalmente elétrico que custava cerca de 92 mil dólares. A Tesla já lançou quatro modelos: S, Y, X e o Modelo 3, este último com a responsabilidade de trazer os carros elétricos para as massas, partindo de um custo inicial de 35 mil dólares.[8] Em 25 de abril de 2022, ele também concordou em comprar o Twitter por 44 bilhões de dólares.[9]

Musk tem sido alvo de críticas devido a posturas incomuns ou não científicas e controvérsias altamente divulgadas. Em 2018, ele foi processado por difamação por um britânico que ajudou no resgate da caverna de Tham Luang; um júri da Califórnia decidiu a favor de Musk. No mesmo ano, ele foi processado pela Comissão de Valores Mobiliários dos Estados Unidos (SEC) por tweetar falsamente que havia garantido o financiamento para uma aquisição da Tesla. Ele fez um acordo com a SEC, deixando temporariamente sua presidência e aceitando limitações ao uso do Twitter. Musk também foi criticado por espalhar desinformação sobre a pandemia de COVID-19 e recebeu críticas de especialistas por suas outras opiniões sobre assuntos como inteligência artificial, criptomoedas e transporte público.
"""


if __name__ == "__main__":
    print("Hello LangChain!")

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

    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/caroline-moraes-da-cruz/")
    with open("third_parties/linkedin-carol.json", "r") as file:
        linkedin_data = clean_linkedin_json(json.load(file))

    print(chain.run(information=linkedin_data))
