import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
MY_API_KEY = os.getenv('API_KEY')

def get_car_ai_bio(model, brand, year):
    genai.configure(api_key=MY_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = '''
        Me mostre uma descrição de venda para o carro {} da marca {} do ano {} em apenas 250 caracteres. Fale coisas específicas desse modelo. Pode citar o nome e modelo sem substituir pela palavra "Genai" ou "IA". Não coloque campos para substituição do usuário, pois será inserido diretamente no banco de dados.
    '''
    prompt = prompt.format(model, brand, year)
    response = model.generate_content(prompt)
    return response.text

print(get_car_ai_bio('Fusca', 'Volkswagen', 1970))