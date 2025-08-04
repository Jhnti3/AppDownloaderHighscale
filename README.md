🎬 AppDownloaderHighscale — Downloader de Vídeos e Áudios do YouTube
Aplicação web simples para baixar vídeos e áudios diretamente do YouTube em formato MP3 ou MP4.
(Serão implementadas dentro de um projeto maior, assim como o image to text)

📌 Funcionalidades
Download de vídeos ou áudios com apenas um clique

Interface limpa e responsiva

Cabeçalho fixo com layout profissional

Mensagens informativas e alerta de uso legal

Tooltip explicativo com ícone SVG

🛠️ Como rodar localmente
1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/Jhnti3/AppDownloaderHighscale.git
cd AppDownloaderHighscale
2. Crie e ative um ambiente virtual (opcional, mas recomendado)
bash
Copiar
Editar
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Rode o app
bash
Copiar
Editar
python app.py
Acesse no navegador:

arduino
Copiar
Editar
http://localhost:5000
📂 Estrutura de Pastas
bash
Copiar
Editar
AppDownloaderHighscale/
│
├── app.py                  # Arquivo principal Flask
├── downloader.py           # Lógica de download com pytube
├── requirements.txt        # Dependências do projeto
│
├── static/                 # Arquivos estáticos
│   ├── css/style.css       # Estilos da interface
│   └── [vídeos]            # Vídeos de teste (não necessários para rodar)
│
├── templates/
│   └── index.html          # Página principal (Jinja2)
│
└── README.md               # Este documento
⚠️ Aviso Legal
Este projeto é apenas para fins educacionais.
O uso indevido da ferramenta para baixar conteúdo protegido por direitos autorais é de responsabilidade do usuário.

Ao utilizar a função de download, você declara que o conteúdo será usado apenas para fins pessoais e não comerciais, conforme descrito na mensagem de aviso do sistema.

✅ Status do Projeto
🟢 Versão inicial pronta e funcional
Melhorias visuais e organizacionais serão feitas nas próximas versões.
