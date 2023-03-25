# Week 3 — Decentralized Authentication

1. go to AWs console and open cognito


userpool when making a webapp, and youwant login and signup
federated identity - you want to use from other apps


enabling the hosted UI will tell cognito to use the AWS managed login/signup pages. In this project we will have our own pages for these purposes

we dont need a callback url, used to pass in the app.


CLI imeplemetation:

AWS Amplify:-

1. AWS AMPlify is a SDK for common serverless librarires, is a hosting platform, way of provisioing backend serverless solution, is a low code soltuion, for hosting static website.
2. Only way to sue cognito client side is to use AWS amplify JS library. 

cd to frontend-react-js
and run 
npm i aws-amplify --save

configure amplify in app.js as 

Amplify.configure({
  "AWS_PROJECT_REGION": process.env.REACT_AWS_PROJECT_REGION,
  "aws_cognito_identity_pool_id": process.env.REACT_APP_AWS_COGNITO_IDENTITY_POOL_ID,
  "aws_cognito_region": process.env.REACT_APP_AWS_COGNITO_REGION,
  "aws_user_pools_id": process.env.REACT_APP_AWS_USER_POOLS_ID,
  "aws_user_pools_web_client_id": process.env.REACT_APP_CLIENT_ID,
  "oauth": {},
  Auth: {
    // We are not using an Identity Pool
    // identityPoolId: process.env.REACT_APP_IDENTITY_POOL_ID, // REQUIRED - Amazon Cognito Identity Pool ID
    region: process.env.REACT_AWS_PROJECT_REGION,           // REQUIRED - Amazon Cognito Region
    userPoolId: process.env.REACT_APP_AWS_USER_POOLS_ID,         // OPTIONAL - Amazon Cognito User Pool ID
    userPoolWebClientId: process.env.REACT_APP_AWS_USER_POOLS_WEB_CLIENT_ID,   // OPTIONAL - Amazon Cognito Web Client ID (26-char alphanumeric string)
  }
});

Add env variables from above to docker-compose to frontend-JS section

all env variable of react app should be prefixed with REACT_APP, this is a must.

in homefeed.js

1.import auth
2.set react state for setting varaibales to modify later.
3. middleware is for server side stuff. In app.py, there are middleware such aws -xray middleware to help inercept the request.
No middleware stuff for cognito
4. Replace teh mocked cookie with the auth


unabel to get invalid username/passwor on the front end..
so modified the catch block to remove the duplicate and it worked.
Then created a user under the user group pool and tried again. Was unable to confirm account, no email was received. 
Whent ried on FE, received unable to read 


The uissue is with the account not being confirmed and at force change password status, used in the line 

"localStorage.setItem("access_token", user.signInUserSession.accessToken.jwtToken)" in on submit  function of SigninPage.js

To fix this, used CLI and rant eh following command

aws cognito-idp admin-set-user-password \
  --user-pool-id us-east-1_pv7xGuGbk \
  --username laksri \
  --password Test123! \
  --permanent

After running this cpmmand, the user status tuend as confirmed.
And teh sign in worked.

Added a console.log('user', user) to print the user object to the console, to inspect when signed in.

On the left panel, My Name ,@handle needs to customised and this comes from preffer username set in teh userpool in AWS console.



You could store more infoon the user in cognito, if needed.

Delete the user via the AWS console before the enxt step.

Implement sign up page:
1. Edit the signup.js file to replace teh onsubmit to remove cookies with a call to auth function.

the authsignup call is made with email as username , and other params , and this enables autosingn, set to true.

go to confirmation page:
Place the import and the on submit replace as edits.

Refreshed the page an got the error
"Username cannot be of email format, since user pool is configured for email alias.".

To fix this,

recreated teh userpool since both email and user anme options were chose  for pool isgn in options.

Created teh user using the signup page, confimed emailaddress and noticed it on the AWS console as user created.

Implement authenticatd and unathenticated requests:
1. change the 

Implement recovery page:




