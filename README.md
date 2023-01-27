### AWS Cognito Sidecar implementation

Ingredients:

* [AWS Cognito User Pool](https://us-east-1.console.aws.amazon.com/cognito/home)


### Environment Variables needed for project:

I store these in a `.devcontainer/devcontainer.env` file, the devcontainer loads them automatically. 


```
FLASK_SESSION_SECRET=secret
LOGIN_URL=https://{{COGNITO_APP_DOMAIN}}.auth.{{COGNITO_APP_REGION}}.amazoncognito.com/login?client_id={{COGNITO_CLIENT_ID}}&response_type=code&scope=aws.cognito.signin.user.admin+email+openid+phone+profile&redirect_uri={{REDIRECT_URL}}
COGNITO_APP_DOMAIN=
COGNITO_APP_REGION=us-east-1
COGNITO_USERPOOL_ID=us-east-1_*******
COGNITO_CLIENT_ID=
COGNITO_CLIENT_SECRET=
REDIRECT_URL=
```
