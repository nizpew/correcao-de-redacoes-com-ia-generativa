
# Projeto Correção de Redações com IA Generativa

## Visão Geral

Desenvolvi uma solução inovadora para automatizar a correção de redações manuscritas, utilizando tecnologias avançadas de OCR e inteligência artificial generativa. O sistema permite que estudantes enviem fotos de suas redações e recebam uma análise detalhada com notas e feedbacks personalizados em tempo real.

## Objetivos do Projeto

- Automatizar o processo de correção de redações, reduzindo o tempo e esforço dos avaliadores humanos.  
- Garantir feedbacks precisos e construtivos baseados em critérios oficiais de avaliação.  
- Facilitar o acesso dos alunos a avaliações rápidas, promovendo melhoria contínua na escrita.

## Tecnologias Utilizadas

- **Frontend:** React com Vite, garantindo uma interface leve, responsiva e de fácil manutenção.  
- **Backend:** Flask em Python, para processamento eficiente e integração com serviços externos.  
- **OCR:** Tesseract, para extração precisa do texto manuscrito a partir das imagens enviadas.  
- **IA Generativa:** Integração com GPT-3.5 via API Poe.com para análise semântica e avaliação textual.  
- **Banco de Dados e Armazenamento:** Firebase Firestore e Storage, garantindo escalabilidade e segurança dos dados.

## Resultados Alcançados

- Implementação de pipeline completo desde o upload da redação até a entrega da análise detalhada.  
- Precisão de extração textual superior a 85% em manuscritos claros, com feedbacks alinhados aos critérios oficiais.  
- Interface intuitiva que promove engajamento dos alunos e facilita o acompanhamento do desempenho.

## Diferenciais Técnicos

- Uso de tecnologias open source e gratuitas para garantir baixo custo e fácil replicabilidade.  
- Arquitetura modular que permite fácil extensão para novos recursos, como correção de gramática e sugestões personalizadas.  
- Configuração de ambiente com práticas recomendadas de segurança e escalabilidade.

## Como Executar

- Configuração rápida com scripts para ambiente virtual Python e instalação de dependências.  
- Frontend moderno com hot reload para desenvolvimento ágil.  
- Documentação clara para facilitar a manutenção e futuras integrações.


              
       cd project-name
       
       
       cd frontend
       npm install
       npm run dev
       
       
       cd ../backend 
       python3 -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt            
       python app.py                               

---

Este projeto demonstra minha capacidade de integrar múltiplas tecnologias modernas para resolver problemas reais com impacto educacional, além de minha atenção a qualidade, usabilidade e escalabilidade.

---

## Dependências completas:


    sudo apt update
    sudo apt install -y python3 python3-pip python3-venv tesseract-ocr tesseract-ocr-por libsm6 libxext6 libxrender-dev build-essential
    
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install flask flask-cors requests python-dotenv pillow pytesseract opencv-python matplotlib tensorflow keras fastai alive-progress glob2 textblob transformers sentencepiece jiwer datasets evaluate accelerate protobuf==3.20.1 tensorboard




# Fotos

![image](https://github.com/user-attachments/assets/89cf2a23-2b20-4b05-ad70-1a22bd552f15)





## futuras mudancas:

-melhorar OCR (https://github.com/LPBeaulieu/Handwriting-OCR-ScriptReader/tree/main)



[1] Aluno tira foto da redação (escrita à mão)
       |
       v
[2] Envia a imagem via app web (React + Vite no GitHub Pages ou Netlify)
       |
       v
[3] Backend recebe imagem (Flask/FastAPI no Replit ou Render.com)
       |
       v
[4] Salva temporariamente a imagem (em Firebase Storage ou local)
       |
       v
[5] Backend roda Tesseract OCR para extrair o texto da imagem
       |
       v
[6] Texto é armazenado em banco NoSQL gratuito (Ex: MongoDB Local ou Firestore Free)
       |
       v
[7] Aluno solicita análise via botão no frontend
       |
       v
[8] Backend recupera o texto e monta o prompt
       |
       v
[9] Envia prompt + texto para:
       - GPT-3.5 via Poe.com API (gratuito)
       - ou LM Studio com modelo local (ex: Mistral ou Phi)
       |
       v
[10] IA retorna nota da redação e explicação
       |
       v
[11] Frontend exibe a análise para o aluno

