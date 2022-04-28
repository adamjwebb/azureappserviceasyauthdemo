# Example of leveraging EasyAuth in Azure App Service to call an API and delegate authorization

The goal of this repo is to provide an example of how to delegate AzureAD authentication from a frontend React SPA app to a backend Python Flask app with minimal code by leveraging Azure App Service's EasyAuth capabilities.

## Infrastructure Configuration

### Create Frontend App

 1. Create an Azure Web App for the front end React app
 2. Enable authentication (EasyAuth) with AzureAD identity provider
    1. Select "Authentication" and then "Add Idenity Provider"
    2. Choose "Microsoft" as the Identity Provider
    3. Settings:
       1. App Registration Type : Create new app registration
       2. Supported Account Types : Current tenant - Single tenant
       3. Restrict Access : Require Authentication
       4. Unauthenticated requests : HTTP 302 Found redirect: recommended for websites
       5. Redirect to : Microsoft
       6. Token Store : Enabled
       7. Permissions : User.Read (default)
    4. Select "Add"
   
 ### Create Backend App
 
 1. Create an Azure Web App for the back end Python Flask app
 2. Enable authentication (EasyAuth) with AzureAD identity provider
    1. Select "Authentication" and then "Add Idenity Provider"
    2. Choose "Microsoft" as the Identity Provider
    3. Settings:
       1. App Registration Type : Create new app registration
       2. Supported Account Types : Current tenant - Single tenant
       3. Restrict Access : Require Authentication
       4. Unauthenticated requests : HTTP 401 Unauthorized: recommended for APIs
       5. Redirect to : Microsoft
       6. Token Store : Enabled
       7. Permissions : User.Read (default)
    4. Select "Add"
 3. Configure CORS for frontend app to access backend app
     1. Select "CORS"
     2. Add the FQDN of the frontend app e.g. https://frontendapp.azurewebsites.net
     3. Click "Save"


### Add backend app to the generated AzureAD access token for the frontend app

 1. Navigate to the backend app in the Azure Portal
 2. Select the Authentication configuration and copy the App (client) ID
 3. Open https://resources.azure.com/ in the browser
 4. Locate the frontend web app, select config > authsettingsV2
 5. Navigate to properties > identityProviders > azureActiveDirectory > login
 6. Add the below configuration and save, ensuring to replace << backend app App ID >> with the copied App ID from the backend app

```
"loginParameters": [
     "response_type=code id_token",
     "scope=openid api://<< backend app App ID >>/user_impersonation"
        ],
```

## Code deployment

1. Deploy code in "frontend" repo folder to frontend app
2. Deploy code in "backend" repo folder to backend app

## Confirm AzureAD authentication delegation from frontend to backend app

1. Navigate to the frontend app URL in the browser
2. When prompted, login to your AzureAD account
3. Press F12 to open the browser developer tools and select "Console"
4. You should see a console log, which is returned from the backend app, and includes:
    1. X-MS-CLIENT-PRINCIPAL-IDP header (Identity Provider e.g. AAD)
    2. X-MS-CLIENT-PRINCIPAL header (Encoded user claims)
    3. X-MS-CLIENT-PRINCIPAL-NAME header (authenticated user email)

If you receive 401 unauthorized errors in the console log, please hit Ctrl + F5 to fully refresh the app. This may be due to the timing of the call to the backend app and the availability of the user access token.
