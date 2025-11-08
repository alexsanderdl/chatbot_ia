from flask import Flask,request, jsonify, render_template
from flask_cors import CORS #Ler aquivo HTML

app=Flask(__name__) #habilita a função para ler dados
CORS(app)

def get_ai_response(user_menssage):
    
    "Retorna uma resposta simulada baseado na mensagem do usuário"
    msg= user_menssage.lower()

    if "olá"in msg or "oi" in msg:
        return"olá, o servidor ia recebeu a mensagem"
    elif "agente de IA" in msg:
        return "Eu sou o agente de ia e estou funcionando"
    elif "python" in msg:
        return "o agente de ia está funcionando"
    else:
        return f"recebi a mensagem: '{user_menssage}'. sou seu assistente pessoal"
    
@app.route('/api/chat', methods=['POST'])
def chat ():
    data=request.get_json
    user_message=data.get('message','')
     # ✅ CORREÇÃO: Salva o retorno da função na variável 'ai_text'
    ai_text = get_ai_response(user_message) 
    return jsonify({
        'status': 'sucess',
        'response': ai_text})

@app.route('/', methods=['GET'])

def index ():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
