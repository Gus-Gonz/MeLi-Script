import requests
import os


def get_products_by_id():

    list_of_products = []
    each_product = {}

    seller_id = input("Ingrese el número de ID que desea buscar: ")
    site_id = "MLA"

    url = (
        f"https://api.mercadolibre.com/sites/{site_id}/search?seller_id={seller_id}")

    payload = {}
    headers = {}

    response = requests.get(url, headers=headers, data=payload)
    data = response.json()
    how_many_results = len(data['results'])

    for i in range(how_many_results):

        each_product['ID'] = data['results'][i]['id']
        each_product['TITLE'] = data['results'][i]['title']
        each_product['CATEGORY_ID'] = data['results'][i]['category_id']

        url = (
            f"https://api.mercadolibre.com/categories/{each_product['CATEGORY_ID']}")
        response = requests.get(url, headers=headers, data=payload)
        each_product['NAME'] = response.json()['name']
        list_of_products.append(each_product)

        try:
            log_file = seller_id + ".log"
            does_exist = os.path.isfile(log_file)
            with open(log_file, 'a+') as file:

                if not does_exist:
                    open(log_file, 'w')
                    file.writelines(str(list_of_products))
                except IOError:
                    print("Ocurrio un error con el archivo")

        except IOError:
            print("Opción ingresada Incorrecta !")


get_products_by_id()
