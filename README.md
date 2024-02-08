# TECHIN510lab4
## Overview
In undertaking this project, I aimed to create a comprehensive application that showcases my skills in web development, automation through GitHub Actions, and cloud services management with Azure. The World Clock application is designed to provide users with the ability to view the current time in various locations around the world, with additional features for those interested in real-time data and database integration.
## How to run
# Azure Web App for World Clock:
I deployed the web application to Azure App Service by setting up an App Service plan, configuring the web app, and deploying the code from my GitHub repository.
The web app features a dropdown menu for selecting locations and uses JavaScript to update the times every second. I utilized APIs like Intl.DateTimeFormat for handling time zones.
# GitHub Action Setup:
In my repository, I created a .github/workflows directory and added a YAML file to define the GitHub Action.
I set up the action to run every 15 minutes using the cron syntax in the on.schedule field. This action triggers scripts such as app.py for the main application logic, and optionally hello.py for bonus tasks like data scraping.
# PostgreSQL Server on Azure:
I used Azure's Database service for PostgreSQL to set up a PostgreSQL database on a free tier.
My application or scripts connect to this PostgreSQL database using the connection string provided by the Azure portal, which I modified as necessary for my application's needs.
## Lessons Learned
Front-End Development: Developing the World Clock application taught me the nuances of client-side programming, including how to handle time zones and update the UI asynchronously.
Automation with GitHub Actions: Implementing a CI/CD pipeline using GitHub Actions showed me the importance of automation in software development, particularly for periodic tasks.
## Question
How can I optimize data ingestion into PostgreSQL for efficiency and reliability, especially with large volumes of real-time data?
