# python-finance-api
python finance api project 

Endpoints: 
    /revenue - gets revenue records
    /customers - gets customers records

Refactored application into scalable architecture using service and routing layers

Connected to SQL Server Database using pydoc

Refacrored data layer to pull from Database

Added new endpoint revenue-trend to find revenue by month aggregated - analytics endpoint

Added Customers route with path parameter and dynamic query

Added Caching for performance