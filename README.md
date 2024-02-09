# Código resultante da NLW expert
Código resultante da NLW expert do inicio de 2024, com algumas alterações para higienizar o nome do arquivo criado e suportar a criação de códigos QR!

![2024-02-09_00_54_50](https://github.com/renanbrayner/nlw-expert-python-2024/assets/29386809/b5c4ab12-3c09-45ed-ab5c-df39befb014c)


## Como executar o projeto
1. Clone o repositório `git clone https://github.com/renanbrayner/nlw-expert-python-2024.git`
2. Entre na pasta do projeto `cd nlw-expert-python-2024`
3. Instale as dependencias com `pip install -r requirements.txt`
4. Execute o programa com `python run.py`
5. Pronto! O projeto deve esta funcionando no localhost porta 3000

## Endpoints
###***POST*** `/create_qrcode`
Cria um código QR
```json
{
	"code": "https://renanbrayner.com"
}
```

###***POST*** `/create_barcode`
Cria um código de barras
```json
{
	"code": "https://renanbrayner.com"
}
```

## Curls de exemplo
**Código QR**
```bash
curl --request POST \
  --url http://localhost:3000/create_qrcode \
  --header 'Content-Type: application/json' \
  --data '{
	"code": "https://renanbrayner.com"
}'
```

**Código de barras**
```
curl --request POST \
  --url http://localhost:3000/create_bar \
  --header 'Content-Type: application/json' \
  --data '{
	"code": "https://renanbrayner.com"
}'
```
