import boto3


dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla =dynamodb.Table('tabla-juan-restrepo')

response = tabla.get_item(Key={'id':'2'})

print(response['Item'])

response = tabla.scan()

print(response['Items'])

tabla.put_item(Item={
    "id": "3",
    "numero":"Juan Pablo",
    "cuidad":"Medellin",
    "edad":35

})

tabla.put_item(Item=item)

#Leer un elemento de la tabla
response = tabla.get_item(key={'id':'3'})

print("Elemento antes de actualizar", response['Item'])

response = tabla.update_item(
    Key={
        'id': '3'
    },
    UpdateExpression='SET edad = :val1', #Expresion de actualizacion
    ExpressionAttributeValues={
        ':val1':34   #Nuevo valor para atributos2
    }
    
    )
    
    #Leer un elemento de la tabla
    response = tabla.get_item(key={'id':'3'})
    
    print("Elemento despues de actualizar", response['Item'])