### Use case of secret manager sample 

# objective
Marvel API (3rd Party API)
1. Create an developer account on https://developer.marvel.com/account
2. Obtain an public and private key to access read permission on marvel apis
Secret Manager
1. add public and private key in Amazon Secrets Manager using console, SDK or cloud-formation.

Lambda
1. Create a lambda function.
2. This lambda function accept character name as parameter and use this parameter to fetch character details from Marvel APis. ie. https://gateway.marvel.com:443/v1/public/characters?name=loki&apikey=myapikey
3. useful links for understanding of Marvel Apis 
	https://developer.marvel.com/docs
	https://developer.marvel.com/documentation/authorization
4. use HttpClient and fetch character content from mentioned Marvel APi.
	