# Example of leveraging EasyAuth in Azure App Service to call an API and delegate authorization


-- vdvsd


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
   
  
 1. Create an Azure Web App for the back end Python Flask app
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
 
 
 1. A numbered list
       1. test
       2. 
              1. A nested numbered list
              2. Which is numbered
 
 
 
 4.  ds
 5.  
   3.   test
 4.   test
 5. 
 6. A numbered list
              1. A nested numbered list
              2. Which is numbered
          2. Which is numbered



The goal of this repo is to provide examples of how to automate the configuration of Azure Privileged Identity Management (PIM) Role Settings for Azure Resources.

When assisting a customer with automating configuration of PIM role settings for Azure Resources, I struggled to locate any concrete examples or sample code. This was most likely due to the PIM APIs being in public preview.

Documentation to configure the role settings manually for an Azure Resource can be located here.

PowerShell
Pre-requisites
Latest version of the Azure Active Directory V2 Preview Module
Discover and on-board Azure Subscription to PIM
Azure Subscription Id
Azure RBAC role Id e.g. Contributor is b24988ac-6180-42a0-ab88-20f7382dd24c
Steps
Ensure the pre-requisites are met
Clone this repo or open the PowerShell file in an IDE e.g. Visual Studio Code or PowerShell ISE
Replace the token with your Azure Subscription Id on line 7
Run the commands in order
Results
The results of running through all the commands in the PowerShell file:

Azure MFA will be required upon PIM role Activation for the Azure Contributor role
Azure MFA will be required upon active assignment of the Azure Contributor role wthin PIM
You can validate the above settings by opening the Azure Portal and navigating to Privileged Identity Management > Azure Resources > Azure Subscription > Settings > Contributor > Edit > Activation/Assignment

References
https://www.jasonfritts.me/2021/07/20/automating-azure-privileged-identity-management-pim-with-powershell https://docs.microsoft.com/en-us/powershell/module/azuread/?view=azureadps-2.0-preview#privileged-role-management
