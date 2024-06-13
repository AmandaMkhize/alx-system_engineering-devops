Project Overview
This project involves setting up development and production environments for a Flask application using Gunicorn and Nginx on Ubuntu 16.04. The process includes configuring the server, proxying requests with Nginx, and ensuring the application runs efficiently in both environments.

I configured a development environment to serve a Flask application using Gunicorn and tested it on web-01. The application was set to serve content on port 5000. For production, I set up Gunicorn to handle requests on the same port and configured Nginx to proxy requests from port 80 to the Gunicorn server on port 5000. Additionally, I added a route with query parameters to handle dynamic content, proxying requests on a different route to another Gunicorn instance. Finally, I set up Nginx to serve an API and the dynamic version of the AirBnB clone, ensuring static assets were correctly served and routes properly configured.

This setup ensures a scalable, efficient deployment of the Flask application using industry-standard practices.
