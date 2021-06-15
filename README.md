# formula-analytcs-one

## Configurando o banco de dados Mysql
####A. Instalação do conector mysql para python.
>- __Se você usar windows__ </br>
   > 1.  baixe o conector mysql de acordo com sua máquina nesse `link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient`
   > 2.  instale o mysqlclient: `pip install mysqlclient-x.x.x-cpxx-cpxxm.whl`  

B. Configurações no Django Project
>- diretório: formula-analitycs-one/formula1/settings</br></br>
`DATABASES = { 
'default': { 
'NAME': 'bd_f1', 
'ENGINE': 'django.db.backends.mysql', 
'USER': 'root', 
'HOST': 'localhost', 
'PORT': 3306, 
'PASSWORD': '',
}`
}

C. Construa o banco de dados inicial do django executando as  migrates com: `python manage.py migrate`

D. Gere models com base nos modelos existentes no banco de dados com `python manage.py inspectdb > models.py`