<a href="https://geradorderascunhoscomdocker.onrender.com/">Ver projeto em produção</a>

# Gerador de Rascunhos para liquidação no âmbito da UFF
Extrai dados de pdfs de notas de empenho para rascunhos de liquidação 

<b>Necessário ter instalado:</b>
<ol>1. VS CODE (IDE)</ol>
<ol>2. Python</ol>
<ol>3. Git</ol>
<ol>4. Docket Desktop</ol>

<b>Clonar projeto</b>

    git clone  https://github.com/GeradorDeRascunhoscomDocker.git

<b>Acessar pasta do projeto (verifique o seu)</b>

    cd C:\Users\PROPPI_01\Desktop\Geradorderascunho
    
<b>Comando no terminal - baixar bibliotecas</b>
    
    pip install -r requirements.txt

<b>Executar projeto para verificar se está rodando corretamente na porta 5000</b>
    
    python app.py

<b> Abrir DOCKER DESKTOP e criar imagem via terminal do VS CODE 

    docker build -t gerador-rascunhos .  

<b> Criar container com docker

    docker run -p 5000:5000 gerador-rascunhos

<b> Se quiser, gerar um app executável para windows</b>

pyinstaller --onefile --icon=static/IconeApp.ico --add-data "static/style.css;static" --add-data "static/script.js;static" --add-data "static/imgp.jpg;static" --add-data "static/imgg.jpg;static" --add-data "static/logo.png;static" --add-data "static/faviconuff.ico;static" --add-data "static/icon.jpg;static" --add-data "templates/index.html;templates" --add-data "pdfs/NE_153248_2025NE000104_v002_PF1522761_20250731142515.pdf;pdfs" --add-data "Modelo.xlsx;." --add-data "Consolidado.xlsx;." --add-data "README.md;." --add-data "requirements.txt;." --add-data "LICENSE;." --add-data "RascunhosGerados/Rascunho inicial-104.xlsx;RascunhosGerados" app.py





