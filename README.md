# Lifestores Backend

Lifestores Backend is a GraphQL backend project built using the django and graphene and containerized using docker. The project provides services for creating, getting all, getting a specific
product, updating a specific product, and deleting product entities such as represented in the JSON payload defined below:
```JSON
[
    {
        "name":"Paracetamol",
        "description":"Paracetamol (acetaminophen) is a pain reliever and a fever reducer",
        "sku":"8HE902",
        "price":300,
        "image":"https://www.m-medix.com/2759-large_default/emzor-paracetamol-tablets.jpg"
    },
    {
        "name":"Prednisolone",
        "description":"Prednisolone is a corticosteroid (cortisone-like medicine or steroid). It works on the immune system to help relieve swelling, redness, itching, and allergic reactions",
        "sku":"8HE809",
        "price":600,
        "image":"https://5.imimg.com/data5/RU/SX/JJ/SELLER-109604861/prednisolone-tablet-500x500.jpg"
    },
    {
        "name":"Lumefantrine",
        "description":"Lumefantrine is an antimalarial agent used to treat acute uncomplicated malaria.",
        "sku":"8HE809",
        "price":1200,
        "image":"https://i1.wp.com/nimedhealth.com.ng/wp-content/uploads/2020/09/IMG_20200920_082326-1.jpg?fit=2487%2C1599&ssl=1"
    },
    {
        "name":"Coflin",
        "description":"Coflin Is Used To Treat Coughs And Congestion Caused By The Common Cold, Bronchitis, And Other Breathing Illnesses.",
        "sku":"8HE809",
        "price":1200,
        "image":"https://www.m-medix.com/2677-large_default/dr-meyers-coflin-expectorant-100ml.jpg"
    }
]
```
## Installation

To run the project on docker, run the following commands(from your desired folder):
```bash
# Clone the git repo
git clone https://github.com/TeeblaQ1/lifestores_backend.git

# Build docker image (from the root folder)
docker build .

# The SQLite DB used has been pushed to the repo as well but the following commands would be useful if the DB was not pushed
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web django-admin loaddata data.json    # The data.json file has been prepared as a fixture


# Run the image (running with flag -d is optional and would only run in detached mode)
docker-compose up -d
# Running on http://127.0.0.1:8000/api
```

## Testing

The application has been tested and confirmed to pass all tests around the CRUD operation using pytest. To test the docker image, while the image is running, use the following command.
```bash
# Optionally, if not already installed along other requirements, install pytest and mixer
docker-compose exec web pip install pytest mixer
# Run this command to carry out the test
docker-compose exec web python manage.py test
```

## Scalability

The project allows for scalability both vertically and horizontally as it contains features that allow our application to be stateless. Third-party services are used for all states. E.g. Database, caching, etc. The database for instance can be changed from the default SQLite database to another database running on another server instance.  Also, since Django is pluggable, we can replace existing "built-in" features with a custom feature we want to add support for in later times.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
