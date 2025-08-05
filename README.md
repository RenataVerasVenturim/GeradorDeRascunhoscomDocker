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

<b> Abrir DOCKER DESKTOP e criar imagem via terminal do VS CODE </b>

    docker build -t gerador-rascunhos .  

<b> Criar container com docker</b>

    docker run -p 5000:5000 [nome_imagem]
    
<b> OU para rodar sem prender terminal:</b>
    
    docker run --name [nome_container] -p5000:5000 -d [nome_imagem]
    

<b>Distruibuir imagem</b>

<b>1- Salvar imagem em um arquivo .tar e distribuir via pendrive, drive, e mail:</b>

    docker save -o meuapp.tar projeto-docker-teste

<b>Abrir arquivo em MAC, WINDOWS, LINUX</b>

<b>gerar imagem</b>
    
    docker load -i meuapp.tar

<b>criar container</b>

    docker run --name meuapp -p 5000:5000 -d projeto-docker-teste

<b>2- Publicar no Docker Hub</b>

    docker login

    docker tag projeto-docker-teste renataveras/projeto-docker-teste:latest 
    
    docker push renataveras/projeto-docker-teste:latest

<b>Abrir arquivo em MAC, WINDOWS, LINUX</b>

*puxar imagem do Docker Hub
    docker pull renataveras/projeto-docker-teste:latest

*criar container
    docker run --name apprecebido -p5000:5000 -d renataveras/projeto-docker-teste  

<b> Se quiser, gerar um app executável para windows</b>

pyinstaller --onefile --icon=static/IconeApp.ico --add-data "static/style.css;static" --add-data "static/script.js;static" --add-data "static/imgp.jpg;static" --add-data "static/imgg.jpg;static" --add-data "static/logo.png;static" --add-data "static/faviconuff.ico;static" --add-data "static/icon.jpg;static" --add-data "templates/index.html;templates" --add-data "pdfs/NE_153248_2025NE000104_v002_PF1522761_20250731142515.pdf;pdfs" --add-data "Modelo.xlsx;." --add-data "Consolidado.xlsx;." --add-data "README.md;." --add-data "requirements.txt;." --add-data "LICENSE;." --add-data "RascunhosGerados/Rascunho inicial-104.xlsx;RascunhosGerados" app.py





