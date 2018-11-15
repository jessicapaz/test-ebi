# Instalação

`$ git clone https://github.com/jessicapaz/test-ebi.git`

`$ cd test-ebi`

`$ pipenv install`

`$ pipenv shell`

### Modifique o arquivo .env e em seguida:

`$ python manage.py migrate`

# Tests

`$ python manage.py test`

# Documentação

## **Seller**
### Url : '/seller/'

### POST:
```
{
  "name": "test",
  "rg": "78987525",
  "cpf": "03589774158",
  "phone": "9181875836",
  "seller": {
    "salary": 5000.80
  }
}
```
