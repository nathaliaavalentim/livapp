Agradeço o apoio financeiro da Fundação de Amparo à Pesquisa do Estado de Minas Gerais (FAPEMIG) para realização dessa esta pesquisa - DEMANDA UNIVERSAL Processo: APQ-00837-21.

Para clonar o projeto: git clone [https://github.com/nathyvalentim/livapp.git](https://github.com/nathaliaavalentim/livapp.git)


########################################################################
SOBRE O STI (analise_preferencia e analise_desemepenho):

Instalações Importantes: </br>
pip install asgiref==3.5.2</br>
pip install bleedfacedetector==1.0.17</br>
pip install cycler==0.11.0</br>
pip install Django==4.0.4</br>
pip install dlib==19.24.0</br>
pip install ec==0.2.5</br>
pip install ecapture==0.0.7</br>
pip install fonttools==4.33.3</br>
pip install kiwisolver==1.4.2</br>
pip install matplotlib==3.5.2</br>
pip install numpy==1.22.4</br>
pip install opencv-python==4.5.5.64</br>
pip install packaging==21.3</br>
pip install Pillow==9.1.1</br>
pip install pip==22.2.2</br>
pip install pyparsing==3.0.9</br>
pip install python-dateutil==2.8.2</br>
pip install setuptools==58.1.0</br>
pip install six==1.16.0</br>
pip install sqlparse==0.4.2</br>
pip install tzdata==2022.1</br>
</br>

Execução do projeto:
- Acessar via terminal a pasta do projeto que contenha o arquivo manage.py e executar o comando: python manage.py runserver 0.0.0.0:5000
- Para acesso remoto, executar o comando: ngrok http [port]


########################################################################

SOBRE O DASHBOARD (livApp_profissional):
Banckend:</br>
Instalar BD postgresql</br>
Instalar o ORM Prisma: yarn add prisma</br>
Instalar o Prisma Client: yarn add @prisma/client</br>
Renomear a pasta prisma e rodar npx prisma init para gerar o env</br>
No env, fazer as configurações de acordo com o seu banco</br>
Fazer as configurações do Prisma Client<br/>
Criar JWT secret no env (https://www.md5hashgenerator.com/)</br>
Migrations: yarn prisma migrate dev</br>
</br>
Instalações importantes para o dashboard:</br>
yarn add brcryptjs</br>
yarn add @types/brcryptjs</br>
yarn add jsonwebtoken   </br>
yarn add @types/jsonwebtoken</br>
yarn add dotenv</br>
</br>
Execuação do projeto (frontend e backend):</br>
yarn dev</br>

########################################################################
SOBRE O MIDDLEWARE (livapp_middleware):
Editar \src\DBConnection\ConnectPostgres.java com os dados do banco.

