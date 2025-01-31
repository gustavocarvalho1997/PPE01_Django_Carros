import google.generativeai as genai

def get_car_ai_bio(model, brand, year):
    genai.configure(api_key='AIzaSyDvPA-JKLqF6PArL2gye4vz1GmmQxp17cE')
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = '''
        Me mostre uma descrição de venda para o carro {} da marca {} do ano {} em apenas 250 caracteres. Fale coisas específicas desse modelo. Pode citar o nome e modelo sem substituir pela palavra "Genai" ou "IA".
    '''
    prompt = prompt.format(model, brand, year)
    response = model.generate_content(prompt)
    return response.text