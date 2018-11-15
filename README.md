# Instalação

`$ git clone https://github.com/jessicapaz/test-ebi.git`

`$ cd test-ebi`

`$ pipenv install`

`$ pipenv shell`

### Modifique o arquivo .env e remova o "-example"
### Em seguida:

`$ python manage.py migrate`

# Tests

`$ python manage.py test`

# Documentação

## **Product/Service**

### POST:
### Url : '/product-service/'

Example:
```
{
   "type_choice": "S",
   "name": "service",
   "description": "des",
   "price": "454.00",
   "commission_rate": 0.02
 }
```
### GET:
### Url : '/product-service/'

Example:
```
[
  {
     "type_choice": "S",
     "name": "service",
     "description": "des",
     "price": "454.00",
     "commission_rate": 0.02
   },
   {.....}
 ]
```
### PUT:
### Url : '/product-service/id'

Example:
```
{
   "type_choice": "P",
   "name": "service update",
   "description": "des",
   "price": "454.00",
   "commission_rate": 0.02
 }
```
### DELETE:
### Url : '/product-service/id'

Example:
```
{
   "type_choice": "P",
   "name": "service update",
   "description": "des",
   "price": "454.00",
   "commission_rate": 0.02
 }
```
### Most Sold List:
### Url : 'most-sold/?start=YYYY-MM-DD&end=YYYY-MM-DD'

Example:
```
[
  {
    "type_choice": "S",
    "name": "aaa",
    "description": "aa",
    "price": "87897.00",
    "commission_rate": 0.004
  },
  {.....}
]
```
### Client Most Sold List:
### Url : '/client-most-sold/?start=YYYY-MM-DD&end=YYYY-MM-DD&cpf=cpf'

Example:
```
[
  {
    "type_choice": "P",
    "name": "product 1",
    "description": "des",
    "price": "97.00",
    "commission_rate": 0.004
  },
  {.....}
]
```
## **Seller**

### POST:
### Url : '/seller/'

Example:
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
### PUT:
### Url : '/seller/id'

Example:
```
{
  "name": "test update",
  "rg": "78987525",
  "cpf": "03589774158",
  "phone": "9181875836",
  "seller": {
    "salary": 5000.80
  }
}
```
### Seller Commission:
### Url : '/seller-commission/?start=YYYY-MM-DD&end=YYYY-MM-DD&cpf=cpf'
```
{
  "total-commission": 154.77
}
```

## **Client**

### POST:
### Url : '/client/'

Example:
```
{
  "name": "test",
  "rg": "78987525",
  "cpf": "03589774158",
  "phone": "9181875836",
  "client": {
    "email": "test@gmail.com"
  }
}
```
### PUT:
### Url : '/client/id'

Example:
```
{
  "name": "test update",
  "rg": "78987525",
  "cpf": "03589774158",
  "phone": "9181875836",
  "client": {
    "email": "test@gmail.com"
  }
}
```

## **Sale**

### POST:
### Url : '/sale/'

Example:
```
{
  "product_service": [
    1, 2, 4
  ],
  "seller": 1,
  "client": 1,
  "timestamp": "2018-08-27T12:00:00Z"
}
```
### GET:
### Url : '/sale/'

Example:
```
[
  {
    "product_service": [
        2, 6
    ],
    "seller": 1,
    "client": 2,
    "timestamp": "2018-08-27T12:00:00Z"
  },
   {.....}
 ]
```
### PUT:
### Url : '/sale/id'

Example:
```
{
  "product_service": [
      2
  ],
  "seller": 1,
  "client": 1,
  "timestamp": "2018-11-15T12:00:00Z"
}
```
### DELETE:
### Url : '/sale/id'

Example:
```
{
  "product_service": [
      2
  ],
  "seller": 1,
  "client": 1,
  "timestamp": "2018-11-15T12:00:00Z"
}
```
